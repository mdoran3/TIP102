class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):

    if not evidence:
        return []
    
    slow = fast = evidence

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # print("cycle detected")
            break
    else:
        return []
    
    slow = evidence

    while slow != fast:
        slow = slow.next
        fast = fast.next

    cycle_start = slow

    result = []
    curr = cycle_start

    while True:

        result.append(curr.value)
        curr = curr.next
        if curr == cycle_start:
            break
    
    return result
    

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

# UNDERSTANDING/PLANNING:
# Step 1: Detect a cycle
# Step 2: Find Position of 1st Node in the Cycle
# Step 3: Return data in each node in a list
#
# Edge Case: 
# Iteration: 
# 1st while loop: Detect if there is a cycle
# 2nd while loop: Find "start" of cycle 
# 3rd while loop: Putting all values into a list


# while fast and fast.next:
#      if slow == fast:
#           print("cycle detected")
#           slow = slow.next
#           while:
#             lst.append(slow.value)
#             if slow == fast:
#                  break
#             else:
#                 slow = slow.next