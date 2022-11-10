import boto3


vpc = boto3.client('ec2')

response = vpc.create_vpc(
        CidrBlock='10.10.0.0/16'
    )

