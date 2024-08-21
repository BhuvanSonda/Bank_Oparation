set1={1,2,5,'bhuvan'}
set2={2,8,6,7,3,8,1}
set3={'ram','gagan',8,5,2,6}
print(set1.union(set2))
set1 |= set2 | set3
print(set1) #upadate sets
print(set3.intersection(set2))
print(set2 & set3)
print(set2.difference(set3))
print(set2 - set3)
print(set2.symmetric_difference(set3))
print(set2 ^ set3)
set4={1,2,3,4,5}
set5={1,5,4,8,2,3,}
print(set2.isdisjoint(set5))

print(set4.issubset(set5))
print(set4<=set5)

print(set4.issuperset(set5))
print(set4>=set5)
