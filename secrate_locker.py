row1 = ['🔵' , '🔵' ,'🔵']
row2 = ['🔵' , '🔵' ,'🔵']
row3 = ['🔵' , '🔵' ,'🔵']
matrix = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
print("Where you have to store your money")
n = int(input("enter row "))
m = int(input("enter column "))
matrix[n-1][m-1] = '🔐'
print(f"{row1}\n{row2}\n{row3}")