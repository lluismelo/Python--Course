import math
xA = float(input("Digite a coordenada x do ponto A: "))
yA = float(input("Digite a coordenada y do ponto A: "))

xB = float(input("Digite a coordenada x do ponto B: "))
yB = float(input("Digite a coordenada y  do ponto B: "))

dist = math.sqrt((xB-xA)**2 + (yB-yA)**2)
if(dist>=10):
    print("longe")
else:
    print("perto")