import random
RED = True
BLACK = False

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = RED

class RedBlackTree:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False
        return node.color == RED

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        return x

    def flip_colors(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.root.color = BLACK

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            node.key = key

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def is_valid(self):
        def is_valid_node(node):
            if node is None:
                return True
            if self.is_red(node.right) and not self.is_red(node.left):
                return False
            if self.is_red(node.left) and self.is_red(node.left.left):
                return False
            if self.is_red(node.left) and self.is_red(node.right):
                return False

            left_black_height = is_valid_node(node.left)
            right_black_height = is_valid_node(node.right)

            if left_black_height is False or right_black_height is False:
                return False
            if left_black_height != right_black_height:
                return False
            return left_black_height + (1 if node.color == BLACK else 0)

        if self.root is None:
            return True

        if self.is_red(self.root.left) or self.is_red(self.root.right):
            return False

        black_height = is_valid_node(self.root)
        if black_height is False:
            return False
        return True
rbt = RedBlackTree()

# Добавляем узлы
rbt.insert(random.randint(1, 1000000000))
rbt.insert(random.randint(1, 1000000000))
rbt.insert(random.randint(1, 1000000000))
rbt.insert(random.randint(1, 1000000000))
rbt.insert(random.randint(1, 1000000000))
rbt.insert(random.randint(1, 1000000000))
rbt.insert(random.randint(1, 1000000000))

# Проверяем свойства красно-черного дерева
print(rbt.is_valid()) # True

# Попробуем добавить узел с уже существующим ключом
rbt.insert(random.randint(1, 1000000000))

# Проверяем свойства красно-черного дерев
