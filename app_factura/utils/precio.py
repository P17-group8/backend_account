import math
tarifa = 2000 #por hora y fracción

def precio(tiempo_en_segundos):
    print(tiempo_en_segundos)
    valor = None
    if(tiempo_en_segundos % 3600 == 0):
        valor =  (tiempo_en_segundos / 3600) * tarifa
    else:
        valor = (math.trunc(tiempo_en_segundos/3600) + 1) * tarifa 
    return int(valor)

     