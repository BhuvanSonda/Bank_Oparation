import queue
list = queue.PriorityQueue()

list.put(12)
list.put(10)
list.put(56)
list.put(9)

print(id(list))

print(list.get())
print(list.get())
print(list.get())

