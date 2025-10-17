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

def add_first(head, task):
    temp = head
    new_node = Node(task)
    new_node.next = temp
    head = new_node
    return head

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# ^^^^ This creates == shake tree -> dig fossils -> catch bugs

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))

# Plan 
    # create new_node 
    # assign temp to task_1
    # assign new_node to head