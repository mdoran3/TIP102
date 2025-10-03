def reverse_comments_queue(comments):
    stack = []

    for i in range(len(comments) - 1, -1, -1): # iterate from end of loop, to beginning with a -1 k-step
        stack.append(comments[i])
    return stack

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# Understand
    # comments come in as list of stirngs
    # reverse string using stack

# Plan
    # iterate over the elements in comments from the last to the first
    # appending each element to the stack
    # return the stack