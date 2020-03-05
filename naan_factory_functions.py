# Functions Here

from run_naan_factory import *


# if argument is water and argument 2 is flour
# return dough
# else return
# not dough

def make_dough(arg1, arg2) :
    if arg1 == 'water' and arg2 == 'flour':
        return 'dough'
    else:
        'not dough'


def bake_dough(arg1) :
    if arg1 == 'dough':
        return 'naan'
    else:
        'not naan'


def run_factory(arg1, arg2) :
    if arg1 == 'water' and arg2 == 'flour':
        return 'naan'
    else:
        'not naan'

