from os import listdir
from os.path import isfile, join

# set up folder structure as following,
# |-script.py
# |-file

# changeList even numebr (original) index 0,2,4 to odd number (new)
# eg: changeList = [old,new,old,new...]
folderName = input('Enter the folder name: ')
old = input('Enter the word you want to change: ')
new = input('Enter the word you want to change to: ')

# Can be modified in the futue to chagne it to support multiple words replace 
changeList = [old,new]

changeFrom = [];
changeTo = [];

# populate the changeFrom and changeTo array
for i in range(len(changeList)):
 if i % 2 == 0:
  changeFrom.append(changeList[i]);
 else:
  changeTo.append(changeList[i]);

# list all file but ignore the hidden one
filesName = [f for f in listdir(folderName) if isfile(join(folderName, f)) and f[0] != "."]

for fileName in filesName:
  print("Processing ",fileName);
  filedata="";

  # Read in the file
  with open(folderName+'/'+fileName, 'r') as file :
    filedata = file.read();

    # Replace the target string
    for i in range(len(changeFrom)):
      print("changing " + changeFrom[i] + " to " + changeTo[i])
      filedata = filedata.replace(changeFrom[i], changeTo[i])

    file.close()

  with open(folderName+'/'+fileName, 'w') as file :

    file.write(filedata)
    file.close()

  print("Finish processing ", fileName)