#!/usr/bin/python

from backup_function import Backup

jira = Backup('XXXXXX','/var/log/chef/','/tmp/','chef')
jira.make_backup()
jira.cleanup()
