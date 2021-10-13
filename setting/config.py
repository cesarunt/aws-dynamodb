""" Developing the initial configuration of this application """

import os
from easydict import EasyDict as edict

__C = edict()
cfg = __C

__C.GLOBAL = edict()

# development environment:      dev / prod
__C.GLOBAL.ENV = 'dev'

# set the table's name on aws
__C.GLOBAL.TABLE = 'users'

# set the region's name on aws
__C.GLOBAL.REGION = 'us-west-2'

# set the information for new item (person)
_item = {
        'dni'        :   '41456859',
        'user_name'  :   'cesarunt',
        'first_name' :   'Cesar Deyvi',
        'last_name'  :   'Peña Anticona',
        'user_age'   :   '40'
        }
__C.GLOBAL.ITEM = _item