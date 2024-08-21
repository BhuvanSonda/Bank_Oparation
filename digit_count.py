x=int(input("Enter any number :"))
count=0

while x != 0:
    x=x//10
    count+=1
print("Entered number has ",count,"digits")
