def is_balanced(expression):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}


## iterate over each character in expression string
    for char in expression:
        if char in bracket_pairs.values():  
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    return not stack

