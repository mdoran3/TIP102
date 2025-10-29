def count_suits_iterative(suits):
    pass

unique_suits = set()
def count_suits_recursive(suits):
    if not suits:
        return 0
    last = suits.pop()
    if last not in unique_suits:
        unique_suits.add(last)
        return 1 + count_suits_recursive(suits)
    else:
        return count_suits_recursive(suits)

print(count_suits_iterative(["Mark I", "Mark I", "Mark III", "Mark IV"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

# UNDERSTAND
    # create iterative and recursive versions
    # input list of strings
    # output is number of distinct suits (uniqueness)

# PLANNING
    # ITER
        # use for loop 
        # create set

    # RECURSE
        # Have a base case
        # create set
        # pop element from list and add to set
