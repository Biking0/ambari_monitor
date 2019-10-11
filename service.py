##!/usr/bin/env python
## -*-coding:utf-8 -*-
##********************************************************************************
## **  �ļ����ƣ�service_monitor.py
## **  �����������������ͨ�ü��
## **  �� �� �� 
## **  �� �� �� 
## **  �� �� �ߣ�hyn
## **  �������ڣ�20191010
## **  �޸���־��
## **  �޸����ڣ�
## *******************************************************************************
## **  ������ø�ʽ��python service_monitor.py
## *******************************************************************************

import os
import sys
import json
import time
import config

# �����ṹ���:
# 		��ʼ��
# 		��������
# 		�������ݱ༭
# 		���Ͷ���

class ServiceMonitor():
	
	# ��ʼ��
	def __init__(self):
		print 'init'
		
		# �Ƿ��Ͷ��ţ����Ͷ�����Ҫ��ΪTrue
		self.send_flag=True
		# ɸѡ����
		self.all_info='ALL'		
		# ��������
		self.sms_list=[]
		
		
	# ��������
	def request_data(self):
		
		print 'requestData'
		
		# ѭ������������
		for service_name in config.liu_service_list:
		
			# �������״̬�������������txt�ļ�
			exec_sh = 'curl -u admin:admin '+config.hbase_url+'/'+config.hbase_name+'/services/'+service_name+' > '+service_name+'.txt'
			print 'exec_sh: '+exec_sh
			result_data = os.popen(exec_sh).readlines()
			
			self.sms_info(service_name,result_data)					
	
	# �������ݱ༭
	def sms_info(self,service_name,result_data):
		print 'sms_info'
		
		# ��ȡkafka�����ļ���Ϣ
		f=open(service_name+'.txt')
		dict_data=json.load(f)

		# service��Ⱥ��Ϣ
		service_info=dict_data['alerts_summary']
		critical_info=service_info['CRITICAL']
		host_info=service_info['OK']
		host_count=len(dict_data['alerts'])
		print service_name+' ��������������'+str(host_count)		
		
		# ���񾯸���Ϣ
		#if critical_info>-1:
		if critical_info>0:
			critical_sms_info=service_name+' ����'+str(critical_info)+'��������ϢCRITICAL��'
			self.sms_list.append(critical_sms_info)
			print critical_sms_info
			#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()
		
		# �����������
		#if host_info<host_count+1:
		if host_info<host_count:
			host_sms_info=service_name+' ��������������������'+str(host_info)+'����'+str(host_info)
			self.sms_list.append(host_sms_info)
			print host_sms_info
			#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()
		
		# ���Ͷ���
		if self.send_flag:
			self.send_sms(service_name)
	
	# ���Ͷ���
	def send_sms(self,service_name):
		
		for sms_info in self.sms_list:
			os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info+' >> service_monitor.log').readlines()
			
			# ����������д����־
			os.popen('echo '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' '+sms_info+' >> service_monitor.log').readlines()
			
			print service_name+' ���ţ�'+sms_info
		
		self.sms_list=[]

# ����
if __name__=='__main__':
	sm = ServiceMonitor()
	
	while True:
		sm.request_data()
		time.sleep(1800)
	
	
