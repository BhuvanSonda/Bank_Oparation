import random
print("To create Password")

letters="q,w,e,r,t,y,u,i,o,p,l,k,j,h,g,f,d,s,a,z,x,c,v,b,n,m,W,Q,E,R,T,Y,U,I,O,P,L,K,J,H,G,F,D,S,A,Z,X,C,V,B,N,M"
special="!,@,#,$,%,^,&,*,(,),<,>"
numbers=[1,2,3,6,5,4,7,8,9]
letters=letters.split(",")
special=special.split(",")
passw=""
ltr=int(input("enter the number of letters :"))
spl=int(input("enter the number of special letters :"))
num=int(input("enter the number of digits :"))
password=[]
for i in range(ltr):
    char= random.choice(letters)
    passw += char
for i in range(spl):
    char = random.choice(special)
    passw += char
for i in range(num):
    char = random.choice(numbers)
    passw += str(char)

for i in passw:
    password.append(i)

random.shuffle(password)
str_password=""

for i in password:
    str_password+=i
print(f"\nyour password is:-  {str_password}")
