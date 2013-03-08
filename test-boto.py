#!/usr/bin/python
import boto.ec2.connection
from boto.ec2.regioninfo import RegionInfo
import clouds.openstack

#e59c100351844ab785ca5133905ec184
#AWS_SECRET_ACCESS_KEY=54f80f17fd4140f8b24b36906453195d

connection = clouds.openstack.EC2Connection(
    aws_access_key_id='e59c100351844ab785ca5133905ec184',
    aws_secret_access_key='54f80f17fd4140f8b24b36906453195d',
    port=8773,
    region = RegionInfo(endpoint='tascloud.it.csiro.au'),
    path = '/services/Cloud',
    is_secure=False)



sgs = connection.get_all_security_groups(filters={'group-name':'_sc-*'})
print sgs

for sg in sgs:
    sg.add_tag('sg','sg')


res = connection.get_all_instances()
for r in res:
    print r.groups
    for i in r.instances:
        print i
        print i.groups
        for g in i.groups:
            print g.name
            print g.id
        print i.id
        i.add_tag('test','test')
