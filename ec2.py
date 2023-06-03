import boto3
import csv

AWS_REGION = "us-east-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

instances = EC2_RESOURCE.instances.all()
file=open('ec2_instance_new.csv','w',newline='')
data_obj=csv.writer(file)
data_obj.writerow(['s.no','Instance.id', 'PublicIp', 'PrivateIp'])
for instance in instances:
    print('EC2 instance:', {instance.id})
    print('Public IPv4 address:',{instance.public_ip_address})
    print('private IPv4 address:', {instance.public_ip_address})
    data_obj.writerow([instance.id,instance.public_ip_address,instance.public_ip_address])

file.close()