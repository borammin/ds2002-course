import boto3
import sys
import os

def upload(folder, destination):
    s3 = boto3.client('s3')
    
    bucket = destination.split('/')[0]
    prefix = '/'.join(destination.split('/')[1:])

    for file in os.listdir(folder):
        if file.startswith("results") and file.endswith(".csv"):
            path = os.path.join(folder, file)
            key = f"{prefix}/{file}"
            s3.upload_file(path, bucket, key)
            print(f"Uploaded {file}")

if __name__ == "__main__":
    folder = sys.argv[1]
    destination = sys.argv[2]
    upload(folder, destination)
