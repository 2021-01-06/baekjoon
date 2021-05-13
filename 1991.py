# 트리 순회라..

# preorder, inorder, postorder

my_tree = {}

test_num = int(input())

for i in range(test_num):
    mom, left, right = input().split()
    my_tree[mom] = (left, right)

def preorder(mom):
    if mom != '.':
        print(mom, end='')
        preorder(my_tree[mom][0])
        preorder(my_tree[mom][1])

def inorder(mom):
    if mom != '.':
        inorder(my_tree[mom][0])
        print(mom, end='')
        inorder(my_tree[mom][1])

def postorder(mom):
    if mom != '.':
        postorder(my_tree[mom][0])
        postorder(my_tree[mom][1])
        print(mom, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
