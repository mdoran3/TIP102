def find_cruise_length(cruise_lengths, vacation_length):
    low = 0
    high = len(cruise_lengths) - 1

    while low <= high:
        mid = (low+high) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif vacation_length > cruise_lengths[mid]:
            low = mid + 1
        else:
            high = mid -1
    return False

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))


# UNDERSTAND
    # Given an integer or "target" which is the length of desired vacation
    # Given a list of possible vacations with their lengths
    # CONSTRAINT: Algo needs to be O(logn)
    # Binary search 

# PLANNING
    # Try using binary search
    # Use recursion
    # find a midpoint (by using len() function)
        # see if midpoint equal target
        # if it equals we probably want to return it
        # if not, then recursively call func() with updated list and target params