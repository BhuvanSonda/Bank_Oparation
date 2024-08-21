E_id={'sham':234,'bham':234,'guru':908}
print(E_id)
print(E_id['sham'])
id=dict([(1,'ram'),(2,'sham'),(3,'shankar')])
id[4]='bhuvan'
print(id)
id[2]='ragu'#it will update the values
print(id)
print(id.get(2))
print(id.get(4)) # it will print None
id[2]={'sham':234,'bham':234,'guru':908}  # for assign Dictionary as an variable
print(id)
print(id[2]['bham'])
del id[2]['bham']# Delete bham key using del
 # print(id[2]['bham'])
