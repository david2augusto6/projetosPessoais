# Trabalho Prático 1- AED1- David Augusto de Oliveira e Silva


class Stack:
	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)

	def isEmpty(self):
		return len(self._data) == 0

	def push(self, e):
		self._data.append(e)

	def top(self):
		if len(self._data) == 0:
			raise "Pilha vazia"
		return self._data[-1]

	def pop(self):
		if len(self._data) == 0:
			raise "Pilha Vazia"
		return self._data.pop()


# Entrada
decNum = int(input())
binary = Stack()
t = decNum  # Variável auxiliar

while True:  # Conversão (Decimal => Binário)
	if t == 1 or t == 0:
		rem = t % 2
		binary.push(rem)
		break
	div = t // 2
	resto = t % 2
	binary.push(resto)
	t = div


for n in range(len(binary)):
	print(binary.pop(), end='')
