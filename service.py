##!/usr/bin/env python
## -*-coding:utf-8 -*-
##********************************************************************************
## **  文件名称：service_monitor.py
## **  功能描述：各类服务通用监控
## **  输 入 表： 
## **  输 出 表： 
## **  创 建 者：hyn
## **  创建日期：20191010
## **  修改日志：
## **  修改日期：
## *******************************************************************************
## **  程序调用格式：python service_monitor.py
## *******************************************************************************

import os
import sys
import json
import time
import config

# 方法结构设计:
# 		初始化
# 		网络请求
# 		短信内容编辑
# 		发送短信

class ServiceMonitor():
	
	# 初始化
	def __init__(self):
		print 'init'
		
		# 是否发送短信，发送短信需要置为True
		self.send_flag=True
		# 筛选条件
		self.all_info='ALL'		
		# 短信内容
		self.sms_list=[]
		
		
	# 网络请求
	def request_data(self):
		
		print 'requestData'
		
		# 循环请求多个服务
		for service_name in config.liu_service_list:
		
			# 请求服务状态数据输出到本地txt文件
			exec_sh = 'curl -u admin:admin '+config.hbase_url+'/'+config.hbase_name+'/services/'+service_name+' > '+service_name+'.txt'
			print 'exec_sh: '+exec_sh
			result_data = os.popen(exec_sh).readlines()
			
			self.sms_info(service_name,result_data)					
	
	# 短信内容编辑
	def sms_info(self,service_name,result_data):
		print 'sms_info'
		
		# 读取kafka本地文件信息
		f=open(service_name+'.txt')
		dict_data=json.load(f)

		# service集群信息
		service_info=dict_data['alerts_summary']
		critical_info=service_info['CRITICAL']
		host_info=service_info['OK']
		host_count=len(dict_data['alerts'])
		print service_name+' 服务总主机数：'+str(host_count)		
		
		# 服务警告信息
		#if critical_info>-1:
		if critical_info>0:
			critical_sms_info=service_name+' 出现'+str(critical_info)+'条警告信息CRITICAL！'
			self.sms_list.append(critical_sms_info)
			print critical_sms_info
			#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()
		
		# 正常主机监控
		#if host_info<host_count+1:
		if host_info<host_count:
			host_sms_info=service_name+' 正常主机数（总主机数'+str(host_info)+'）：'+str(host_info)
			self.sms_list.append(host_sms_info)
			print host_sms_info
			#os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info).readlines()
		
		# 发送短信
		if self.send_flag:
			self.send_sms(service_name)
	
	# 发送短信
	def send_sms(self,service_name):
		
		for sms_info in self.sms_list:
			os.popen('sh send_sms.sh'+' '+sms_info+' '+all_info+' >> service_monitor.log').readlines()
			
			# 将短信内容写入日志
			os.popen('echo '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' '+sms_info+' >> service_monitor.log').readlines()
			
			print service_name+' 短信：'+sms_info
		
		self.sms_list=[]

# 启动
if __name__=='__main__':
	sm = ServiceMonitor()
	
	while True:
		sm.request_data()
		time.sleep(1800)
	
	
