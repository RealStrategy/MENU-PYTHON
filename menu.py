!/usr/bin/python
GREEN = '\033[32m'
#16/02/2023 @RealStrategy
import os
def menu():
os.system('clear')
print (GREEN+"MENU PYTHON V.1")
print("")
print ("1 - Acceder internet satelital")
print ("2 - Hackear la nasa y gobierno")
print ("3 - Ingresar a la deep web")
print ("4 - Hackear el pentagono y area 51")
print ("5 - Ver tarjetas de credito A.E. Centurion")
print ("6 - Esconder direccion IP y Geolocalizacion")
print ("7 - Hackear usuarios de facebook y gmail")
print ("8 - salir")
print("")
while True:
menu()
opcionMenu = input("inserta un numero: ")
if opcionMenu=="1":
print ("")
os.system("ls -a")
input("Presione enter para continuar")
elif opcionMenu=="2":
print ("")
input("Presione enter para continuar")
elif opcionMenu=="3":
print ("")
input("Presione enter para continuar")
elif opcionMenu=="8":
break
else:
print ("")
input("Opción incorrecta…\npulsa una tecla para continuar")
