#!/usr/bin/python
import boto.ec2
from datetime import datetime

conn = boto.ec2.connect_to_region("ap-southeast-1")

#HardCoded SVN Instance id here
instance_id = 'XXXXX'

volumes = conn.get_all_volumes(filters={'attachment.instance-id': instance_id})
description = instance_id + "  " + datetime.today().isoformat(' ')

# This will take only the snapshot of the 1st Data drive , where SVN is configured
snap = [v.create_snapshot(description+'v') for v in volumes[1:][:-1]]
