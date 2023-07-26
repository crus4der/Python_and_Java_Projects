
class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return self.stack.pop()
        else:
            return "the stack is empty"

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return "the stack is empty"

    def empty(self):
        if not self.stack:
            print("Stack is empty :((")
        else:
            return print(self.stack)

    def clear(self):
        return self.stack.clear()

    def str(self):
        return str(self.stack)

    def len(self):
        return len(self.stack)

