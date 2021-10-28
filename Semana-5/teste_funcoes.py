# Este programa serve para testar pedaços de códigos

#def total_Caracteres (x, y, z):
#    return len(x)+len(y)+len(z)
#print(total_Caracteres("abc","abc","abc"))

#def leitura(x = int(input("Digite o valor: "))):
    
#    while x <= 0:
#        x = int(input("Digite um valor: "))
#    return x
#print(leitura())


#def leitura():
 #   x = -1
 #   while x > 0:
  #      x = int(input("Digite um valor: "))
  #  return x
#print(leitura())

def maior_primo(n):
    for c in range(n, 1, -1):
        if primo(c):
            return c


def primo(m):
    i = 1
    cont = 0
    while i <= m:
        if m % i == 0:
            cont += 1
        i += 1
        if cont > 2:
            return False
    return True


num = int(input('Digite um número inteiro maior que "1": '))

print(f'O maior número primo menor ou igual a "{num}" é: {maior_primo(num)}')