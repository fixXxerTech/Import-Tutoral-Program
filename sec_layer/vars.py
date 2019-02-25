try:
	import ter_layer.funcs_ter as funcs
	import ter_layer.vars_ter as vars
except:
	from .ter_layer import funcs_ter as funcs
	from .ter_layer import vars_ter as vars


def sec_layer_display():
	print ('In sec_layer_display funcs in sec_layer vars')

sec_show= 'In sec_layer_show var in sec_layer vars'


def do_ter():
	vars.ter_layer_display()
	print(vars.ter_show)

	funcs.ter_layer_display()
	print(funcs.ter_show)