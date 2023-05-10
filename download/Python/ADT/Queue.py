class Queue:

	def __init__(self):
		"""Inicializa uma fila vazia."""
		self._data = []

	def enqueue(self, e):
		"""Adiciona um elemento ao fim da fila."""
		self._data.append(e)

	def dequeue(self):
		"""Se a fila não estiver vazia, retorna e remove o primeiro elemento da fila.
		Caso contrário, mostra um erro."""
		if len(self._data) == 0:
			raise "\033[31mPilha Vazia\033[39m"
		else:
			return self._data.pop(0)

	def first(self):
		"""Se a fila não estiver vazia, retorna, mas não remove, o primeiro elemento da fila.
		Caso contrário, mostra um erro."""
		if len(self._data) == 0:
			raise "\033[31mPilha Vazia\033[39m"
		else:
			return self._data[0]

	def isEmpyt(self):
		"""Retorna True se a fila for vazia ou False se a fila não for vazia."""
		return len(self._data) == 0

	def __len__(self):
		"""Retorna o tamanho da fila."""
		return len(self._data)
