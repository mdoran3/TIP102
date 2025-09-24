def get_item(items, x):
	#edge case
    if x > len(items) - 1:
        return None

    #regular case
    for i in range(len(items)):
        if i == x:
            return items[i]

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)
print(get_item(items, x))

items = []
x = 5
get_item(items, x)
print(get_item(items, x))