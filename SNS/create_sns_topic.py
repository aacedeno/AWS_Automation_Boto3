import boto3

sns = boto3.resource('sns')

#Creating SNS topic
topic = sns.create_topic(
    Name='sns_testing')
    
#Prints the ARN 
print(topic)