#!/usr/bin/env python
# -*-coding:utf-8 -*-
# *******************************************************************************
# �ļ����ƣ�send_sms.sh
# ������������ض��ŷ���ͨ�ýű������ڽű��ڲ����øýű�
# ����������������ݣ����˲���
# �� �� ��
# �� �� �ߣ�hyn
# �������ڣ�20191010
# �޸���־��
# �޸����ڣ�
# *******************************************************************************
# ������ø�ʽ��sh send_sms.sh sms_info ALL
# *******************************************************************************

# �ò���Ĭ�ϷŶ��ŷ������ݣ�Ҳ�ɷŷ�������Ϣ
sms_info=$1
# �����û�����
all_info=$2

# ���ݿ��¼����
exec_mysql_ng="mysql -h10.97.192.180 -ungtassuite -pAj7y32h! ngtassuite"

# ���Ͷ��ţ������������Ϣ
${exec_mysql_ng} -e "INSERT INTO tb_sys_sms_send_cur(serv_number, send_date,text,opt_user,opt_date ) SELECT serv_number, now(), '$sms_info', opt_user, now() FROM tb_sys_sms_phone WHERE opt_user = 'ocetl' and sms_id = '$all_info';" 2>/dev/null