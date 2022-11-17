import boto3


sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='Ryan-is-cool'
    )

q_url = sqs.get_queue_url(
    QueueName = 'Ryan-is-cool'
    )
    
print(q_url['QueueUrl'])