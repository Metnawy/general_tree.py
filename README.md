

# General Tree Implementation in Python

This repository contains a Python implementation of a **general tree** data structure. A general tree is a hierarchical data structure where each node can have an arbitrary number of child nodes. This implementation provides a flexible and efficient way to manage tree structures, with support for various operations such as adding, deleting, and searching nodes, as well as merging and extracting subtrees.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Classes and Methods](#classes-and-methods)
4. [Usage](#usage)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

---

## Overview

A **general tree** is a tree data structure where each node can have zero or more child nodes. This implementation provides a flexible and efficient way to manage such trees, with support for various operations like adding, deleting, and searching nodes, as well as merging and extracting subtrees.

The implementation is designed to be **type-safe**, ensuring that all nodes in the tree maintain consistent data types. It also provides methods for traversing the tree (breadth-first and depth-first), calculating tree statistics, and performing advanced operations like merging and extracting subtrees.

---

## Features

- **Node Management**: Add, delete, and search nodes in the tree.
- **Type Safety**: Ensures that all nodes in the tree maintain consistent data types.
- **Tree Traversal**: Supports breadth-first and depth-first traversal.
- **Subtree Operations**: Merge and extract subtrees with or without modifying the original tree.
- **Tree Statistics**: Calculate tree height, level, and other statistics.
- **Iterable**: The tree can be iterated over using Python's `for` loop.
- **Error Handling**: Robust error handling for edge cases like empty trees or type mismatches.

---

## Classes and Methods

### 1. **`general_tree`**
   - The main class representing the general tree.
   - **Methods**:
     - `add_to_root_childern(data)`: Adds a new node to the root's children.
     - `add_to_child_no_depth_index(data, index)`: Adds a child to a specific node without depth.
     - `add_to_child_with_depth_index(data, index)`: Adds a child to a specific node with depth.
     - `delete_root_son_index(root, index)`: Deletes a child of the root by index.
     - `delete_root_son_value(root, value)`: Deletes a child of the root by value.
     - `delete_position(position)`: Deletes a node at a specific position.
     - `breadth_first_search(node)`: Performs a breadth-first search starting from a node.
     - `depth_first_search_pre_order(node)`: Performs a depth-first search in pre-order.
     - `depth_first_search_post_order(node)`: Performs a depth-first search in post-order.
     - `merge_without_change(second, mood, start)`: Merges two trees without modifying the original.
     - `merge_with_change(second, mood, start)`: Merges two trees, modifying the original.
     - `extract_subtree_with_change_by_position(position)`: Extracts a subtree by position, modifying the original tree.
     - `extract_subtree_without_change_by_position(position)`: Extracts a subtree by position without modifying the original tree.
     - `is_equivilant(second)`: Checks if two trees are equivalent.
     - `is_superset(second)`: Checks if the current tree is a superset of another tree.
     - `is_subset(second)`: Checks if the current tree is a subset of another tree.

### 2. **`tree_node`**
   - A nested class representing a node in the tree.
   - **Methods**:
     - `add_child(data)`: Adds a child node.
     - `delete_child_index(index)`: Deletes a child node by index.
     - `delete_child_value(value)`: Deletes a child node by value.
     - `size_childern()`: Returns the number of children.
     - `childern()`: Returns the list of children.

### 3. **`_position`**
   - A nested class representing a position in the tree.
   - **Methods**:
     - `__repr__()`: Returns a string representation of the position.
     - `__eq__(second)`: Checks if two positions are equal.
     - `__lt__(second)`: Checks if one position is less than another.

---

## Usage

To use the general tree implementation, simply import the `general_tree` class and create an instance of it:

```python
from general_tree import general_tree

# Create a new tree
tree = general_tree()

# Add nodes to the tree
tree.add_to_root_childern(10)
tree.add_to_root_childern(20)

# Add children to a specific node
tree.add_to_child_no_depth_index(30, 0)

# Traverse the tree
print(tree.breadth_first_search(tree.root))

# Merge two trees
another_tree = general_tree()
another_tree.add_to_root_childern(40)
tree.merge_with_change(another_tree, "value", 10)

# Extract a subtree
subtree = tree.extract_subtree_without_change_by_value(20)
```

---

## Examples

### Example 1: Basic Tree Operations
```python
from general_tree import general_tree

# Create a tree
tree = general_tree()

# Add nodes to the root
tree.add_to_root_childern(10)
tree.add_to_root_childern(20)

# Add children to a specific node
tree.add_to_child_no_depth_index(30, 0)

# Print the tree
tree.the_tree(tree.root)
```

### Example 2: Tree Traversal
```python
from general_tree import general_tree

# Create a tree
tree = general_tree()

# Add nodes to the root
tree.add_to_root_childern(10)
tree.add_to_root_childern(20)

# Perform breadth-first search
print(tree.breadth_first_search(tree.root))

# Perform depth-first search (pre-order)
print(tree.depth_first_search_pre_order(tree.root))
```

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

