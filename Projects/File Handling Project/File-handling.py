# Making a file handling project
# We are going to make a file handling project in next 2 days, and you can check my commits here in this folder

from pathlib import Path
import os

def createfolder():
    try:
        readfilesandfolders()
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
    try:
        readfilesandfolders()
        name = input("Which folder you want to update/change name: ")
        path = Path(name)
        if path.exists() and path.is_dir():
            newname = input("Enter the new name: ")
            new_path = Path(newname)
            path.rename(new_path)
        else:
            print("No such named folder exists") 
    except Exception as err:
        print(f"{err} sorry this error occured")  
        
def deletefolder():
    try:
        readfilesandfolders()
        name = input("Enter the name of your folder: ")
        path = Path(name)
        if path.exists() and path.is_dir():
            path.rmdir()
        else:
            print("No path exist with this name")
    except Exception as err:
        print(f"{err} sorry this error occured")
        
def createfile():
    try:
        readfilesandfolders()
        name = input("Enter the name of the file: ")
        path = Path(name)
        if not path.exists():
            with open(name, 'w') as fs:
                data = input("What do want to write in the file: ")   # You can remove this two line and can write "pass" to continue without writing anything
                fs.write(data)
            print(f"File {name} created successfully")
        else:
            print("Sorry this file name already exist")
    except Exception as err:
        print(f"{err} sorry this error occured")

def readfile():
    try:
        readfilesandfolders()
        name = input("Enter the file you want to read: ")
        path = Path(name)
        if path.exists():
            with open(name, 'r') as fs:
                data = fs.read()
                print(data)
        else:
            print("Sorry this file name doesn't exist")
    except Exception as err:
        print(f"{err} sorry this error occured")

def updatefile():
    try:
        readfilesandfolders()
        name = input("Enter the file name you want to update: ")
        path = Path(name)
        if path.exists():
            print("Press 1 for changing the file name")
            print("Press 2 for appending new content in the file")
            print("Press 3 for deleteing all the content of the file")
            choice = int(input("What you wanna do: "))

            if choice == 1:
                new_name = input("Enter the new name for the file: ")
                new_path = Path(new_name)
                if not new_path.exists():
                    path.rename(new_path)
                    print("Name changes successfully")
                else:
                    print("Sorry, this file name already exist")
            elif choice == 2:
                with open(name, 'a') as fs:
                    data = input("What do you want to append: ")
                    fs.write(" " + data)
                print("Content appended successfully")
            elif choice == 3:
                with open(name, "w") as fs:
                    data = input("Press enter to skip or write new data: ")
                    fs.write(data)
                print("All the content deleted successfully")
    except Exception as err:
        print(f"{err} sorry this error occured")
            
def deletefile():
    try:
        readfilesandfolders()
        name = input("Enter the file name your want to delete: ")
        path = Path(name)
        if path.exists() and path.is_file():
            # os.remove     # You can use this also to remove the path
            path.unlink()
        else:
            print("Sorry this file doesn't exist")
    except Exception as err:
        print(f"{err} sorry this error occured")


print("Press 1 for creating a folder")
print("Press 2 for reading files and folders")
print("Press 3 for Updating a folder")
print("Press 4 for deleting a folder")
print("Press 5 for creating a file")
print("Press 6 for read a file")
print("Press 7 for updating a file")
print("Press 8 for deleting a file")

check = int(input("What do you want: "))

if check == 1:
    createfolder()
elif check == 2:
    readfilesandfolders()
elif check == 3:
    updatefolder()
elif check == 4:
    deletefolder()
elif check == 5:
    createfile()
elif check == 6:
    readfile()
elif check == 7:
    updatefile()
elif check == 8:
    deletefile()