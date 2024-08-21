num=[1,2,3,4,5,6]
c=0
for i in num:
    print(i)
    if i % 10==0:
        c=1
        break
else:
    print("successfully completed!! ")

if c ==1:
    print("loop is forcefully stopped!!")

num=[1,2,3,4,5,6]
for i in num:
    print(i)
    if i %3==0:
        c=1
        break
else:
    print("successfully completed!! ")

if c ==1:
    print("loop is forcefully stopped!!")