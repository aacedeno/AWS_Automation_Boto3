import boto3


ec2 = boto3.client('ec2')

#If you want to create multiple instances, increase the MaxCount
response = ec2.run_instances(
    ImageId='ami-09d3b3274b6c5d4aa',
    InstanceType='t2.micro',
    MaxCount=3,
    #Keypair = 'xxxx'
    MinCount=1,
    SubnetId='subnet-08ce052f60b1f875f',
)