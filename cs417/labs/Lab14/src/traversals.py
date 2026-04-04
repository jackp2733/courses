"""
Tree Traversals — Lab 14

Implement four traversal algorithms for a Binary Search Tree.
The BST module is provided — don't modify bst.py.
"""

from bst import BST


def build_sample_tree():
    tree = BST()
    for value in [15, 9, 21, 4, 12, 18, 25, 2, 7]:
        tree.insert(value)
    return tree


# ── Task 1: Explore the BST ─────────────────────────────────────────

def explore():
    tree = build_sample_tree()

    tree.display()

    for val in [12, 20, 25]:
        if tree.search(val):
            print(f"Search {val}: Found")
        else:
            print(f"Search {val}: Not found")

    print(f"Tree has {tree.size()} nodes")


# ── Task 2: Inorder Traversal ───────────────────────────────────────

def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


# ── Task 3: Preorder Traversal ──────────────────────────────────────

def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


# ── Task 4: Postorder Traversal ─────────────────────────────────────

def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


# ── Task 5: Level-Order Traversal ───────────────────────────────────

def levelorder(node):
    if node is None:
        return []

    result = []
    queue = [node]

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    explore()