import queue

stack=queue.LifoQueue()
stack.put(12)
stack.put(13)
print(stack)
stack.get(timeout=1)
print(stack)

import collections

stack=collections.deque()
stack.append(1)
stack.append(13)
print(stack)
print(stack.pop())
print(stack)

