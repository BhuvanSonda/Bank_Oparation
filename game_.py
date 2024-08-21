import datetime as dt
import pandas as pd
import re
import os

data = {"Names": [], "A/C No:": [], "Balance :": [], "Sign:": [], 'Mobile_No:':[],'Adhar_No:':[],"Time:": []}

class Update:
    @staticmethod
    def update(name, account_no, sign, init_balance, mobile_no, adhar_no, time):
        new_entry = {
            "Names": [name],
            "A/C No:": [account_no],
            "Balance :": [init_balance],
            "Sign:": [sign],
            "Mobile_No:": [mobile_no],
            "Adhar_No:": [adhar_no],
            "Time:": [time]
        }
        df = pd.DataFrame(new_entry)
        df.to_csv("data.csv", mode="a", index=False, header=not os.path.exists("data.csv"))

class Validation:
    @staticmethod
    def Mobile():
        M = re.compile("^[6-9][0-9]{9}$")
        while True:
            mobile = input("Enter Mobile No: ")
            if M.match(mobile):
                return mobile
            else:
                print("Invalid Mobile No. Please try again.")

    @staticmethod
    def Adhar():
        A = re.compile("^[2-9][0-9]{11}$")
        while True:
            adhar = input("Enter Adhar No: ")
            if A.match(adhar):
                return adhar
            else:
                print("Invalid Adhar No. Please try again.")

class BankOperations:
    def __init__(self):
        self.file_path = "data.csv"
        self.columns = ["Names", "A/C No:", "Balance :", "Sign:", "Mobile_No:", "Adhar_No:", "Time:"]
        
        if os.path.exists(self.file_path):
            self.read = pd.read_csv(self.file_path)
        else:
            self.read = pd.DataFrame(columns=self.columns)
            self.read.to_csv(self.file_path, index=False)
    
    def ac_generator(self):
        if self.read.empty:
            return 123
        else:
            return max(self.read['A/C No:']) + 1
    
    def create(self):
        name = input("Enter Name: ")
        account_no = self.ac_generator()
        init_balance = int(input("Enter amount to deposit: "))
        sign = input("Enter signature: ")
        mobile_no = Validation.Mobile()
        adhar_no = Validation.Adhar()
        current_time = dt.datetime.now()

        if account_no in self.read["A/C No:"].values:
            print("--" * 15)
            print("This account already exists.")
        else:
            Update.update(name, account_no, sign, init_balance, mobile_no, adhar_no, current_time)
            print("--" * 15)
            print("Your account has been successfully created.")
            self.read = pd.read_csv(self.file_path)  # Refresh the DataFrame with updated data

    def deposit(self):
        account_no = int(input("Enter account number: "))
        amount = int(input("Enter amount: "))
        
        if account_no in self.read["A/C No:"].values:
            index = self.read.index[self.read["A/C No:"] == account_no].tolist()[0]
            self.read.at[index, "Balance :"] += amount
            self.read.to_csv(self.file_path, index=False)
            print("--" * 15)
            print("Your account has been successfully deposited.")
            print(f"Your account balance is {self.read.at[index, 'Balance :']}")
        else:
            print("--" * 15)
            print("Account number does not exist!")
            choice = input("Please create your account\nPress\nY --> for Create\nN --> for Not Create\n").lower()
            if choice == 'y':
                self.create()
            else:
                print("--" * 15)
                print("Thank you for using our services")

    def withdraw(self):
        account_no = int(input("Enter account number: "))
        if account_no in self.read["A/C No:"].values:
            index = self.read.index[self.read["A/C No:"] == account_no].tolist()[0]

            sign = input("Enter signature: ")
            while self.read.at[index, "Sign:"] != sign:
                print("--" * 15)
                print("Mismatched signature!")
                sign = input("Enter your correct signature: ")

            if self.read.at[index, "Sign:"] == sign:
                amount = int(input("Enter amount: "))
                if self.read.at[index, "Balance :"] >= amount:
                    self.read.at[index, "Balance :"] -= amount
                    self.read.to_csv(self.file_path, index=False)
                    print("--" * 15)
                    print("Your account has been successfully withdrawn.")
                    print(f"Your account balance is {self.read.at[index, 'Balance :']}")
                else:
                    print("--" * 15)
                    print("Insufficient funds!")
                    while True:
                        try:
                            amount = int(input("Enter valid amount: "))
                            if amount > 0 and self.read.at[index, "Balance :"] >= amount:
                                self.read.at[index, "Balance :"] -= amount
                                self.read.to_csv(self.file_path, index=False)
                                print("--" * 15)
                                print("Your account has been successfully withdrawn.")
                                print(f"Your account balance is {self.read.at[index, 'Balance :']}")
                                break
                            else:
                                print("Insufficient funds or invalid amount! Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a valid amount.")
        else:
            print("--" * 15)
            print("Account number does not exist!")
            choice = input("Please create your account\nPress\nY --> for Create\nN --> for Not Create\n").lower()
            if choice == 'y':
                self.create()
            else:
                print("Thank you for using our services")

    def check(self):
        account_no = int(input("Enter account number: "))
        if account_no in self.read["A/C No:"].values:
            index = self.read.index[self.read["A/C No:"] == account_no].tolist()[0]
            print("--" * 15)
            print(f"\n\nName: {self.read.at[index, 'Names']}")
            print(f"A/C No: {self.read.at[index, 'A/C No:']}")
            print(f"Available Balance: {self.read.at[index, 'Balance :']}")
        else:
            print("--" * 15)
            print("Account number does not exist!")
            choice = input("Please create your account\nPress\nY --> for Create\nN --> for Not Create\n").lower()
            if choice == 'y':
                self.create()
            else:
                print("Thank you for using our services")

print("--" * 10)

x = 1
bank_operations = BankOperations()

while x != 0:
    x = int(input("\nEnter\n0 --> EXIT\n1 --> Create new account\n2 --> Deposit\n3 --> Withdraw\n4 --> Check balance\n"))
    print("--" * 15)

    if x == 0:
        break
    elif x == 1:
        bank_operations.create()
    elif x == 2:
        bank_operations.deposit()
    elif x == 3:
        bank_operations.withdraw()
    elif x == 4:
        bank_operations.check()
    else:
        print("Invalid input! Try again.")
