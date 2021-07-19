entrada = input()
L = [int(x) for x in entrada.split(' ')]

A = L[0]
B = L[1]
C = L[2]
D = L[3]

if B > C and D > A and C + D > A + B and C and D >= 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")