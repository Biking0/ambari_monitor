#!/usr/bin/env python
# -*-coding:utf-8 -*-
# *******************************************************************************
# 文件名称：service_monitor.py
# 功能描述：各类服务通用监控
# 输 入 表： 
# 输 出 表： 
# 创 建 者：hyn
# 创建日期：20191010
# 修改日志：
# 修改日期：
# *******************************************************************************
# 程序调用格式：python service_monitor.py
# *******************************************************************************

import os
import sys
import json
import time
import config

# 方法结构设计:
# 1.初始化
# 2.网络请求
# 3.短信内容编辑
# 4.发送短信

class ServiceMonitor():
	
	# 初始化
	def __init__(self):
		
		# 短信内容
		self.sms_list=[]
		
	# 网络请求
	def request_data(self):
		
		# 循环请求多个服务
		for service_name in config.service_list:
		
			# 请求服务状态数据输出到本地txt文件
			exec_sh = 'curl -u admin:admin '+config.monitor_url+'/'+config.monitor_name+'/services/'+service_name+' > '+config.log_path+config.service_monitor+'.txt'
			# print 'exec_sh: '+exec_sh
			result_data = os.popen(exec_sh).readlines()
			
			try:
			
				self.sms_info(service_name,result_data)
			except Exception as e:
				print '# monitor '+service_name +'error,next'
				print e
				continue
	
	# 短信内容编辑
	def sms_info(self,service_name,result_data):
	
		# 读取kafka本地文件信息
		f=open(config.log_path+config.service_monitor+'.txt')
		dict_data=json.load(f)

		# service集群信息
		service_info=dict_data['alerts_summary']
		critical_info=service_info['CRITICAL']
		host_info=service_info['OK']
		host_count=len(dict_data['alerts'])
		if service_name=='HDFS':
			host_count=host_count-30
			
		print service_name+'服务总主机数：'+str(host_count)
		
		# 服务警告信息
		
		# HDFS警告需要特殊处理
		
		if service_name=='HDFS':
			#if critical_info>-1:
			
			if critical_info>5:
				critical_sms_info=service_name+'出现'+str(critical_info)+'条警告信息CRITICAL！'
				self.sms_list.append(critical_sms_info)
				print critical_sms_info
				
			
			# 正常主机监控
			#if host_info<host_count+1:
			if host_info<host_count:
				host_sms_info=service_name+'正常主机数（总主机数'+str(host_count)+'）：'+str(host_info)
				self.sms_list.append(host_sms_info)
				print host_sms_info
			
			
		else:
			
			#if critical_info>-1:
			if critical_info>0:
				critical_sms_info=service_name+'出现'+str(critical_info)+'条警告信息CRITICAL！'
				self.sms_list.append(critical_sms_info)
				print critical_sms_info
				
			
			# 正常主机监控
			#if host_info<host_count+1:
			if host_info<host_count:
				host_sms_info=service_name+'正常主机数（总主机数'+str(host_count)+'）：'+str(host_info)
				self.sms_list.append(host_sms_info)
				print host_sms_info
		
		# 发送短信s
		if config.send_flag:
			self.send_sms(service_name)
	
	# 发送短信
	def send_sms(self,service_name):
		
		for sms_info in self.sms_list:
			
			# 发送短信
			os.popen('sh send_sms.sh'+' '+sms_info+' '+config.all_info+' >> '+config.log_path+'service_monitor.log').readlines()
			
			# 将短信内容写入日志
			os.popen('echo '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' '+sms_info+' >> '+config.log_path+'service_monitor.log').readlines()
			
			print service_name+' 短信：'+sms_info
		
		self.sms_list=[]

# 启动测试
#if __name__=='__main__':
#	sm = ServiceMonitor()
#	
#	while True:
#		sm.request_data()
#		time.sleep(config.sleep_time)
#	
#	
