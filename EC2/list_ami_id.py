import boto3

#naming our client ec2 
ec2 = boto3.client('ec2')

response = ec2.describe_instances()

#Parsing the output from response var
reservations = response['Reservations']

#This iteration assigns the Dict key 'Instance' to instances var
for reservation in reservations:
    instances = reservation['Instances']
    #This iteration print the Image Id and Instance Id for every instance in instances list
    for instance in instances:
        print(instance['ImageId'], instance['InstanceId'])
    


