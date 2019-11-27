#!/usr/bin/env python
# -*-coding:utf-8 -*-
# *******************************************************************************
# �ļ����ƣ�service_monitor.py
# �����������������ͨ�ü��
# �� �� �� 
# �� �� �� 
# �� �� �ߣ�hyn
# �������ڣ�20191010
# �޸���־��
# �޸����ڣ�
# *******************************************************************************
# ������ø�ʽ��python service_monitor.py
# *******************************************************************************

import os
import sys
import json
import time
import config

# �����ṹ���:
# 1.��ʼ��
# 2.��������
# 3.�������ݱ༭
# 4.���Ͷ���

class ServiceMonitor():
	
	# ��ʼ��
	def __init__(self):
		
		# ��������
		self.sms_list=[]
		
	# ��������
	def request_data(self):
		
		# ѭ������������
		for service_name in config.service_list:
		
			# �������״̬�������������txt�ļ�
			exec_sh = 'curl -u admin:admin '+config.monitor_url+'/'+config.monitor_name+'/services/'+service_name+' > '+config.log_path+config.service_monitor+'.txt'
			# print 'exec_sh: '+exec_sh
			result_data = os.popen(exec_sh).readlines()
			
			try:
			
				self.sms_info(service_name,result_data)
			except Exception as e:
				print '# monitor '+service_name +'error,next'
				print e
				continue
	
	# �������ݱ༭
	def sms_info(self,service_name,result_data):
	
		# ��ȡkafka�����ļ���Ϣ
		f=open(config.log_path+config.service_monitor+'.txt')
		dict_data=json.load(f)

		# service��Ⱥ��Ϣ
		service_info=dict_data['alerts_summary']
		critical_info=service_info['CRITICAL']
		host_info=service_info['OK']
		host_count=len(dict_data['alerts'])
		if service_name=='HDFS':
			host_count=host_count-30
			
		print service_name+'��������������'+str(host_count)
		
		# ���񾯸���Ϣ
		
		# HDFS������Ҫ���⴦��
		
		if service_name=='HDFS':
			#if critical_info>-1:
			
			if critical_info>5:
				critical_sms_info=service_name+'����'+str(critical_info)+'��������ϢCRITICAL��'
				self.sms_list.append(critical_sms_info)
				print critical_sms_info
				
			
			# �����������
			#if host_info<host_count+1:
			if host_info<host_count:
				host_sms_info=service_name+'��������������������'+str(host_count)+'����'+str(host_info)
				self.sms_list.append(host_sms_info)
				print host_sms_info
			
			
		else:
			
			#if critical_info>-1:
			if critical_info>0:
				critical_sms_info=service_name+'����'+str(critical_info)+'��������ϢCRITICAL��'
				self.sms_list.append(critical_sms_info)
				print critical_sms_info
				
			
			# �����������
			#if host_info<host_count+1:
			if host_info<host_count:
				host_sms_info=service_name+'��������������������'+str(host_count)+'����'+str(host_info)
				self.sms_list.append(host_sms_info)
				print host_sms_info
		
		# ���Ͷ���s
		if config.send_flag:
			self.send_sms(service_name)
	
	# ���Ͷ���
	def send_sms(self,service_name):
		
		for sms_info in self.sms_list:
			
			# ���Ͷ���
			os.popen('sh send_sms.sh'+' '+sms_info+' '+config.all_info+' >> '+config.log_path+'service_monitor.log').readlines()
			
			# ����������д����־
			os.popen('echo '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' '+sms_info+' >> '+config.log_path+'service_monitor.log').readlines()
			
			print service_name+' ���ţ�'+sms_info
		
		self.sms_list=[]

# ��������
#if __name__=='__main__':
#	sm = ServiceMonitor()
#	
#	while True:
#		sm.request_data()
#		time.sleep(config.sleep_time)
#	
#	
