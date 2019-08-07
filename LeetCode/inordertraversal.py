class solution(object):
    '''Morris Inorder traversal '''
    def inordertraversal(self, root):

        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    result.append(curr.val)
                    node.right(None)
                    curr = curr.right
        return result


class TreeNode(object):
    def __init__(self, val=None, lef=None, rit=None):
        self.value = val
        self.left = lef
        self.right = rit