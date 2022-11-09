import boto3


#Can reference boto3 with a client or a resource
#Do not assume the service name is what it is actually called (For VPCs you pass ec2 as the services)
#Naming the client and assigning it to s3 var
s3 = boto3.client('s3')

#Storing the output from list buckets in the response variable
response = s3.list_buckets()

#Parse the info from response variable, data from response variable comes back as a dict and the key name "Buckets" is used 
buckets = response["Buckets"]

#iterate through the buckets; buckets is a list 
for bucket in buckets:
    print(bucket["Name"])