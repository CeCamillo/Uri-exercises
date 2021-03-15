entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

pi = 3.14159

triangulo = (a * c) / 2
circulo = pi * c**2
trapezio = ((b + a) * c) / 2
quadrado = b * b
retangulo = a * b

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))
