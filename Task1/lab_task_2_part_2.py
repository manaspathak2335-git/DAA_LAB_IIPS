from collections import deque

tasks = ["Task1","Task2","Task3","Task4","Task5"]

mystack = deque()
comp_order_stack = []

myqueue = deque()
comp_order_queue = []

for task in tasks:
    mystack.append(task)
    myqueue.append(task)

while mystack:
    comp_order_stack.append(mystack.pop())

while myqueue:
    comp_order_queue.append(myqueue.popleft())

print("Completion order when served using stack:",comp_order_stack)
print("Completion order when served using queue:",comp_order_queue)


    
