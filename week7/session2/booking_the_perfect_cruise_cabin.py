def find_cabin_index(cabins, preferred_deck):
    low = 0
    high = len(cabins) -1

    while low <= high:
        mid = (low + high) // 2
        if cabins[mid] == preferred_deck:
            return mid
        elif preferred_deck >= cabins[mid]:
            low = mid + 1
        else:
            high = mid -1
    return mid + 1

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))