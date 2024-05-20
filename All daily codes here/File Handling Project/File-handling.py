# Making a file handling project
# We are going to make a file handling project in next 2 days, and you can check my commits here in this folder

from pathlib import Path

def createfolder():
    try:
        namef = input("Tell you folder name: ")
        if namef == "":
            namef == "New folder"
        path = Path(namef)
        path.mkdir()
        print(f"Folder {namef} created successfully")
    except Exception as err:
        print(f"Error: Folder {namef} already exist")

def readfilesandfolders():
    path = Path("./All daily codes here/")               # Here you can put path where you want to read otherwise(empty directory) it will read through current directory
    items = list(path.rglob("*"))
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")
        
def updatefolder():
    readfilesandfolders()
    name = input("Which folder you want to update/change name: ")
    path = Path(name)
    if path.exists() and path.is_dir():
        newname = input("Enter the new name: ")
        new_path = Path(newname)
        path.rename(new_path)
    else:
        print("No such named folder exists")   


print("Press 1 for creating a folder")
print("Press 2 for reading files and folders")
print("Press 3 for Updating a folder")
print("Press 4 for deleting a folder")

check = int(input("What do you want: "))

if check == 1:
    createfolder()
elif check == 2:
    readfilesandfolders()
elif check == 3:
    updatefolder()