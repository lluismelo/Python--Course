#Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, 
#respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo 
#informado com caracteres '#' na saída.

#Exemplo --> largura = 5 e altura = 5
        #Resultado -->  #####
                        #####

largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor da altura: "))

#não funcionou
while altura >= 1:
    while largura >= 1:
        print("#",end="")
        largura = largura - 1
    altura = altura -1
    print("")

#não funcionou
while largura >= 1:
    print("#", end="")
    largura = largura - 1
    #print("\n")
    if largura < 1:
        print("")
        while altura >= 1:
            print("#", end="")
            altura = altura - 1

