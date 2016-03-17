#!/usr/bin/python
import tinys3,datetime,os,glob,zipfile,sys

today = datetime.date.today()
S3_ACCESS_KEY = 'XXXXXXXXXXXXXXXX'
S3_SECRET_KEY = 'XXXXXXXXXXXXXXX'

class Backup():

    def __init__(self,my_bucket,source,destination,application):
        self.my_bucket = my_bucket
        self.source    = source
        self.destination = destination
        self.application = application

    def make_backup(self):
        file_name = zipfile.ZipFile(self.destination + str(today) + ".zip", "w")
        for name in glob.glob(self.source + "*"):
            file_name.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
        file_name.close()
        conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY)
        f = open(self.destination + str(today) + ".zip",'rb')
        conn.upload(self.application + "-" + str(today) + ".zip" ,f,self.my_bucket)

    def cleanup(self):
        os.remove(self.destination + str(today) + ".zip")
