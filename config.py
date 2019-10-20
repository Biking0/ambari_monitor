#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：config.py
# 功能描述：ambari监控项目配置文件
# 输 入 表：
# 输 出 表：
# 创 建 者：
# 创建日期：
# 修改日志：
# 修改日期：
# ***************************************************************************
# 程序调用格式：python config.py
# ***************************************************************************

# 目前测试监控habse集群

# hbase集群地址
hbase_url='http://10.218.146.65:8080/api/v1/clusters'

# hbase集群名字
hbase_name='hbasecluster'

# 三期集群地址
sanqi_url='http://10.93.171.97:8080/api/v1/clusters'

# 三期集群名字
sanqi_name='hnydcluster'

# 流处理相关服务
liu_service_list=['FLUME','KAFKA']

# 目前监控服务
service_list=['AMBARI_INFRA','FLUME','HBASE','KAFKA','MAPREDUCE2','PIG','RANGER','SLIDER','SPARK','TEZ','YARN','ZOOKEEPER']

# 全部服务
all_service_list=['AMBARI_INFRA','AMBARI_METRICS','FLUME','HBASE','HDFS','HIVE','KAFKA','MAPREDUCE2','PIG','RANGER','SLIDER','SPARK','TEZ','YARN','ZOOKEEPER']

# 无法监控服务，ambari页面参数异常
error_service_list=['AMBARI_METRICS','HDFS','HIVE']

# 短信过滤
all_info='ALL'

# 短信通知开关，是否发送短信，发送短信需要置为True，否则为False
send_flag=True

# solr短信开关
solr_send_falg=True

# 日志文件路径
log_path='log/'

# solr默认查询活动idactivity_num
default_activity_num = '10415'

# 查询最新30分钟
search_time=1800

# solr数据量警告值
solr_data_num=100

# 监控间隔
sleep_time=600

################ 程序监控名称，用于日志打印 ################
service_monitor = 'service_monitor'
solr_monitor = 'solr_monitor'
kafka_monitor = 'kafka_monitor'

############## 程序监控开关，可停用指定监控程序 ############
service_monitor_flag = True
solr_monitor_flag = True
kafka_monitor_flag = True


###### 监控开关 #######
# 1. 监控各类服务
# 2. 监控solr
# 3. 
# 4. 监控kafka消费
# 5. 监控kafka日志，有监控
		
		# 
		
		


