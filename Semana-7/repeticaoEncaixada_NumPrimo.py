def éPrimo (x):
    count = 2
    if x == 2:
        return True
    while x % count !=0 and count <= x/2:
        count +=1
    if x % count == 0:
        return False
    else:
        return True
    

num = int(input("Digite um número inteiro: "))

if (num == 0):
    print("indeterminação")

while num > 0:
    #if (num == 0):
    #    print("indeterminação")
    if éPrimo(num):
        print(num, "é primo! :-)")
    else:
        print(num, "não é primo :-(")
    num = int(input("Digite um número inteiro: "))
    #if (num == 0):
    #    print("indeterminação")