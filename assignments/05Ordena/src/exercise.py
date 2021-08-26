def main():
    # Escribe el código adecuado para completar el programa
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))
z = int(input("Ingresa el tercer número: "))

if x<y<z or x<z<y:
    print (x)

elif y<x<z or y<z<x:
    print (y)

elif z<x<y or z<y<x:
    print (z)

if y<x<z or z<x<y:
    print (x)

elif x<y<z or z<y<x:
    print (y)

elif x<z<y or y<z<x:
    print (z)

if x>y>z or x>z>y:
    print (x)

elif y>x>z or y>z>x:
    print (y)

elif z>x>y or z>y>x:
    print (z)
    pass


if __name__=='__main__':
    main()
