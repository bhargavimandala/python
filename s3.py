import boto3
import os

os.environ['AWS_PROFILE'] = "DevOps"

client = boto3.client('s3', region_name='eu-west-2')

response = client.create_bucket(
        Bucket='s3-bucket-boto3-mb',
    
)

print(response)