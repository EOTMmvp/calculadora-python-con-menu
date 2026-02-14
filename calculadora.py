print("Calculadora con una sola variable \n")

print("********************")
print("* Menú de opciones *")
print("******************** \n")

print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.Divión entera")
print("6.Exponente")
print("7.Modulo o resto ")
print("8.Raiz cuadrada ")
print("9.Seno ")
print("10.Coseno \n")
import math
Numero = int(input("Introduce la opción deseada: "))

if Numero == 1:
    print("Eligste suma \n")
    Numero = int(input("Introduce el primer número:"))
    Numero += int(input("Introduce el segundo número:"))
    print("El resultado de la suma es:", Numero)

elif Numero == 2:
    print("Eligste resta \n")
    Numero = int(input("Introduce el primer número:"))
    Numero -= int(input("Introduce el segundo número:"))
    print("El resultado de la resta es:", Numero)

elif Numero == 3:
    print("Eligste multiplicación \n")
    Numero = int(input("Introduce el primer número:"))
    Numero *= int(input("Introduce el segundo número:"))
    print("El resultado de la multiplocación es:", Numero)

elif Numero == 4:
    print("Eligste división \n")
    Numero = int(input("Introduce el primer número:"))
    Numero /= int(input("Introduce el segundo número:"))
    print("El resultado de la division es:", Numero)

elif Numero == 5:
    print("Eligste División Entera \n")
    Numero = int(input("Introduce el primer número:"))
    Numero //= int(input("Introduce el segundo número:"))
    print("El resultado de la División Entera es:", Numero)

elif Numero == 6:
    print("Eligste Exponente \n")
    Numero = int(input("Introduce el primer número:"))
    Numero **= int(input("Introduce el segundo número:"))
    print("El resultado del Exponente es:", Numero)

elif Numero == 7:
    print("Eligste resto \n")
    Numero = int(input("Introduce el primer número:"))
    Numero %= int(input("Introduce el segundo número:"))
    print("El resultado del resto es:", Numero)

elif Numero == 8:
    print("Eligste raiz \n")
    Numero = int(input("Introduce el número:"))
    print("El resultado de la raiz es:", math.sqrt(Numero))

elif Numero == 9:
    print("Eligste seno \n")
    Numero = int(input("Introduce el número:"))
    print("El resultado del seno es:", math.sin(Numero))

elif Numero == 10:
    print("Eligste seno \n")
    Numero = int(input("Introduce el número:"))
    print("El resultado del seno es:", math.cos(Numero))


else:
    print ("Esa opción no es valida")
