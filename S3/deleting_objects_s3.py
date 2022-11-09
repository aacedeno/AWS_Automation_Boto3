import boto3

s3 = boto3.client('s3')

bucket_name = 'acedeno-11082022'

#Deletes a single object in a bucket
response = s3.delete_objects(
    Bucket= bucket_name,
    Delete={
        'Objects': [
            {
                'Key': 'primes.txt',
            },
        ],
    
    },
   
)

