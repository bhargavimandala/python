import boto3
ec2_client = boto3.client('ec2')
instances = ec2_client.describe_instances()
used_amis = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])
        
print(used_amis)

## remove duplicate amis
def remove_duplicates(amis):
    unique_amis = []
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)
        return unique_amis
unique_amis = remove_duplicates(used_amis)
print(unique_amis)

##### get custom amis from the account
custom_images = ec2_client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': [
                'available',
            ]
        },
    ],
    Owners = ['self']
)

custom_amis_list = []
for image in custom_images['Images']:
    custom_amis_list.append(image['ImageId'])

for custom_ami in custom_amis_list:
    if custom_ami not in used_amis:
        print("deregistering ami{}".format(custom_ami))
        ec2_client.deregister_image(ImageId=image['ImageId'])