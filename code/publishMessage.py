import json
import boto3
import os

sns = boto3.client('sns')
ses = boto3.client('ses')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['tableName'])


def lambda_handler(event, context):
    body = json.loads(event['body'])
    print(body)
    response = sns.publish(
        Message=body['message'],
        PhoneNumber=body['user_friend_phone']
    )
    response = ses.send_email(
        Source='solonsef@gmail.com',  # hardcoded...will be woof email
        Destination={'ToAddresses': [body['user_friend_email']]},
        Message={
            'Subject': {'Data': "WOOF"},
            'Body': {'Text': {'Data': body['message']}}
        }
    )
    response = table.put_item(
        Item={
            "user_email": body['user_email'],
            "user_friend_name": body['user_friend_name'],
            "timestamp": body['timestamp'],
            "message": body['message']
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Message published and saved"
            }
        ),
    }
