y=int(input("enter Y-axise :" ))
x=int(input("enter X-axise :" ))

if x>0 and y>0:
    print("First Quadrant")
elif x<0 and y>0:
    print("Second Quadrant")
elif x>0 and y<0:
    print("Third Quadrant")
elif x < 0 and y < 0:
    print("Fourth Quadrant")

else:
    if x==0 and (y>0 or y<0):
        print("X-axise is in Origin and Y-axise is varing ")
    elif (x>0 or x<0) and y==0:
        print("Y-axise is in Origin and X-axise is varing ")
    else:
        print("Both axise are in Origin ")