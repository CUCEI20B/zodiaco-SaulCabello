print("los dias y meses se ingresan en numeros")
dia = int(input("Ingresa dia "))
mes = int(input("Ingresa mes "))
if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12:
    print ("El signo zodiacal es: ")
#ACUARIO
if mes == 1:
   if dia >= 21 and dia <=31:
        print ("acuario")
elif mes == 2:
    if dia >= 1 and dia <= 19:
        print ("acuario")
#PISCIS
if mes == 2:
   if dia >= 20 and dia <=28:
        print ("piscis")
elif mes == 3:
    if dia >= 1 and dia <= 20:
        print ("piscis")
#ARIES 
if mes == 3:
    if dia >= 21 and dia <= 31:
        print ("aries")
elif mes == 4:
    if dia >= 1 and dia <= 19:
        print ("aries")
#TAURO
if mes == 4:
   if dia >= 20 and dia <= 30:
        print ("tauro")
elif mes == 5:
    if dia >= 1 and dia <= 20:
        print ("tauro")
#GEMINIS
if mes == 5:
   if dia >= 21 and dia <= 31:
        print ("geminis")
elif mes == 6:
    if dia >= 1 and dia <= 21:
        print ("geminis")
#CANCER
if mes == 6:
   if dia >= 22 and dia <= 30:
        print ("cancer")
elif mes == 7:
    if dia >= 1 and dia <= 22:
        print ("cancer")
#LEO
if mes == 7:
   if dia >= 23 and dia <= 31:
        print ("leo")
elif mes == 8:
    if dia >= 1 and dia <= 23:
        print ("leo")
#VIRGO
if mes == 8:
   if dia >= 24 and dia <= 31:
        print ("virgo")
elif mes == 9:
    if dia >= 1 and dia <= 22:
        print ("virgo")
#LIBRA
if mes == 9:
   if dia >= 23 and dia <= 30:
        print ("libra")
elif mes == 10:
    if dia >= 1 and dia <= 22:
        print ("libra")
#ESCORPIO
if mes == 10:
   if dia >= 23 and dia <= 31:
        print ("escorpio")
elif mes == 11:
    if dia >= 1 and dia <= 22:
        print ("escorpio")
#SAGITARIO
if mes == 11:
   if dia >= 23 and dia <= 30:
        print ("sagitario")
elif mes == 12:
    if dia >= 1 and dia <= 21:
        print ("sagitario")
#CAPRICORNIO
if mes == 12:
   if dia >= 22 and dia <= 31:
        print ("capricornio")
elif mes == 1:
    if dia >= 1 and dia <= 20:
        print ("capricornio")
if mes > 12 or mes < 1 or dia < 1 or dia > 31:
    print("Dato no valido")