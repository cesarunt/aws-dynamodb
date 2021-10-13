"""
Test Cheetrack,
Registro de datos genéricos, Registro de Personas (datos principales y metadatos)
"""

try:
    import boto3
    import datetime
except Exception as e:
    print("Faltan algunos módulos")

""" Implementando el patrón Singleton """
class Metaclass(type):
    _instance = {}
    
    def __call__(cls, *args, **kwargs): 
        if cls not in cls._instance:
            cls._instance[cls] = super(Metaclass, cls).__call__(*args, **kwargs) 
            return cls._instance[cls]

class Person(object):
    
    def __init__(self):
        pass
    
    def getMetadata(self):
        # generate the 
        d = datetime.datetime.now()
        _time = "{}{}{}-{}:{}:{}".format(d.year, d.month, d.day, d.hour, d.minute, d.second)     
        return _time

class DynamoDb(object):
    
    def __init__(self, Table_Name='users'): 
        self.Table_Name  = Table_Name
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

class AWS_DYNAMODB(metaclass=Metaclass):

    def __init__(self):
        self._database = DynamoDb()
        self._item     = Person()
    
    def select(self, _item):
        _result = self._database.get(_item)
        if _result == None :
            print("\nItem not found")
        else:
            print("\nItem found\n" + str(_result))
        return _result
    
    def register(self, _item):
        # getting metadata from Person
        _time    = self._item.getMetadata()
        _result  = self._database.put(_item, _time)
        print("\nItem saved\n" + str(_result))

    def update(self, _item):
        # getting metadata from Person
        _date   = self._item.getMetadata()
        _result = self._database.upd(_item, _date)
        print("\nItem updated\n" + str(_result))

def main():
    user = None

    _item = {
            'dni'        :   '41456859',
            'user_name'  :   'cesarunt',
            'first_name' :   'Cesar D.',
            'last_name'  :   'Peña Anticona',
            'user_age'   :   '33'
            }
    
    item = AWS_DYNAMODB()

    # INSERT OR UPDATE
    user = item.select(_item)
    if user != None :
        item.update(_item)
    else:
        item.register(_item)

if __name__ == "__main__" :
    main()