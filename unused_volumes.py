import boto3
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')
volumes = ec2_client.describe_volumes()
sns_arn = "arn:aws:sns:eu-west-2:245182714656:unused-volume"
unused_vol = []
for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0:
        #### if there is no attachments to the  volume add to the list #####
        unused_vol.append(volume['VolumeId'])
        print(volume)
        print("____"*5)

email_body = "### unused volumes ####\n"


for vol in unused_vol:
    email_body = email_body + "VolumeId = {} \n".format(vol)

    ### send email ####
    sns_client.publish(
        TopicArn = sns_arn,
        Subject = "Unused Volumes",
        Message = email_body
    )


    print(email_body)

