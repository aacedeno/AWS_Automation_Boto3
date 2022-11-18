import boto3


sns = boto3.client('sns')

#Subscribing to SNS topic 
response = sns.subscribe(
    TopicArn='arn:aws:sns:us-east-1:901305956784:sns_testing',
    Protocol='email',
    Endpoint='aacedeno1@gmail.com',
    #Need this attribute so the ARN of the subscription prints, if we don't add this it'll 
    #show the status of the subscription which will most likely be 'pending confirmation'
    ReturnSubscriptionArn = True 

    )
#This give us the ARN of the topic and the ARN of the subscription
print(response['SubscriptionArn'])