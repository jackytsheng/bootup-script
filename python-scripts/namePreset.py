from os import listdir,mkdir
from os.path import isfile, join
from distutils.dir_util import copy_tree

folderName = input('Enter the folder name: ')

# list all file but ignore the hidden one
dirNames = [f for f in listdir(folderName) if not isfile(join(folderName, f)) and f[0] != "."]

print(dirNames)

dest = 'presets03'

for index in range(len(dirNames)):
	
	f = dirNames[index];
	newDest = dest + '/theLutBayC' + str(index+1).zfill(2) + ' ' + f
	currentPath = folderName + '/'+f +'/LRtemplate' 
	print(currentPath," to ", newDest)

	if index == 0 :
		mkdir(newDest);
	

	copy_tree(currentPath,newDest);
