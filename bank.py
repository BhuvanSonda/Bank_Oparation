import datetime as dt
import pandas  as pd  
class Bank:
    def __init__(self):
        self.customer={"Names":[],"A/C No:":[],"Balance :":[],"Sign:":[],"Time:":[]}
b=Bank()    
data={"Names":[],
          "A/C No:":[],
          "Balance :":[],
          "Sign:":[],
          "Time:":[]}  
class Update: 
    def update(Name,account_no,sign,init_balance,time):
        data["Names"].append(Name)
        data["A/C No:"].append(account_no)
        data["Balance :"].append(init_balance)
        data["Sign:"].append(sign)
        data["Time:"].append(time)
        df=pd.DataFrame(data)
        df.to_excel("data.xlsx",mode="w",index=0)

    
read=pd.read_excel("data.xlsx")
class bank:
    def __init__(self):
        self.read=pd.read_excel("data.xlsx")
    def create(self,Name,account_no,sign,init_balance):
        
        for i in self.read["A/C No:"]:
            if account_no == i:
                print("This account has already existed ")
                break
        else:
            time=dt.datetime.now()
            Update.update(Name,account_no,sign,init_balance,time)
            print("your account successfully created ")
        

    def deposit(self,account_no,amount):
        for i in self.read["A/C No:"]:
            if account_no == i:
                for b in self.read["Balance :"]:
                    if self.read[i]==self.read[b]:
                        b+=amount
                        self.read
                        print("your account successfully deposited ")
                        print("your account balance is ",b)
                    break
        else:
            print("Account number does not exist!")

    def withdraw(self,account_no,sign,amount):
        for i in self.read["A/C No:"]:
            if account_no == i:
                for b in self.read["Balance :"]:
                    if self.read[i]==self.read[b]:
                        b+=amount
                        print("your account successfully Withdraw ") 
                    print("your account balance is ",b)
                    break
                else:
                    print('Insufficient fund!!')
                    break
            else:
                print('Missmatched Signature')
                break
        else:
            print("Account number does not exist!")

    def check(first,account_no):
        if account_no in b.customer:
            print(f'\n\nName : {b.customer[account_no]["Name:"]}\nA/C No : {b.customer[account_no]["A/C No:"]}\nAvailable Balance is : {b.customer[account_no]["Balance : "]}')
        else:
            print("Account number does not exist!")

    def display(self):
        for i in b.customer:
            print(f'\n\nName : {b.customer[i]["Name:"]}\nA/C No : {b.customer[i]["A/C No:"]}\nAvailable Balance is : {b.customer[i]["Balance : "]}\n')
a=bank()

x=1
while x!=0:
    a=bank()
    x=int(input("\nenter\n0-->EXIST\n1-->create new account\n2-->Deposit\n3-->withdraw\n4-->check balance\n"))

    if x==0:
        break


    if x ==1:
        nm=input("Enter Name : ")
        ac=(input("enter account number : "))
        amount=int(input("enter amount to deposit : "))
        sign=input("enter signature : ")
        a.create(nm,ac,sign,amount)
    elif x==2:
        ac = (input("enter account number : "))
        amount = int(input("enter amount  : "))
        a.deposit(ac,amount)
    elif x==3:
        ac = (input("enter account number : "))
        amount = int(input("enter amount  : "))
        sign = input("enter signature : ")
        a.withdraw(ac,sign,amount)
    elif x == 4:
        ac = (input("enter account number : "))
        a.check(ac)
    
    else:
        print("Entered wrong !!  Try again")
