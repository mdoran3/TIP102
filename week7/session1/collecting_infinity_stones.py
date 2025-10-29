def sum_stones(stones):
    if not stones:
        return 0
    else:
        power = stones.pop()
        return power + sum_stones(stones)

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))

# UNDERSTAND
    # we have a list of integers
    # we need to return the sum of the integers in the list
    # need to use recursion

# PLANNING
    # Have a base case
    # set var equal to stones.pop()
    # Have a recursive case 
    # Return the recursive call + the var