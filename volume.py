import boto3
import csv
from pprint import pprint
ec2_cli=boto3.client(service_name='ec2')
collect_all_regions=[]
for each_region in ec2_cli.describe_regions()['Regions']:
    collect_all_regions.append(each_region['RegionName'])
print(collect_all_regions)
fo=open('ec2_inven_new.csv','w',newline='')
data_obj=csv.writer(fo)
data_obj.writerow(['S.no','VolumesId','VolumeType','VolumeSize'])

cnt=1
for each_region in collect_all_regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_region)
    for each_ins_in_reg in ec2_re.instances.all():
        data_obj.writerow([cnt,each_ins_in_reg.Volume_id,each_ins_in_reg.Volume_Type,each_ins_in_reg.Volume_size])
        cnt+=1
fo.close()