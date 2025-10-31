def is_profitable(excursion_counts):
    nums = len(excursion_counts)
    count = 0
    for i in range(0, len(excursion_counts)):
        if excursion_counts[i] >= nums:
            count +=1
    if count == 0:
        return -1
    return count

print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
