num = int(input("enter number  : "))
composit=[]
prime=[]
for i in range(num+1) :
    if i ==0 or i ==1:
        continue
    for j in range(i+1):
        if j == 0 or j ==1:
            continue
        elif i%j==0:
            if j==i:
                prime.append(i)
            else:
                composit.append(i)

            break

print(f"the prime numbers are {prime}")
print(f"The non prime numbers are {composit}")
