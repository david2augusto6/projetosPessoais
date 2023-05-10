class _BinTreeNode:
    """Gerador de nós para Árvores Binárias"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preFixTrav(subt):
        """Caminhamento pré-fixado"""
        if subt is not None:
            print(subt.data)
            preFixTrav(subt.left)
            preFixTrav(subt.right)
    
    def centralTrav(subt):
        """Caminhamento central"""
        if subt is not None:
            centralTrav(subt.left)
            print(subt.data)
            centralTrav(subt.right)
    
    def posFixTrav(subt):
        """Caminhamento pós-fixado"""
        if subt is not None:
            posFixTrav(subt.left)
            posFixTrav(subt.right)
            print(subt.data)
    
    def widthTrav(bintree):
        """Caminhamento por largura"""
        import Queue
        q = Queue()
        q.enqueue(bintree)

        while not q.isEmpty():
            node = q.dequeue()
            print(node.data)
        
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
