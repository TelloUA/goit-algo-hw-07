# code from lection
import avlnode

def max_value(root):
    if root is None:
        return None

    if root.right is None:
        return root.key
    else:
        return max_value(root.right)
    
# Driver program to test the above functions
root = None
keys = [12, 15, 10, 19, 17, 5, 21, 6]


for key in keys:
    root = avlnode.insert(root, key)
    
    print("Вставлено:", key)    
    print("AVL-Дерево:")
    print(root)
    print("Максимальне значення в дереві", max_value(root))
    print('---------------------')

# Delete
keys_to_delete = [21, 17, 19]
for key in keys_to_delete:
    root = avlnode.delete_node(root, key)
    print("Видалено:", key)
    print("Максимальне значення в дереві", max_value(root))
    # print("AVL-Дерево:")
    # print(root)

    
