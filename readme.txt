����ʱ�䣺2019/10/12 17:35:27

ambari_monitor�����Ŀ
����������
1.���Hbase��Ⱥ�������YARN��Hbase��kafka��flume�ȣ��������Ƿ���ߣ��Ƿ���־�����Ϣ
2.���solr����30����������������������100�������澯
3.��ؼ��10����

�ű�λ�ã�
ssh ocdp@10.218.146.65
ocdp123
/home/ocdp/hyn

����ģ�飺
	������
	������Ϣ���
	�������������������ֹͣ��
	���ŷ���
	���̼��

��Ŀ�ṹ��
	run.py               ����
	service_monitor.py   ��ظ�����񡢾�����Ϣ
	solr_monitor.py      solr���������
	config.py            ���������ļ�
	send_sms.sh          ����֪ͨͨ�ýű�
	api_help             Ambari api�ӿڰ����ĵ�
	log:                 �����־
		