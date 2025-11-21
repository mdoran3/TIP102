def can_rebook(flights, source, dest):
    length= len(flights[source])
    if flights[source][dest] == 1:
        return True
    stack.push(flights[source]) 
    helper(stack)
    def helper(stack):
        while stack:
            sourceFromTheStack = stack.pop()
            for position in range(length):
                if flights[sourceFromTheStack][position]==1:
                    stack.push(position)
                if flights[sourceFromTheStack][dest] == 1:
                    return True
        return False
    
flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 

# UNDERSTAND
    # Given an adjency matrix with available flights => flights1 && flights2
    # Given source and destination as params, we need to check if a flight is available


# PLANNING
    # check for direct route 
        # length= len(flights[source])
        # if flights[source][dest] == 1:
        #   return True
        # elif
            # use for looop to iterate the row source 
            # push all positions of "1s" on to stack
            # def helper(stack)
            #   while stack:
                  # sourceFromTheStack = stack.pop()
                  # for positon in range(length):
                          # if flights[sourceFromTheStack][position]==1:
                               # stack.push(position)
                  # if flights[sourceFromTheStack][destination] == 1:
            #         return True
            #   return False