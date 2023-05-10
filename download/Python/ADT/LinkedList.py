class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList(object):
	def __init__(self, node=None):
		self.size = 0
		self.head = node

	def length(self):
		current = self.head
		count = 0
		while current is not None:
			count += 1
			current = current.next
		return count

	def insertBeg(self, e):
		new = Node()
		new.data = e
		if self.size == 0:
			self.head = new
		else:
			new.next = self.head
			self.head = new
		self.size += 1

	def insertEnd(self, e):
		new = Node()
		new.data = e
		current = self.head
		while current.next is not None:
			current = current.next
		current.next = new
		self.size += 1

	def insert(self, pos, e):
		if 0 > pos > self.size:
			return None
		else:
			if pos == 0:
				self.insertBeg(e)
			else:
				new = Node()
				new.data = e
				count = 1
				current = self.head
				while count < pos - 1:
					count += 1
					current = current.next
				new.next = current.next
				current.next = new
				self.size += 1

	def isEmpty(self):
		return self.length() == 0

	def kill(self):
		self.head = None
		self.size = 0
	
	def delBeg(self):
		if self.length() == 0:
			raise ValueError("Lista vazia")
		else:
			self.head = self.head.next
			self.size -= 1
	
	def delEnd(self):
		if self.isEmpty():
			raise "Lista vazia"
		else:
			now = self.head
			before = self.head
			while now.next is not None:
				before = now
				now = now.next
			before.next = None
			self.size -= 1

	def delNode(self, node):
		if self.isEmpty():
			raise "Lista Vazia"
		else:
			now = self.head
			before = None
			found = False
		while not Found:
			if current == Node:
				found = True
			elif current is None:
				raise "Nó não está na lista"
			else:
				before = now
				now = now.next
		if before is None:
			self.head = now.next
		else:
			before = current.next
		self.size -= 1

	def delValue(self, value):
		now = self.head
		before = self.head

		while now.next != None or now.data != value:
			if now.value == value:
				before.next = now.next
				self.size -= 1
				return
			else:
				before = now
				now = now.next
				