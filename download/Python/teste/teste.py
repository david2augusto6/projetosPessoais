import numpy as n

def pseudoinverse(x, y):
    return n.matmul(n.matmul(n.transpose(x), x), n.matmul(n.transpose(x), y))

arq1 = open("elevacao.txt", "r")
x = []
for linha in arq1.readlines():
    x.append(int(linha))
arq1.close()

arq2 = open("temperatura.txt", "r")
y=[]
for linha in arq2.readlines():
    y.append(float(linha.replace(",", ".")))
arq2.close()

xm = n.matrix(x)
ym = n.matrix(y)

a = pseudoinverse(xm, ym)

print(n.matmul(ym, a))