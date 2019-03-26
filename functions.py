# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:42:58 2019

@author: Oliver

This is a documentation that I can, in fact, reverse a binary tree
"""

import random
from node import node

tree = node(0.5)  # the root node of the tree is called tree

for i in range(100):  # add 50 random numbers to tree
    tree.add(random.random())

def recursive_print(root):
    """
    iterate through the nodes in the given root, favoring print left, then
    self, then right
    """
    if root is None:
        return

    if root.left is not None:
        recursive_print(root.left)
    
    print(root.data)

    if root.right is not None:
        recursive_print(root.right)
        
def reverse_tree(root):
    if root is None:
        return None
    tmp = root.left
    root.left = reverse_tree(root.right)
    root.right = reverse_tree(tmp)
    return root
        
recursive_print(tree)
print("""
Performing exceptionally difficult procedure.
Please allow for at least two years of computation time
...
...
...
Thank you for your patience
""")
reverse_tree(tree)
recursive_print(tree)