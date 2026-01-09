class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items += [value]   # no append()

    def print_stack(self):
        i = len(self.items) - 1
        while i >= 0:
            print(self.items[i])
            i -= 1

# Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.print_stack()
