import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event,context):
   filter = [
     {
         'Name': 'tag: Type',
         'Values': ['Scheduled']
},
]

 instances = ec2.instances.filter(Filters=filter)
 for instance in instances:
   instance.start()
