import math
A, B, C = [float(x) for x in input().split(' ')]

try:
    delta = B*B - 4 * A * C
    R1 = (-B + math.sqrt(delta)) / (2*A)
    R2 = (-B - math.sqrt(delta)) / (2*A)

    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))

except:
    print("Impossivel calcular")