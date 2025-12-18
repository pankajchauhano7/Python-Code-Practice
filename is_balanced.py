#Given a list or string containing brackets like ()[]{}, determine if it is balanced.
brackets="((()))"


def balanced(brackets):
    stack=[]
    mapping={')':'('}
    for ch in brackets:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop() 
    return len(stack) == 0
print(balanced(brackets))
