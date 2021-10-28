# Este programa mostra se o número é um número primo

num = int(input("Digite um número inteiro: "))

cont = 2
Primo = True

if (num == 0):
    print("indeterminação")

if(num!=0):
    while (cont < num and Primo and num > 0):

        Primo = not ((num % cont) == 0)
        cont += 1
        
    if (Primo):
        print("primo")
    else:
        print("não primo")

