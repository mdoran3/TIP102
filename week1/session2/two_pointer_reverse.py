def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while start <= end:
        lst[start], lst[end] = lst[end], lst[start]
        # temp = lst[start]
        # lst[start] = lst[end]
        # lst[end] = temp

        start += 1
        end -= 1
    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))