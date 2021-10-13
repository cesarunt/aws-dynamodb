"""
Test Cheetrack,
Registro de datos genéricos, Registro de Personas (datos principales y metadatos)
"""

try:
    import os
    import sys
    import boto3
except Exception as e:
    print("Faltan algunos módulos")

from classes.singleton import Metaclass
from classes.dynamodb import DynamoDb
from classes.item import Item
from setting.config import cfg
import utils.print as uprint


class AWS_DYNAMODB(metaclass=Metaclass):

    def __init__(self):
        self._database = DynamoDb()
        self._item     = Item()
    
    def select(self, _item):
        _result = self._database.get(_item)
        if _result == None :
            print("\nItem not found")
        else:
            print("\nItem found\n" + str(_result))
        return _result
    
    def register(self, _item):
        _time    = self._item.getMetadata()
        _result  = self._database.put(_item, _time)
        print("\nItem saved\n" + str(_result))

    def update(self, _item):
        _date   = self._item.getMetadata()
        _result = self._database.upd(_item, _date)
        print("\nItem updated\n" + str(_result))


def main():

    _user = None
    _item = cfg.GLOBAL.ITEM 
    
    aws = AWS_DYNAMODB()

    # INSERT OR UPDATE
    _user = aws.select(_item)
    
    if _user :
        aws.update(_item)
    else:
        aws.register(_item)


if __name__ == "__main__" :
    
    if cfg.GLOBAL.ENV == 'dev' :
        uprint.enablePrint()
    else:
        print("Important:\nIn prod environment, the print functions are disabled")
        uprint.disablePrint()
    
    main()