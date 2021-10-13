""" DynameDb class """

import boto3
from setting.config import cfg

class DynamoDb(object):
    
    def __init__(self, Table_Name = cfg.GLOBAL.TABLE):
        # self.Table_Name  = Table_Name
        self.db          = boto3.resource('dynamodb')
        self.table       = self.db.Table(Table_Name)
        self.client      = boto3.client('dynamodb')

    # FUNCTION TO GET SELECT ITEM FROM DYNAMODB
    def get(self, _item):
        result = None
        response = self.table.get_item(
            Key={
                'dni'      : _item['dni'],
                'user_name': _item['user_name']
            }
        )
        try:
            result = response['Item']
        except Exception as e:
            result = None
        return result

    # FUNCTION TO INSERT NEW ITEM ON DYNAMODB
    def put(self, _item, _date=''):
        result = None
        response = self.table.put_item(
            Item={
                'dni'             : _item['dni'],
                'user_name'       : _item['user_name'],
                'first_name'      : _item['first_name'],
                'last_name'       : _item['last_name'],
                'user_age'        : _item['user_age'],
                'user_date_create': _date,
                'user_date_update': ''
            }
        )
        if response != None :
            result = _item
        return result
    
    # FUNCTION TO UPDATE NEW ITEM ON DYNAMODB
    def upd(self, _item, _date=''):
        result = None
        response = self.table.update_item(
            Key={
                'dni'      : _item['dni'],
                'user_name': _item['user_name']
            },
            UpdateExpression='SET first_name = :val0, last_name = :val1, user_age = :val2, user_date_update = :val3',
            ExpressionAttributeValues={
                ':val0': _item['first_name'], ':val1': _item['last_name'], ':val2': _item['user_age'], ':val3': _date
            }
        )
        if response != None :
            result = _item
        return result