# 큐
# 선입선출
from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.popleft()
queue.append(2)
queue.append(1)
queue.popleft()

#queue.pop을 하면 맨 마지막에 들어온게 빠짐
#queue.popleft를 하면 맨 처음에 들어온게 빠짐 

print(queue)
