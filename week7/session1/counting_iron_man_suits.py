def count_suits_iterative(suits):
    count = 0
    for _ in suits:
        count +=1
    
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    else:
        suits.pop()
        return 1 + count_suits_recursive(suits)

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

# UNDERSTAND
    # One process is iterative
        # cannot use len() func()
        # most likely using loop to iterate

    # One process is recursive
        # need base case
        # need to make a recursive call within func()

# PLANNING
    # ITER
    # Iterate through list of strings (input)
    # create count var
    # for loop or while loop
    # return count var

    # RECURSE
    # base case: could start from back of list and pop off elements
    # when element is popper, global count is += 1
    # once base case is hit (no elements left in list), then return count