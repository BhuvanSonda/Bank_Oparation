Prime=[1]
Composit=[]
def prime(x):
    i=0
    while i <= x:
        print("val of i:",i)
        for j in range(2,i+1,3):
            print("value of j =",j,"  value of i =",i)
            if i%j==0:
                if i==j:
                    Prime.append(i)
                else:
                    Composit.append(i)
                break
        i+=1
    print("Prime numbers are : ",Prime)
    print("Composite numbers are : ",Composit)

    Prime.clear();Composit.clear()
    Prime.append(1)

num=1
while num != 0:
    num = int(input("Enter any number to find the present prime and composite numbers in that range :"))
    if num == 0:
        print("\nThank You!!")
        break
    else:
        prime(num)
