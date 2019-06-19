#!/usr/bin/python
import boto3
import sys
import os 


file = os.environ['FILE_NAME']
upload_dir = '/opt/upload_files/'
filename = upload_dir + file

ACCESS_KEY  = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']


s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)

def s3_upload():
       try:
		s3.meta.client.upload_file(filename, 'prasadtesting', file)
                print file + " Uploaded to S3"
       except:
 		None

def main():
	s3_upload()

if __name__ == '__main__':
	sys.exit(main())
s3_upload.py
