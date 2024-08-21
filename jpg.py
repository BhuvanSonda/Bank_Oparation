f1 = open("python.jpg", "rb")
f2 = open("image.jpg","wb")
print(f1.read())
for i in f1:
    f2.write(i)
