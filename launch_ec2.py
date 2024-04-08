### Launching an ec2 instance using boto3 ###
import boto3
import os

os.environ['AWS_PROFILE'] = "DevOps"
client = boto3.client('ec2', region_name='eu-west-2')
response = client.run_instances(ImageId='ami-004961349a19d7a8f',InstanceType='t2.micro',MaxCount=1,MinCount=1)

for i in response['Instances']:
    print(i['InstanceId'])    
