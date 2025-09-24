def sum_honey(hunny_jars):
    sum = 0
    for i in range(len(hunny_jars)):
        sum += hunny_jars[i]
    return sum

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))