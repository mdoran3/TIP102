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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
kk_slider.next = harriet
saharah = Node("Saharah")
harriet.next = saharah
isabelle = Node("Isabelle")
saharah.next = isabelle

print_linked_list(kk_slider)

# Understand
 # link the nodes together in LL