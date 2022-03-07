from collections import deque


class Stack:
    def __init__(self) -> None:
        self.container = deque()
        print(self.container)

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def pushBulkValue(self, list):
        for i in list:
            self.container.append(i)

    def clearStack(self):
        self.container.clear()

    def printStack(self):
        for i in range(len(self.container), 0, -1):
            print(i-1, "-->", self.container[i-1], "-->", end="\n")
        print("\n")

    def reverse_string(self):
        data = ""
        while len(self.container):
            data += self.pop()
        print(data)
        print(self.container)


def isMatch(ch1, ch2):
    paratheses = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return paratheses[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            stack.push(ch)
        if ch == ")" or ch == "]" or ch == "}":
            if stack.size() == 0:
                return False
            if not isMatch(ch, stack.pop()):
                return False
    return stack.size() == 0
    
#Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". 
if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("(*)(*)}"))
        


# if __name__ == '__main__':
#     stack = Stack()
#     for i in "We will conquere COVID-19":
#         stack.pushBulkValue(i)
#     stack.printStack()
#     stack.reverse_string()
