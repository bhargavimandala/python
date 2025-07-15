import boto3
import os

sns_client = boto3.client('sns')
ec2_client = boto3.client('ec2')

# Environment variables (configured in Lambda console)
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
INSTANCE_ID = os.environ['INSTANCE_ID']  # Optional hard-coding

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    state = event['detail']['state']

    if state == 'stopped':
        # Get tags (for context)
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]
        tags = instance.get('Tags', [])
        tag_dict = {tag['Key']: tag['Value'] for tag in tags}
        env = tag_dict.get("Environment", "Unknown")

        # Only notify if in production
        if env.lower() == "production":
            message = f"""
Instance ID: {instance_id}
Environment: {env}
Current State: {state}
Tags: {tag_dict}
"""
            # Publish to SNS
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="Production EC2 Instance Stopped",
                Message=message
            )
            print("SNS notification sent.")
        else:
            print(f"Instance {instance_id} stopped but not in production. No alert sent.")
