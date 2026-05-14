def isValid(s: str) -> bool:
    stack = []

    for char in s:
        # قوس فاتح → حطه في الـ stack
        if char in '([{':
            stack.append(char)
        
        # قوس غالق → تحقق إذا يطابق آخر فاتح
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
        
        elif char == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()

    return len(stack) == 0


# example

print(isValid("()"))      # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))      # False
print(isValid("{[]}"))    # True
