""" Item class """

import datetime

class Item(object):
    
    def __init__(self):
        pass
    
    def getMetadata(self):
        
        # generate the 
        d = datetime.datetime.now()
        _time = "{}{}{}-{}:{}:{}".format(d.year, d.month, d.day, d.hour, d.minute, d.second)     
        
        return _time