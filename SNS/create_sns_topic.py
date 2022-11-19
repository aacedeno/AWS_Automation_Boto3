import boto3

sns = boto3.client('sns')

#Creating SNS topic
response = sns.create_topic(
    Name='sns_testing')
    
topic = response['TopicArn']
    
#Prints the ARN 
print(topic)