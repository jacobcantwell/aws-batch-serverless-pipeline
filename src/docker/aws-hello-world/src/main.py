import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
# table = dynamodb.Table('helloWorld')
# print(table.creation_date_time)

print("Hello world")
