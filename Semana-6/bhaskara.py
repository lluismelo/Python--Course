#Este programa cálcula as raizes. Foi refatorado e agora utiliza funções para melhorar o código
import math

def delta (a,b,c):
    return b**2 - 4*a*c
def main():
    num_a = float(input("Entre com o valor de a: "))
    num_b = float(input("Entre com o valo de b: "))
    num_c = float(input("Entre com o valor de c: "))
    imprime_raizes(num_a,num_b,num_c) #chamando a função e passando os valores digitados pelo User como parâmetro

def imprime_raizes(a,b,c):
    d = delta(a,b,c)

    if (d < 0):
        print("esta equação não possui raízes reais")

    if (d >= 0):
        x1 = ((-b) + math.sqrt(d)) / (2*a)
        x2 = ((-b) - math.sqrt(d)) / (2*a)

    if (d == 0):
            print("a raiz dupla desta equação é", x1)
    if(d>0):
        if(x1>x2):
            print("as raízes da equação são",x2,"e",x1)
        else:
            print("as raízes da equação são",x1,"e",x2)
        