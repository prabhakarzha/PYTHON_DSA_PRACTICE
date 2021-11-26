class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Return a list containing the inorder traversal of the given tree
    def preOrder(self,root):
        ans=[]
        stack=[root]
        while stack:
            process=stack.pop()
            if process:
                ans.append(process.data)
                stack.append(process.right)
                stack.append(process.left)
        return ans