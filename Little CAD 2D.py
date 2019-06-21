import math
opcion = int(input("Menu:\n" +
                   "1. Agregar una linea\n"
                   "2. Agregar una elipse o circulo\n"
                   "3. Agregar un rectángulo o cuadrado\n"
                   "4. Agregar un triangulo\n"
                   "0. Salir del programa\n\n" + "Ingrese una opcion: "));
while opcion != 0:
    if opcion == 1:
        for i in range(1,100):
            print("*",end="")
        break
    elif opcion == 2:
        print("")
        break

    elif opcion == 3:
            for i in range(0, 6) :
                print (" ")
                for j in range(0, 6) :
                    if (i == 0 or i == 5 or j== 0 or j == 5) :
                        print("*",end="")
                    else :
                        print(" ",end="")
            break

    elif opcion == 4:
        for i in range(6):
            print(" "*(6-1-i)+"* "*(i+1))
        break
    else:
        print("Ingrese una opcion válida");
        break

print()
def dibujar(radio):
	for i in range((2 * radio)+1):
		for j in range((2 * radio)+1):
			distancia = math.sqrt((i - radio) * (i - radio) +
				(j - radio) * (j - radio))
			if (distancia > radio - 0.5 and distancia < radio + 0.5):
				print("*",end="")
			else:
				print(" ",end="")
		print()
radio = int(input("radio del circulo: "))
dibujar(radio)



