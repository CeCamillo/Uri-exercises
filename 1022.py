
L=[]
for x in range(4):
    L.append(input())

if (L[1] > L[2]) and (L[3] > L[0]) and ((L[2] + L[3]) > (L[0] + L[1])) and (L[2],L[3] > 0) and (L[0] % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
