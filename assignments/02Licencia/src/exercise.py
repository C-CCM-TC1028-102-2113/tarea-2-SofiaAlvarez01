
def main():
    #Escribe tu código debajo de esta línea
import math
edad= int(input("Ingresa tu edad: "))
if edad>=18:
    identificacion= str(input("¿Tienes identificación oficial? (s/n): "))

    if (identificacion== "s"):
        print ("Trámite de licencia concedido")

    elif (identificacion== "n"):
        print ("No cumples requisitos")

    elif (identificacion != "s" != "n"):
        print ("Respuesta incorrecta")        
else:
    print("No cumples con los requisitos")    

pass

if __name__ == '__main__':
    main()
