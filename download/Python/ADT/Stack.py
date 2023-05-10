class Stack:

	def __init__(self):
		"""Cria uma pilha vazia"""
		self._data = []

	def __len__(self):
		"""Retorna o tamanho da Pilha"""
		return len(self._data)

	def push(self, e):
		"""Insere um elemento no topo da pilha"""
		self._data.append(e)

	def isEmpty(self):
		"""True = Pilha Vazia; False = Pilha não vazia"""
		return len(self._data) == 0

	def top(self):
		"""Retorna o elemento do topo. Caso a piha esteja vazia, mostra um erro"""
		if len(self._data) == 0:
			raise "Pilha vazia"
		return self._data[-1]

	def pop(self):
		"""Retorna e exclui o elemento do topo"""
		if len(self._data) == 0:
			raise "Pilha Vazia"
		return self._data.pop()
