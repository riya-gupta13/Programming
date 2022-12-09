class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isempty(self):
        return self.items == []

    def peek(self):
        if not self.isempty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '({[':
            s.push(paren)
        else:
            if s.isempty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.isempty() and is_balanced:
        return True
    else:
        return False


def div_by_2(num):
    s = Stack()
    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2
    bin_num = ''
    while not s.isempty():
        bin_num += str(s.pop())
    return bin_num


def reverse_string(stack, string):
    for i in range(len(string)):
        stack.push(string[i])
    rev = ''
    while stack.isempty():
        rev += stack.pop()


if __name__ == '__main__':
    s = Stack()
    s.push('A')
    s.push('B')
    print(s.get_stack())
    s.push('C')
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
    print(s.peek())
    print(is_paren_balanced('()(()(){}'))
    print(div_by_2(242))
    print('hello')
