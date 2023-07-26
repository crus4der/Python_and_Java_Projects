from NewProg.Stack import *
from NewProg.Queue import *
# NewProg - folder
# Stack/Queue  - python file name

stack = Stack()
queue = Que()

# Stack

# appending or push
stack.push("A")
stack.push("B")
stack.push("C")
print(stack.str(), "\n")

# pop or removing the top of the list

print(stack.pop())
print(stack.pop())
print(stack.pop() + "\n")

# peek or checking the top of the list

stack.push("A")
stack.push(1)
print(stack.str())
print(stack.peek(), "\n")


# size or length

print(stack.len(), "\n")

# empty and clearing

stack.push("There something here")
stack.empty()
stack.clear()
stack.empty()
print("\n")

# Queue

# enque

queue.enqueue("Song 1")
queue.enqueue("Song 2")
queue.enqueue("Song 3")
print(queue.str() + "\n")

# dequeue

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue() + "\n")

# front

queue.enqueue("Fill 1")
queue.enqueue("Fill 2")
print(queue.str())
print(queue.front(), "\n")

# size
print(queue.len(), "\n")

# empty and clear
queue.empty()
queue.clear()
queue.empty()






