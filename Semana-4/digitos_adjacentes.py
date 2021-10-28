#Este programa identifica se um número possui sequência dígitos iguais 
num=int(input('digite um numero: '))

num1 = num

resto1 = num % 10

while (num//10!=0):

       num = num // 10
       resto=num%10

       if resto == resto1:
               print('sim')
               num=num1

               break
       resto1 = resto

if ( (num // 10) == 0):
       print('nao')