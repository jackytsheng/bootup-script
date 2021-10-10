file= input("Enter file name: ")
with open(file) as f:
    lines = f.readlines()

print(len(lines[0].split(" ")))