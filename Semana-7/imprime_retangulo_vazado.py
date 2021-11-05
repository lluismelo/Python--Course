#Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
#de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

#Exemplo --> largura = 10 e altura = 3
        #Resultado -->  ##########
                        #        #
                        ##########
#### REFAZER DO ZERO ######
#FUNCIONOU MAIS OU MENOS

largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor da altura: "))

alt=altura
larg=largura

while larg > 0:
    while alt > 0:
        if(alt==altura or alt==1 or larg==1 or larg==largura):
# Este if faz a varredura... Se o ponteiro estiver nas extremidades verticais da tabela (extremidade superior => alt==altura OU extremidade inferior => alt==1) irá escrever #
# Se o ponteiro estiver nas extremidades horizontais da tabela (extremidade esquerda => larg==largura OU extremidade direita => larg==1) também irá escrever #
# O restante sempre será espaço em vazio 
            print("#",end="")
            #larg = larg - 1
        if(alt!=altura and alt!=1):
            print(" ",end="")
        alt = alt - 1
        larg = larg-1
    print("")
    #larg = larg-1
    alt = alt - 1    
    larg = largura












