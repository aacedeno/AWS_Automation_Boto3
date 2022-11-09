import boto3

#Can refer to any s3 inside our Amazon account using the s3 var
s3 = boto3.client('s3')

#upload_file(Filename, Bucket, Key, ExtraArgs=None, Callback=None, Config=None)¶
#I am using Cloud9 on AWS so in order to upload something to S3 I had to upload the file to the EC2 machine and refernece the file below
s3.upload_file(
    Filename='/home/ec2-user/environment/AWS_Automation_Boto3/HTML-Codecademy.pdf', 
    Bucket='acedeno-11082022', 
    Key='html.pdf'
    )