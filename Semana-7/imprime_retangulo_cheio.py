#Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, 
#respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo 
#informado com caracteres '#' na saída.

#Exemplo --> largura = 5 e altura = 5
        #Resultado -->  #####
                        #####

largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor da altura: "))

larg = largura
while altura > 0:
    while larg > 0:
        print("#", end="")
        larg = larg - 1
    print("")
    altura = altura - 1    
    larg = largura 