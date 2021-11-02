#Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
#de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

#Exemplo --> largura = 10 e altura = 3
        #Resultado -->  ##########
                        #        #
                        ##########
#### REFAZER DO ZERO

largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor da altura: "))

alt=altura
larg=largura

larg = largura
while alt > 0:
    while larg > 0:
        if(alt==altura or alt==1):
            #while larg > 0:
            print("#", end="")
            larg = larg - 1
        print("") 
    #if(alt>1 and alt <altura):
     #   if(larg)   
    alt = alt - 1    
    larg = largura 












