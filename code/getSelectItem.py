import boto3
import sys

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('users')

# get Item
response = table.get_item(
    Key={
        'dni'       : '324234234',
        'user_name'  : 'cesarunt'
    }
)

print('Response: ', response)

try:
    item = response['Item']
except Exception as e:
    item = "Item no encontrado"

print(item, flush=False)
sys.stdout.write("This is my string")
sys.stdout.flush()