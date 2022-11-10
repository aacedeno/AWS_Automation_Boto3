import boto3

vpc = boto3.client('ec2')

response = vpc.describe_vpcs()


vpcs = response['Vpcs']

#Iterates through the vpcs var and prints the VPC_Id and CIDR Block for every VPC
for vpc in vpcs:
    print(vpc['VpcId'], vpc['CidrBlock'])