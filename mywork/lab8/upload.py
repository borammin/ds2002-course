import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-tsc9rv'
file_name = 'cloud.jpg'

s3.upload_file(file_name, bucket, file_name)

s3.upload_file(file_name, bucket, file_name, ExtraArgs={'ACL': 'public-read'})
