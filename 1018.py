valor = int(input())

n100 = valor // 100
r = valor % 100

n50 = r // 50
r = r % 50

n20 = r // 20
r = r % 20

n10 = r // 10
r = r % 10

n5 = r // 5
r = r % 5

n2 = r // 2
r = r % 2

n1 = r // 1
r = r % 1

print(valor)
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))