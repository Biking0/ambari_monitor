#!/usr/bin/env python
# -*-coding:utf-8 -*-
#********************************************************************************
# ** �ļ����ƣ�solr_monitor.py
# ** ����������solr��أ���ѯ��30����������
# ** ���������
# ** �� �� ��
# ** �� �� �ߣ�hyn
# ** �������ڣ�20191015
# ** �޸���־��
# ** �޸����ڣ�
# *******************************************************************************
# ** ������ø�ʽ��python solr_monitor.py
# *******************************************************************************

import os
import sys
import time
import json
import datetime
import config

# �����ṹ���:
# 1.��ʼ��
# 2.��������
# 3.�������ݱ༭
# 4.���Ͷ���

# solr���
class SolrMonitor():
	
	# ��ʼ��
	def __init__(self):
		
		# ɸѡ����
		self.all_info='ALL'
		# ��������
		self.sms_list=[]
		
		# ��ʼ����ѯ����
		end_time_stamp = str(time.time()).split('.')[0]
		self.activity_num=config.default_activity_num
		self.start_time_stamp=str(int(end_time_stamp)-config.search_time)+'000'
		self.end_time_stamp=end_time_stamp+'000'
		
	# ��������
	def request_data(self):
		
		# ��ѯsolr����������search_solr.txt
		solr_sh='curl -i -H "Content-Type:application/json" -X POST --data \''+'{"condition":"activity_num:'+self.activity_num+' AND start_time:{\\"'+self.start_time_stamp+'\\" TO \\"'+self.end_time_stamp+'\\"}" ,"tables":["DW_LOC_ZX_USER_BH_MIN_20190917"],"query":"","start":0,"return_fields":["phone","imsi","start_time","city_id","county_id"],"cursor_mark":"*","sort":"id desc","rows":10000}\' '+'http://10.218.146.65:9000/ocsearch-service/query/search | more'+' > '+config.log_path+'solr_monitor.txt'
	
		print solr_sh

		os.popen(solr_sh).readlines()
		self.sms_info()
		
	
	# �������ݱ༭
	def sms_info(self):
	
		# ��ȡ�����ļ���Ϣ
		f=open(config.log_path+'solr_monitor.txt').readlines()

		dict_data=json.loads(f[6])
		
		total_num=dict_data['data']['total']		
		
		# ���Զ��ŷ���
		#if True:
		# ������С�ھ���ֵ�������쳣
		if total_num<config.solr_data_num:		
		
			# ��������
			solr_info='solr�������쳣������30������������'+str(total_num)
			
			self.sms_list.append(solr_info)
			print solr_info
			
			# ���Ͷ���
			if config.solr_send_falg:
				self.send_sms()
		else:
			print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' '+'solr����,����30������������'+str(total_num)
	
	# ���Ͷ���
	def send_sms(self):
		
		for sms_info in self.sms_list:
			
			# ���Ͷ���
			os.popen('sh send_sms.sh'+' '+sms_info+' '+config.all_info+' >> '+config.log_path+'solr_monitor.log').readlines()
			
			# ����������д����־
			os.popen('echo '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' '+sms_info+' >> '+config.log_path+'solr_monitor.log').readlines()

		self.sms_list=[]
		

# ��������
#if __name__=='__main__':	
#	
#	while True:
#		
#		sm = SolrMonitor()
#		
#		sm.request_data()
#		# 10���Ӽ��
#		time.sleep(config.sleep_time)