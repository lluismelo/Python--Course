#Este programa imprime o fatorial de um número
n = int(input("Digite o valor de n:"))
fat = 1
while n > 1:
    fat = fat * n
    n = n - 1
print (fat)
