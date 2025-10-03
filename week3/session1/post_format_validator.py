def is_valid_post_format(posts):
    stack = []

    matches = {')' : '(', '}' : '{', ']' : '['}

    for char in posts:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            else:
                if stack[-1] == matches[char]:
                    stack.pop()
    return len(stack) == 0      

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

# Understand
 # make sure we have balanced types of brackets
 # make sure brackets are ordered correctly as well

# Planning
    # Stack implementation 
    # if closing bracket and stack empty => return False
    # push opening brackets to stack "(, [, { "
    # If you see a closing bracket, look for a corresponding open bracket, if found, pop it off. 
    # if the top of the stack matched (eg. ([{}])) corresponding open brackts, pop it
    # if closing bracket is seen pop opening from stack 