import boto3

s3 = boto3.client('s3')


response = s3.create_bucket(
    ACL='private',
    Bucket='acedeno-11082022',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
   
    )

print(response)