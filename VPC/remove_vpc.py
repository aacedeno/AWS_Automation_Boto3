import boto3

vpc = boto3.client('ec2')

#The VPC you want to delete must detach or delete all gateways and resources that are associated with the VPC before you can delete it.
vpc_id = 'vpc-00537d542cbdea877'

response = vpc.delete_vpc(
    VpcId= vpc_id,
)

#Printing the response to see what the HTTPStatusCode is. If it displays 200 that means the code was succesful
print(response)

