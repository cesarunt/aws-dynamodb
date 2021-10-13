import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
# Get the client
client = boto3.client('dynamodb', region_name='us-west-2')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'dni',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'user_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'dni',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'user_name',
            'AttributeType': 'S'
        }
    ],
    
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print('Creating Table...')

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)