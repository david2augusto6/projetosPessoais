class Node:
    def __init__(self, key):
        self.data = key
        self.l = None
        self.r = None

# inserir elementos na ABB
def insert(root, key):
    if root is None:
        root = Node(key)
    else:
        if root.data == key:
            return root
        elif root.data > key:
            root.r = insert(root.r, key)
        else:
            root.l = insert(root.l, key)
    return root

# altura da ABB
def altura(root):
    if root is None:
        return 0
    return max(altura(root.l), altura(root.r)) + 1

# estatura = comprimento do maior caminho entre dois nós folhas passando pela raiz
def estatura(root):
    # (altura à direita) + (altura à esquerda) + (nó raiz)
    return altura(root.r) + altura(root.l) + 1 

def preOrder(root):
    if root is not None:
        print(root.data)
        preOrder(root.l)
        preOrder(root.r)

if __name__ == "__main__":
    r = Node(int(input("Raiz: ")))

    x = " "
    while True:
        x = input("Insira um valor: ")
        if x == "": break
        insert(r, int(x))
    print("="*30)
    print(f"Estatura da árvore: {estatura(r)}")