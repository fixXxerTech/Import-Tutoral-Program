import sec_layer.funcs as funcs
import sys

for i in sys.path:
	print (i)
import sec_layer.vars as vars
import sec_layer.ter_layer.funcs_ter as ter_funcs
import sec_layer.ter_layer.vars_ter as ter_vars
from time import sleep



funcs.sec_layer_display()
sleep(0.8)
print(funcs.sec_show)
funcs.do_ter()
print ('\nfuncs has done ter_layer succesfully..\n')
sleep(1.2)
print ('\n\n')
print ('sec_layer[funcs] completed..')


print ('\n\n')
vars.sec_layer_display()
sleep(0.8)
print(funcs.sec_show)
vars.do_ter()
print ('\nvars has done ter_layer succesfully..\n')
sleep(1.2)
print ('\n\n')
print ('sec_layer[vars] completed..')


print ('\n\n')
ter_funcs.ter_layer_display()
sleep(0.8)
print(ter_funcs.ter_show)
ter_funcs.home()
print ('\nvars has done home succesfully..\n')
sleep(1.2)
print ('\n\n')
print ('ter_layer[funcs] completed..')


print ('\n\n')
ter_vars.ter_layer_display()
sleep(0.8)
print(ter_funcs.ter_show)
ter_vars.home()
print ('\nvars has done home succesfully..\n')
sleep(1.2)
print ('\n\n')
print ('ter_layer[vars] completed..')
sleep(0.8)
print('\n\n Succesful import excersices on python: {}'.format(sys.version_info[0]))


sleep(1.2)
print ('\n\n')
details= '''
Author: ThefxXxer [ Managwi Ikenna Alfred ]
Github: @ThefixXxer
Linkdin: Ikenna Alfred Managwu
'''
print (details)