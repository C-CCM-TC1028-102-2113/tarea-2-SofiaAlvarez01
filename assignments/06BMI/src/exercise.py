def main():
    #escribe tu código abajo de esta línea
    import math
peso = float(input("Peso en kg: "))
altura = float(input("Altura en m: "))

if peso>0 and altura>0:
    índice= (peso)/(altura**2)
    if índice<20:
        print ("PESO BAJO")
    elif 20 <= índice < 25:
        print ("NORMAL")
    elif 25 <= índice < 30:
        print ("SOBREPESO")
    elif 30 <= índice < 40:
        print ("OBESIDAD")
    elif índice >= 40:
        print ("OBESIDAD MORBIDA")


else:
    print("Revisa tus datos, alguno de ellos es erróneo.")

    pass
if __name__=='__main__':
    main()
