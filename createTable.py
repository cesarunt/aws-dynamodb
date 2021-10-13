import boto3
from setting.config import cfg

nameDB = cfg.GLOBAL.TABLE
region = cfg.GLOBAL.REGION
table  = None

def createTable(dynamodb):

    table = dynamodb.create_table(
        TableName = nameDB,
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

    print('Creating Table ...')
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=nameDB)

    return table

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name=region)
# Get the client
client = boto3.client('dynamodb', region_name=region)

table = createTable(dynamodb)
# print(table.item_count)

if table :
    print("The table "+str(nameDB).upper()+" has been created successfully")
