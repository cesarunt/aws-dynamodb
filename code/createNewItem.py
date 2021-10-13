import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('users')
# print(table.creation_date_time)

response = table.put_item(
   Item={
        'dni'       : '32423423',
        'user_name' : 'janedoe',
        'first_name': 'Jane',
        'last_name' : 'Doe',
        'user_age'  : 25
    }
)

print(response)