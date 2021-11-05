#Esse programa recebe uma sequência de dígitos e coloca em uma lista. Se digitar zero (0)
#o loop finaliza e acontece uma inversão na lista e ela é impressa do final para o início
num = int(input("Digite um número inteiro: "))
lista = []
exit = False
while not exit:
    lista.append(num)
    num = int(input("Digite um número inteiro: "))
    if(num == 0):
        lista.append(num)
        exit = True
lista.reverse()
print(lista)