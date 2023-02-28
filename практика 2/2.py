import random
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_helper(self.root, key)

    def _insert_helper(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert_helper(node.left, key)
        else:
            node.right = self._insert_helper(node.right, key)

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, node):
        left_child = node.left
        right_child = left_child.right

        left_child.right = node
        node.left = right_child

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        left_child.height = 1 + max(self._get_height(left_child.left),
                                    self._get_height(left_child.right))

        return left_child

    def _rotate_left(self, node):
        right_child = node.right
        left_child = right_child.left

        right_child.left = node
        node.right = left_child

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        right_child.height = 1 + max(self._get_height(right_child.left),
                                     self._get_height(right_child.right))

        return right_child

    def traverse_in_order(self, node):
        if not node:
            return
        self.traverse_in_order(node.left)
        print(f'{node.key} Balance: {self._get_balance(node)}')
        self.traverse_in_order(node.right)

tree = AVLTree()
tree.insert(random.randint(1, 10000000))
tree.insert(random.randint(1, 10000000))
tree.insert(random.randint(1, 10000000))
tree.insert(random.randint(1, 10000000))
tree.insert(random.randint(1, 10000000))
tree.insert(random.randint(1, 10000000))
tree.insert(random.randint(1, 10000000))

tree.traverse_in_order(tree.root)
