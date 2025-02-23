#!/usr/bin/env python3

import os
import shutil
from os import listdir
from datetime import datetime
from os.path import isfile, join

favourite = input(
    'folder for favourite file : [Enter if current directory is used] ')
toDelete = input(
    'folder for file to be deleted : [Enter if current directory is used] ')
if favourite == "":
    print('current directory is used')
    favourite = "."
else:
    print('keeping files in directory ' + favourite)

if toDelete == "":
    print('current directory is used')
    toDelete = "."
else:
    print('deleting files in directory ' + toDelete)

keepfiles = [f for f in listdir(favourite) if isfile(join(favourite, f))]
namesToKeep = [f.split(".")[0] for f in keepfiles if f.split(".")[0] != ""]
namesToKeepSet = set(namesToKeep)
print("files number found to keep is " + str(len(namesToKeep)))


deletefiles = [f for f in listdir(toDelete) if isfile(join(toDelete, f))]

deleteDict = {}
for f in deletefiles:
    if f.split(".")[0] != "":
        deleteDict[f.split(".")[0]] = f.split(".")[1]


namesToDelete = deleteDict.keys()
namesToDeleteSet = set(namesToDelete)
print("files number found to be check for delete is " + str(len(namesToDelete)))

filesToBeDeleted = namesToDeleteSet.difference(namesToKeepSet)
print("files be deleted {0} keeping {1} ".format(
    len(filesToBeDeleted), len(namesToDeleteSet) - len(filesToBeDeleted)))

filesToBeDeletedName = [f+"."+deleteDict[f] for f in filesToBeDeleted]
filesToBeDeletedName.sort()
print("files to be deleted are the following")
print(filesToBeDeletedName)
confirm = input("do you want to direct delete the files [Y/N] ? ")

if confirm == "Y" or confirm == "y":
    print("removing files ...")
    for f in filesToBeDeletedName:
        os.remove(toDelete+"/"+f)

    print("finish removing all files ...")

print("moving files into temp folder...")

tmp_destination = toDelete+'/tmp'+datetime.now().strftime("%Y-%m-%d")
os.mkdir(tmp_destination)
for f in filesToBeDeletedName:
    shutil.move(toDelete+"/"+f, tmp_destination)

print("finish removing all files ...")
