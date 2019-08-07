class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
    if not node:
        return True
    
    val = node.val
    if val <= lower or val >= upper:
        return False

    if not helper(node.right, val, upper):
        return False
    if not helper(node.left, lower, val):
        return False
    return True

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(9)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(6)

    print(helper(root))