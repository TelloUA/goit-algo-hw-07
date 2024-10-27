# code from lection
import avlnode

def preorder_traversal_sum(root, sum = 0):
    if root:
        sum += root.key
        sum = preorder_traversal_sum(root.left, sum)
        sum = preorder_traversal_sum(root.right, sum)
    return sum

# Driver program to test the above functions
root = None
keys = [12, 15, 10, 19, 17, 5, 21, 6]

for key in keys:
    root = avlnode.insert(root, key)
    
    print("Вставлено:", key)    
    print("AVL-Дерево:")
    print(root)
    print("Сумма значень дерева", preorder_traversal_sum(root))
    print('---------------------')

# Delete
keys_to_delete = [21, 17, 19]
for key in keys_to_delete:
    root = avlnode.delete_node(root, key)
    print("Видалено:", key)
    print("Сумма значень дерева", preorder_traversal_sum(root))

