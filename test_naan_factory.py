#Import naan factory functions
# define and run the tests


from naan_factory_functions import *

#1
#As a user, I can use the make_dough with water and flour to make dough.

print("Calling make_dough with water and flour, expect 'dough as a result")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))
#
#
# #2
# #As a user, I can use the bake_dough with dough to get naan.
#
print("Calling bake_dough with dough, expect 'naan' as a result")
print(bake_dough('dough') == 'naan')
print('got:', bake_dough('dough'))
#
# #3
# #As a user, I can user the run_factory with water and flour and get naan.
print("Calling run_factory with water and flour, expect 'naan' as a result")
print(run_factory('water', 'flour') == 'naan')
print('got:', run_factory('water', 'flour'))


