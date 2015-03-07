__author__ = 'Girish'

#31.14 points due to recursion depth exceeding
#pass if uncomment the line
'''
import sys
sys.setrecursionlimit(10000)
'''
class node:
	def __init__(self,data=None):
		self.left =None
		self.right = None
		self.data = data

head = node(1)
temp = head

def add_in_tree(depth,data=None,j=0):
    if data==None:
        data =[head]
    if depth ==j:
        return 0
    else:
        ansli=[]
        for i in data:
            x,y =[int(x) for x in input().split()]
            if x != -1:
                i.left=node(x)
                ansli.append(i.left)
            if y != -1:
                i.right=node(y)
                ansli.append(i.right)
            j+=1
    return 1+add_in_tree(depth,ansli,j)

def inorder_traversal(node):
    if node !=None:
        inorder_traversal(node.left)
        print(node.data,end=" ")
        inorder_traversal(node.right)

def swap_at(depth,max_dp,node=head,j=0):
    if max_dp==j:
        return
    if (j+1)%depth==0:
        t1=node.left
        t2=node.right
        node.left,node.right =node.right,node.left
        if t1 !=None:
            swap_at(depth,max_dp,t1,j+1)
        if t2 !=None:
            swap_at(depth,max_dp,t2,j+1)
    else:
        if node.left!=None:
            swap_at(depth,max_dp,node.left,j+1)
        if node.right!=None:
            swap_at(depth,max_dp,node.right,j+1)




max_dpth= add_in_tree(int(input()))



for i in range(int(input())):
    swap_at(int(input()),max_dpth-1)
    inorder_traversal(head)