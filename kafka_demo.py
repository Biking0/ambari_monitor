##!/usr/bin/env python
## -*-coding:utf-8 -*-
##********************************************************************************
## **  �ļ����ƣ�kafka_demo.py
## **  ����������kafka������demo
## **  �� �� �� 
## **  �� �� �� 
## **  �� �� �ߣ�hyn
## **  �������ڣ�20191010
## **  �޸���־��
## **  �޸����ڣ�
## *******************************************************************************
## **  ������ø�ʽ��python kafka_demo.py
## *******************************************************************************

import os
import json

# �Ƿ��Ͷ��ţ����Ͷ�����Ҫ��ΪTrue
send_flag=True

# ����kafka״̬���������kafka.txt
kafka_sh='curl -u admin:admin http://10.218.146.65:8080/api/v1/clusters/hbasecluster/services/KAFKA > kafka.txt'
result=os.popen(kafka_sh).readlines()

# ɸѡ����
all_info='ALL'

# ��ȡkafka�����ļ���Ϣ
f=open('kafka.txt')
dict_data=json.load(f)

# kafka��Ⱥ��Ϣ
kafka_info=dict_data['alerts_summary']
critical_info=kafka_info['CRITICAL']
host_info=kafka_info['OK']

# ��������
sms_list=[]

# kafka��Ϣ���
if critical_info>-1:
	critical_sms_info='kafka ����'+str(critical_info)+'��������ϢCRITICAL��'
	sms_list.append(critical_sms_info)
	print 'kafka ����'+str(critical_info)+'��������ϢCRITICAL��'
	#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()

if host_info<8:
	host_sms_info='kafka ������������'+str(host_info)
	sms_list.append(host_sms_info)
	print 'kafka ������������'+str(host_info)
	#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()

# ���Ͷ���
if send_flag:
	for sms_info in sms_list:
		#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()
		print 'kafka ���ţ�'+sms_info


