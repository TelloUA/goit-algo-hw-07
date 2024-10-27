# code from lection
import avlnode
    
def min_value(root):
    if root is None:
        return None
    
    if root.left is None:
        return root.key
    else:
        return min_value(root.left)
    
# Driver program to test the above functions
root = None
keys = [12, 15, 10, 11, 8, 5, 18]


for key in keys:
    root = avlnode.insert(root, key)
    
    print("Вставлено:", key)    
    print("AVL-Дерево:")
    print(root)
    print("Мінімальне значення в дереві", min_value(root))
    print('---------------------')

# Delete
keys_to_delete = [5, 8]
for key in keys_to_delete:
    root = avlnode.delete_node(root, key)
    print("Видалено:", key)
    print("Мінімальне значення в дереві", min_value(root))
