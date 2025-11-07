from collections import deque 

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
# Problem 1: Monstera Madness
def count_odd_splits(root):
    sum = 0
    
    def helper(root):
        nonlocal sum
        
        if not root:
            return 0
        
        if root.left:
            if root.val % 2 != 0:
                sum += count_odd_splits(root.left) + 1
            else:
                sum += count_odd_splits(root.left)
        
        if root.right:
            if root.val % 2 != 0:
                sum += count_odd_splits(root.right) + 1
            else:
                sum += count_odd_splits(root.right)
    helper(root)
    return sum


"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

# UNDERSTAND
    # Traverse every node
    # check if the value contained in the node is odd
    # return the number of nodes that have odd val

# PLANNING
    # check first for empty BST
        #if empty return 0
    
    # Check if val in Node is odd
        # if yes, return 1
    
    # Check left and right node
        # if left, recurse
        # if right, recurse

# IMPLEMENT