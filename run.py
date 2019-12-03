#!/usr/bin/env python
# -*-coding:utf-8 -*-
#********************************************************************************
# ** 文件名称：run.py
# ** 功能描述：ambari 监控项目启动所有监控程序
# ** 输 入 表：
# ** 输 出 表：
# ** 创 建 者：hyn
# ** 创建日期：20191020
# ** 修改日志：
# ** 修改日期：
# *******************************************************************************
# ** 程序调用格式：nohup python run.py >> nohup.out &
# *******************************************************************************

import os
import time
import config
import service_monitor
import solr_monitor

# 启动
if __name__=='__main__':
	
	while True:
	
		# 1.监控各类服务
		service_monitor_object = service_monitor.ServiceMonitor()
		service_monitor_object.request_data()
		
		# 2.监控solr
		solr_monitor_object = solr_monitor.SolrMonitor()
		solr_monitor_object.request_data()
		
		# 3.监控kafka消费
		
		# 4.监控kafka日志，有监控
		
		print('sleep 900s')
		time.sleep(config.sleep_time)
		
		#time.sleep(3)

