names=set()

while True:
 name=input("Enter a name: ")

 if name == "":
  break
 elif name in names:
     print("Name already in use")
 else:
     print("new name")
     names.add(name)

print(names)