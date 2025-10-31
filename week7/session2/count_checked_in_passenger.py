def count_checked_in_passengers(rooms):
    low = 0
    high = len(rooms)
    
    while low < high:
        mid = (low + high) // 2
        if rooms[mid] == 0:
            low = mid + 1
        else:
            high = mid
    return len(rooms) - low

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))