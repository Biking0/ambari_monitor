##!/usr/bin/env python
## -*-coding:utf-8 -*-
##********************************************************************************
## **  �ļ����ƣ�service_demo.py
## **  �����������������ͨ�ü��demo
## **  �� �� �� 
## **  �� �� �� 
## **  �� �� �ߣ�hyn
## **  �������ڣ�20191010
## **  �޸���־��
## **  �޸����ڣ�
## *******************************************************************************
## **  ������ø�ʽ��python service_demo.py KAFKA
## *******************************************************************************

import os
import sys
import json

# �Ƿ��Ͷ��ţ����Ͷ�����Ҫ��ΪTrue
send_flag=True

# Ĭ��Ϊkafka����������:KAFKA,FLUME,YARN,AMBARI_INFRA,HBASE
service_name=sys.argv[1]
if service_name is '':
	service_name='FLUME'
print '����������'+service_name

# ����kafka״̬���������kafka.txt
kafka_sh='curl -u admin:admin http://10.218.146.65:8080/api/v1/clusters/hbasecluster/services/'+service_name+' > '+service_name+'.txt'
result=os.popen(kafka_sh).readlines()

# ɸѡ����
all_info='ALL'

# ��ȡkafka�����ļ���Ϣ
f=open(service_name+'.txt')
dict_data=json.load(f)

# service��Ⱥ��Ϣ
service_info=dict_data['alerts_summary']
critical_info=service_info['CRITICAL']
host_info=service_info['OK']
host_count=len(dict_data['alerts'])
print service_name+' ��������������'+str(host_count)

# ��������
sms_list=[]

# service��Ϣ���
if critical_info>-1:
	critical_sms_info=service_name+' ����'+str(critical_info)+'��������ϢCRITICAL��'
	sms_list.append(critical_sms_info)
	print critical_sms_info
	#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()

if host_info<host_count+1:
	host_sms_info=service_name+' ������������'+str(host_info)
	sms_list.append(host_sms_info)
	print host_sms_info
	#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()

# ���Ͷ���
if send_flag:
	for sms_info in sms_list:
		# os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()
		print service_name+' ���ţ�'+sms_info


