from typing import Optional, List


class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1

    def __repr__(self):
        return f"AVLNode({self.key})"



class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def get_height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def update_height(self, node: AVLNode):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def balance_factor(self, node: Optional[AVLNode]) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def _insert(self, node: Optional[AVLNode], key: int) -> AVLNode:
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  

        self.update_height(node)
        bf = self.balance_factor(node)

        if bf > 1 and key < node.left.key:
            return self.rotate_right(node)
        if bf < -1 and key > node.right.key:
            return self.rotate_left(node)
        if bf > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if bf < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, key: int):
        self.root = self._insert(self.root, key)

    def inorder(self, node: Optional[AVLNode]) -> List[int]:
        if not node:
            return []
        return self.inorder(node.left) + [node.key] + self.inorder(node.right)

    def preorder(self, node: Optional[AVLNode]) -> List[int]:
        if not node:
            return []
        return [node.key] + self.preorder(node.left) + self.preorder(node.right)
def insert_from_file_into_avl(filename: str) -> AVLTree:
    avl = AVLTree()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                avl.insert(int(line))
    return avl


if __name__ == "__main__":
    avl = insert_from_file_into_avl("datos.txt")

    print("Altura del árbol:", avl.root.height if avl.root else 0)
    print("Recorrido inorden:", avl.inorder(avl.root))
    print("Recorrido preorden:", avl.preorder(avl.root))