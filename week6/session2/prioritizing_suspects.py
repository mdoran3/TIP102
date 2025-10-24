class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):

    greater_dummy = Node(0)
    less_equal_dummy = Node(0)

    greater = greater_dummy
    less_equal = less_equal_dummy

    curr = suspect_ratings

    while current:
        
	
suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))