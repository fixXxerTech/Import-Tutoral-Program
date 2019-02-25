# Import-Tutoral-Program
***

# Overview

Import tutorial as the name implies is just a small educational program written in python to do nothing other than 
illustrate how to import your own scipts or functions from your own scripts which are not located in your current
directory. 

This can be quite a tricky twist between python2 and 3 as they have slightly different import techniques.
I used the sys module in my case, there are a number of ways to import modules [scripts or functions] in python,

## Examples:

1. Using the regular `import <scriptname>` [for script in the same directory ONLY!!];
	This for me seems to work very well on python2 where as on python3, i must add;
	`.` [a dot] in front of the scriptname i.e `import .<scriptname>`. Remember this method works for scripts in
	same directory only.

	The import statement can also be used to get a particular function or class [sub-module] inside an entire script.
`>>> from <scriptname> import <functionname>`   
for file in the same directory.
`>>> from <folder.second_folder.scriptname> import <functionname>`
for file in another directory.


2. Using the `importlib` module [takes either just the script name or full script location];
	This is a more up to date method and highly recommended as the importlib module is simply a wrpper around the 
	`__import__()` which is an unseen function invoked by the python interpreter when we normally import modules,
	i.e `import <modulename>`. This module however can be used as such;

`>>> import importlib`
`>>> importlib.import_module(<scriptname>)`
or
`>>> importlib.import_module(<folder.second_folder.scriptname>)`
You can specify the full path to your scrip like so.

This is recommended because it can be parsed by most recent python interpreter 2.7 or 3

3. Using the `sys.path` module;
	This the method i used in this small program. The familiar sys module has a not so familiar function called `path`
	i.e `import sys.path` . Now, this contains all the directories where your python interpreter will check for scripts
	when it sees an import statement. If you do a ;

`>>> import sys`
`>>> print(sys.path)`

It prints a list containing all the directorys in the python environment path. These directories are
	visible to python no matter where python is run from. So I used the `sys.path.append(<myscriptpath>)` method here. This will
	append a specified path to the python enironment os by using;

`>>> import sys`
`>>> import os`

`>>> sys.path.append(os.getcwd())`

I appended the current working directory of my script to the python environment temporarily in memory, during the duration the script is running, that way I was able to import all scripts in thenow appended directory, including the subfolders and modules [my scripts] all the way to the last folder `ter_layer` and in,the modules there, `funcs_ter.py` and `vars_ter.py`, I added functions called `home()` which just called a module names `home_dis.py` from **The parent directory** [which this file is now...look around this folder for the home_dis.py file]... This means all modules in the subfolder and all those in the sub-sub-folder where imported and ran, and them the last modules imported a module from the first [parent folder], all the way round. This is important in writting a professional program so all your functions don't look clustered in one file.


## To see more import styles see: 

python docs: [The import system](https://docs.python.org/3/reference/import.html)

See also: 
[StackOverflow answer1](https://stackoverflow.com/questions/2349991/how-to-import-other-python-files)   

[StackOverflow answer2](https://stackoverflow.com/questions/28231738/import-vs-import-vs-importlib-import-module) for more import examples.
***

# NOTE  

You must create an empty file called `__init__.py` in every folder in the path, thos will inform
python that to treat that folder as one module. 

## More on modules:

python docs: [Modules](https://docs.python.org/2/tutorial/modules.html)

In this program i used the 3rd option. This method has a catch though, the `sys.path.append(<myscriptpath>)` must be called at the beginning of the script before importing any any thing else or else the intepreter will attempt to import all modules stated before it gets to the 
`sys.path.append(<myscriptpath>)`. i.e;

`>>> import sys`
`>>> sys.path.append(<myscriptpath>)`

`>>> import <folder.second_folder.scriptname>`
or
`>>> from <folder.second_folder> import <scriptname>`
or
`>>> from <folder.second_folder.scriptname> import <functionname>`

In this program I avoided this ugly method by placing `sys.path.append(os.getcwd())` in all `__init__.py` files, as they are the first 
modules run by the python interpreter if they are present, by doing this the current directory is temporarily in memory, during the duration of the script running. Also note the use of exception handling to alternate between python 2 import style and python 3 if an error is hit, meaning wrong import stlye cause all files are present. 
