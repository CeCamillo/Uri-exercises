roupas1 = input().split()

c1 = int(roupas1[0])
n1 = int(roupas1[1])
v1 = float(roupas1[2])

roupas2 = input().split()

c2 = int(roupas2[0])
n2 = int(roupas2[1])
v2 = float(roupas2[2])

total = (n1 * v1) + (n2 * v2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
