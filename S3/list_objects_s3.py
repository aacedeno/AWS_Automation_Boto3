import boto3


s3 = boto3.client('s3')

bucket_name ='acedeno-11082022'

response = s3.list_objects_v2(
    Bucket = bucket_name,
)

contents = response['Contents']

for content in contents:
    print(content['Key'])

