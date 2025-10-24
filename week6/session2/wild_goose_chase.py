class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    if clues is None:
        return False
    current = clues

    while current.next:

        if current.next == clues:
            return True
        current = current.next

    return False

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

#UNDERSTAND
 # detecting cycle in singly LL
 # INPUT - head of singly LL
 # OUTPUT - boolean value (True if cycle, else False)
 # Edge case - if clues is None -> return False (can't be circular)
 #           - if LL is only one node -> return False if doesn't point to itself

#PLAN
 # Check edge case - if LL is None return False
 # set current = head (set up for iteration)
 # then begin iteration (while loop)
 # if current.next = head (clues) then return True (circular)
 # else return False