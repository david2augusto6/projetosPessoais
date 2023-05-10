from TAD.DoublyLinkedList import *

w = input("Palavra: ")

L = DoublyLinkedList()

for n in range(len([i for i in w])):
    if n == len(w) - 1:
        L.insertBeg(w[n])
        break
    L.insertBeg(w[n])

