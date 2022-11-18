import boto3

function = boto3.client('lambda')
    
response = function.create_event_source_mapping(
    EventSourceArn='arn:aws:sqs:us-east-1:901305956784:Messages',
    FunctionName='SQS-Lambda-SNS',
    Enabled=True #Activates the event source mapping
    )
    
#Prints the state of the event source mapping and the identifier
print(response['State'], response['UUID'])
    
    
    
    
    
    
    
    
   