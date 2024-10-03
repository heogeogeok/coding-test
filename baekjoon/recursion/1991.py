n = int(input())
tree = {}

for _ in range(n):
    parent, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[parent] = [left, right]


def preorder(node):
    if node is None:
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node is None:
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])

def postorder(node):
    if node is None:
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
