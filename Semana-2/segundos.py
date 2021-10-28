seg = int(input("Por favor, entre com o número de segundos que deseja converter:"))
dia = seg//86400
hora = (seg % 86400)//3600
minuto = (seg % 86400 % 3600)//60
seg_final = (seg % 86400 % 3600 % 60)
print(dia,"dias,",hora,"horas,",minuto,"minutos e",seg_final,"segundos")