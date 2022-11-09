import boto3

s3 = boto3.client('s3')

#Parsing the Bucket key name from list_bucket method
create_date = s3.list_buckets()["Buckets"]

for bucket in create_date:
    print(bucket["Name"])
    print(bucket["CreationDate"])create_date = s3.list_buckets()["Buckets"]
