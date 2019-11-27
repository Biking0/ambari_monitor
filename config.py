#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# �ļ����ƣ�config.py
# ����������ambari�����Ŀ�����ļ�
# �� �� ��
# �� �� ��
# �� �� �ߣ�
# �������ڣ�
# �޸���־��
# �޸����ڣ�
# ***************************************************************************
# ������ø�ʽ��python config.py
# ***************************************************************************

# hbase��Ⱥ��ַ
hbase_url='http://10.218.146.65:8080/api/v1/clusters'

# hbase��Ⱥ����
hbase_name='hbasecluster'

# ���ڼ�Ⱥ��ַ
sanqi_url='http://10.93.171.97:8080/api/v1/clusters'

# ���ڼ�Ⱥ����
sanqi_name='hnydcluster'

# ���Ŀ���ַ
monitor_url=hbase_url
monitor_name=hbase_name

# ��������ط���
liu_service_list=['FLUME','KAFKA']

# Ŀǰ��ط���
service_list=['AMBARI_INFRA','FLUME','HBASE','KAFKA','MAPREDUCE2','PIG','RANGER','SLIDER','SPARK','TEZ','YARN','ZOOKEEPER','HDFS']

# ȫ������
all_service_list=['AMBARI_INFRA','AMBARI_METRICS','FLUME','HBASE','HDFS','HIVE','KAFKA','MAPREDUCE2','PIG','RANGER','SLIDER','SPARK','TEZ','YARN','ZOOKEEPER']

# �޷���ط���ambariҳ������쳣
error_service_list=['AMBARI_METRICS','HDFS','HIVE']

# ���Ź���
#all_info='ALL'

# ���Ź��˲���
all_info='HYN'

# ����֪ͨ���أ��Ƿ��Ͷ��ţ����Ͷ�����Ҫ��ΪTrue������ΪFalse
send_flag=True

# solr���ſ���
solr_send_falg=True

# ��־�ļ�·��
log_path='log/'

# solrĬ�ϲ�ѯ�idactivity_num
default_activity_num = '10415'

# ��ѯ����30����
search_time=1800

# solr����������ֵ
solr_data_num=100

# ��ؼ��
sleep_time=600

################ ���������ƣ�������־��ӡ ################
service_monitor = 'service_monitor'
solr_monitor = 'solr_monitor'
kafka_monitor = 'kafka_monitor'

############## �����ؿ��أ���ͣ��ָ����س��� ############
service_monitor_flag = True
solr_monitor_flag = True
kafka_monitor_flag = True


###### ��ؿ��� #######
# 1. ��ظ������
# 2. ���solr
# 3. 
# 4. ���kafka����
# 5. ���kafka��־���м��
		
		# 
		
		

