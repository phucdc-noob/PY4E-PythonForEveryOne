class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None

    def insert(self, node):
        if self.isEmpty():
            self.root = node
            return
        f = None
        p = self.root
        while p is not None:
            if node.key == p.key:
                return
            elif node.key > p.key:
                f = p
                p = p.right
            else:
                f = p
                p = p.left
        if node.key > f.key:
            f.right = node
        else:
            f.left = node

    # return Node that have key or None if no Node with required key
    def search(self, key):
        if self.isEmpty():
            return
        cur = self.root
        while cur is not None:
            if cur.key == key:
                return cur
            if key > cur.key:
                cur = cur.right
            else:
                cur = cur.left
        return

    # find height of tree (or sub-tree, with root is a leaf of main tree)
    '''
    Height |       Tree
    1      |         3
           |       /   \
    2      |     2       5
           |    /       / \
    3      |   1       4   6
           |                \
    4      |                 7
        
        => height(root) or height(search(3)) = 4
        => height(search(2)) also can be called as height(root.left) = height(search(6)) = 2
        => height(search(1)) = height(search(4)) = height(search(7)) = 1
        => height(search(5)) also can be called as height(root.right) = 3
    '''
    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1
    
    # get the level of a node in tree, for example from bellow, node 5 has level 2 (level(Node(5)) = 2), node 7 has level 4 (level(Node(7)) = 4)
    # if you fill in a Node that not exist (level(Node(10))) then it return None
    def level(self, node):
        if node is None:
            return
        cur = self.root
        lv = 0
        while cur is not None:
            if cur.key == node.key:
                return lv + 1
            if node.key > cur.key:
                cur = cur.right
                lv += 1
            else:
                cur = cur.left
                lv += 1
        return

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.key, end = " ")
            self.inOrder(root.right)
    
    def preOrder(self, root):
        if root:
            print(root.key, end = " ")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.key, end = " ")

    # breadth first search or breadth first tranversal or level order tranversal
    def breadthFirstSearch(self):
        cur = self.root
        result = []
        queue = []
        queue.append(cur)
        while len(queue) != 0:
            cur = queue.pop(0)
            result.append(cur.key)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        return result
   
    # real nightmare, delete by copying and delete by merging
    


bt = BinaryTree()
bt.insert(Node(3))
bt.insert(Node(2))
bt.insert(Node(1))
bt.insert(Node(5))
bt.insert(Node(4))
bt.insert(Node(6))
bt.insert(Node(7))
print(*bt.breadthFirstSearch(), sep = ', ')