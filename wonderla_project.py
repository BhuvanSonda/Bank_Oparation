print("""Well Come To "Wonder🤩la"

Ticket prices:

Children (above 5 year)= 150$ 
adults = 500$
Older persons (above 60 year) = 300$
for Premium = 125$ extra!!

parking Charge:
Car/Traveller/Bus = 350$
Bike = 180$
for Premium = 52$""")
car1 = 0
bike1 = 0
Total = 0
P_total = 0

children = int(input("Enter the number of children : "))
adult = int(input("Enter the number of adults : "))
older = int(input("Enter the number of older persons : "))

if children == 0 and adult == 0 and older == 0:
    print("Please Enter valid information!! ")
elif children != 0 and adult == 0 and older == 0:
    print("Only Children are not allowed!! ")

else:
    premium = input("Are you want premium ticket ? (yes/no) :").lower()
    parking = input("Are you have a vehicle? (yes/no)").lower()
    if parking == 'yes':
        car = input("you have a Car/Traveller/Bus ? (yes/no) :").lower()
        bike = input("you have a bike ? (yes/no) :").lower()
        if car == 'yes' and bike == 'yes':
            car1 = int(input("Enter the number of Car/Traveller/Bus : "))
            bike1 = int(input("Enter the number of Bikes : "))
        elif car == 'yes':
            car1 = int(input("Enter the number of Car/Traveller/Bus : "))
        else:
            bike1 = int(input("Enter the number of Bikes : "))

    if premium == 'yes':
        if parking == 'yes':
            P_total = ((car1 * 350) + (bike1 * 180)) + 52
        else:
            P_total = 0
        Total = ((children * 150) + (adult * 500) + (older * 300)) + 125
        print(""f"\n\nTicket Price\nChildren {children} * 150$ = {children * 150}"
              f"\nAdults {adult} * 500$ = {adult * 500}"
              f"\nOlder person {older} * 300 = {older * 300}\nCandidates Total + Premium(125$) = {Total}\n\n"
              f"Parking Bill:\nCar/Traveller/Bus--> {car1}*350$ = {car1 * 350}"
              f"\nBike--> {bike1}*180$ = {bike1 * 180}\nParking Total + Premium(52$) = {P_total}"
              f"\n\nTotal : {Total + P_total}"
              f"Here the QR :: \n You can scan & pay..\n🤩HAVE NICE DAY 🥰!!""")
    else:
        P_total = (car1 * 350) + (bike1 * 180)
        Total = (children * 150) + (adult * 500) + (older * 300)
        print(""f"\n\nTicket Price\nChildren {children} * 150$ = {children * 150}"
              f"\nAdults {adult} * 500$ = {adult * 500}"
              f"\nOlder person {older} * 300 = {older * 300}\nCandidates Total = {Total}\n\n"
              f"Parking Bill:\nCar/Traveller/Bus {car1}*350$={car1 * 350}"
              f"\nBike {bike1} * 180$ = {bike1 * 180}\nParking Total = {P_total}\n\nTotal : {Total}"
              f"Here the QR :: \n You can scan & pay..\n🤩HAVE NICE DAY 🥰!!""")
