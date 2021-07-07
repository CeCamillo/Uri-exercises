diasVividos = int(input())

ano = diasVividos // 365
saldo = diasVividos % 365

mes = saldo // 30
saldo2 =  saldo % 30

dia = saldo2

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano, mes, dia))