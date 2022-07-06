#Realice un programa que lea un numero entero y diga si es mayor, menor o igual a 100
respuesta = "S"
while respuesta == "S":
    numero = int(input("Digite un número entero: "))
    if numero > 100:
        print(f"El número es mayor a 100")
    elif numero < 100:
        print(f"El número es menor a 100")
    else:
        print(f"El número es igual a 100")
    respuesta = input('Presiones "S" para continuar o cualquier tecla para salir \n')
    
