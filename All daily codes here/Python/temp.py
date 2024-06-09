# Some day notes OOPS

import json
import string
import random

class Bank:
    database = "bank.json"
    data = []
    
    
    try:
        with open(database) as fs:
            data = json.loads(fs.read())
    except Exception as err:
        print(err)
        
                    
    @classmethod
    def updatedata(cls):
        with open(cls.database,"w") as fs:
            fs.write(json.dumps(cls.data))
    
        
    @classmethod
    def randomifsc(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        number = random.choices(string.digits,k = 3) 
        spchar = random.choices("!@#$%^&*",k = 2)
        id = alpha + number + spchar        
        random.shuffle(id)
        return "".join(id)
    
        
    @classmethod
    def createaccount(cls):
        info = {
            "name" : input("Enter your Name : "),
        "email" : input("Enter your email ID : "),
        "number" : int(input("Enter your mobile Number : ")),
        "Account Number" : cls.randomifsc(),
        "pin" : int(input("please tell your 4-digit pin : ")),
        "balance" : 0,
        }
        cls.data.append(info)
        cls.updatedata()


    @classmethod
    def depositemoney(cls):
        an = input("Enter your account number : ")
        pin = int(input("please tell your pin : "))
        user = [i for i in cls.data if i["Account Number"] == an and i["pin"] == pin]
        
        if not user:
            print("no user found")
        else:
            print(f"Your Current balance : {user[0]["balance"]}")
            amt = int(input("How much amount you want to deposit : "))
            if amt > 9999:
                print("Sorry you cannot deposit this much.")
            else:
                user[0]["balance"] += amt 
                print("Amount added successfully.")
                Bank.updatedata()
            
            
print("press 1 for creating an account : ")
print("press 2 to Deposit money : ")

check = input("Enter your choice : ")
    
if check == "1" :
    Bank.createaccount()    
elif check == "2":
    Bank.depositemoney()