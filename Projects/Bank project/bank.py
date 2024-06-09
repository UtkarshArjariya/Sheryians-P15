# Some day notes OOPS


import json
import string
import random
import os

class Bank:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    database = os.path.join(current_dir, "bank.json")
    data = []

    try:
        with open(database) as fs:
            data = json.loads(fs.read())
    except Exception as err:
        print(err)
    
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
        number = random.choices(string.digits, k=6)
        random.shuffle(number)
        return "".join(number)
    
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
            print(f"Your Current balance : {user[0]['balance']}")
            amt = int(input("How much amount you want to deposit : "))
            if amt > 9999:
                print("Sorry you cannot deposit this much.")
            else:
                user[0]["balance"] += amt 
                print("Amount added successfully.")
                Bank.updatedata()
    
    @classmethod
    def withdrawmoney(cls):
        an = input("Enter your account number : ")
        pin = int(input("please tell your pin : "))
        user = [i for i in cls.data if i["Account Number"] == an and i["pin"] == pin]
        
        if not user:
            print("no user found")
        else:
            print(f"Your Current balance : {user[0]['balance']}")
            amt = int(input("How much amount you want to withdraw : "))
            if amt > user[0]["balance"]:
                print("Insufficient balance.")
            else:
                user[0]["balance"] -= amt 
                print("Amount withdrawn successfully.")
                Bank.updatedata()
    
    @classmethod
    def updatebankdetails(cls):
        an = input("Enter your account number : ")
        pin = int(input("please tell your pin : "))
        user = [i for i in cls.data if i["Account Number"] == an and i["pin"] == pin]
        
        if not user:
            print("no user found")
        else:
            print(f"Your Current details : {user[0]}")
            info = {
                "name" : input("Enter your updated Name : "),
                "email" : input("Enter your updated email ID : "),
                "number" : int(input("Enter your updated mobile Number : ")),
                "pin" : int(input("please tell your updated 4-digit pin : ")),
            }
            user[0].update(info)
            print("Bank details updated successfully.")
            Bank.updatedata()

print("press 1 for creating an account : ")
print("press 2 to Deposit money : ")
print("press 3 to Withdraw money : ")
print("press 4 to Update bank details : ")

check = input("Enter your choice : ")
    
if check == "1":
    Bank.createaccount()    
elif check == "2":
    Bank.depositemoney()
elif check == "3":
    Bank.withdrawmoney()
elif check == "4":
    Bank.updatebankdetails()
else:
    print("Invalid choice.")
