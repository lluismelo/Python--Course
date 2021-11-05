
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
    

limite = int(input("Digite o limite máximo: "))
num = 2

while num < limite:
    if éPrimo(num):
        print(num, end=", ")
    num +=1