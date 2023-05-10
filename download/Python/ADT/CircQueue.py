class CQueue:
	DEFAULT_CAPACITY = 10

	def __init__(self):
		"""Cria uma fila vazia"""
		self._data = [None] * CQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		"""Retorna o número de elementos na fila"""
		return self._size

	def isEmpty(self):
		"""Retorna True se a fila estiver vazia"""
		return self._size == 0

	def first(self):
		"""
		Retorna sem remover o elemento na frente da fila.
		Caso a fila esteja vazia, mostra um erro
		"""
		if self.isEmpty():
			raise "\033[31mFila vazia\033[m"
		return self._data[self._front]

	def dequeue(self):
		"""
		Remove e retorna o primeiro elemento da fila
		Se a fila estiver vazia, retorna um erro.

		"""
		if self.isEmpty():
			raise "Fila Vazia"
		resp = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		return resp

	def _resize(self, cap): # cap >= len(self)
		"""Reajusta o tamanho para uma lista de capacidade >= len(self)."""
		ant = self._data
		self._data = [None] * cap
		passo = self._front
		for k in range(self._size):
			self._data[k] = ant[passo]
			passo = (1+passo)%len(ant)
		self._front = 0

	def enqueue(self, e):
		"""Adiciona um elemento ao final da fila"""
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
