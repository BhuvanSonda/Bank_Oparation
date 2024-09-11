import font as ac

x= int(input("enter a number of customer :"))
acounts = {}
for i in range(1, x+ 1):
    d = ac.accounts()
    acounts[i] = d
print(acounts)

for key in acounts:
    print(f"\n\nName :-{acounts[key]['Name']}\nAc.No:- {acounts[key]['AC.NO']}\nIFSC CODE :- {acounts[key]['IFSC']}"
          f"\nBalance :-  {acounts[key]['Balance']}\n")
