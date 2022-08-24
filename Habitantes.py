A1=int(input("Introduce el numero de habitantes de las puertas de la puerta A1 "))
B1=int(input("Introduce el numero de habitantes de las puertas de la puerta B1 "))
C1=int(input("Introduce el numero de habitantes de las puertas de la puerta C1 "))
D1=int(input("Introduce el numero de habitantes de las puertas de la puerta D1 "))

A2=int(input("Introduce el numero de habitantes de las puertas de la puerta A2 "))
B2=int(input("Introduce el numero de habitantes de las puertas de la puerta B2 "))
C2=int(input("Introduce el numero de habitantes de las puertas de la puerta C2 "))
D2=int(input("Introduce el numero de habitantes de las puertas de la puerta D2 "))

A3=int(input("Introduce el numero de habitantes de las puertas de la puerta A3 "))
B3=int(input("Introduce el numero de habitantes de las puertas de la puerta B3 "))
C3=int(input("Introduce el numero de habitantes de las puertas de la puerta C3 "))
D3=int(input("Introduce el numero de habitantes de las puertas de la puerta D3 "))

A4=int(input("Introduce el numero de habitantes de las puertas de la puerta A4 "))
B4=int(input("Introduce el numero de habitantes de las puertas de la puerta B4 "))
C4=int(input("Introduce el numero de habitantes de las puertas de la puerta C4 "))
D4=int(input("Introduce el numero de habitantes de las puertas de la puerta D4 "))

A5=int(input("Introduce el numero de habitantes de las puertas de la puerta A5 "))
B5=int(input("Introduce el numero de habitantes de las puertas de la puerta B5 "))
C5=int(input("Introduce el numero de habitantes de las puertas de la puerta C5 "))
D5=int(input("Introduce el numero de habitantes de las puertas de la puerta D5 "))

A6=int(input("Introduce el numero de habitantes de las puertas de la puerta A6 "))
B6=int(input("Introduce el numero de habitantes de las puertas de la puerta B6 "))
C6=int(input("Introduce el numero de habitantes de las puertas de la puerta C6 "))
D6=int(input("Introduce el numero de habitantes de las puertas de la puerta D6 "))

edificio=[A1,B1,C1,D1,A2,B2,C2,D2,A3,B3,C3,D3,A4,B4,C4,D4,A5,B5,C5,D5,A6,B6,C6,D6]
puertas=["A1","B1","C1","D1","A2","B2","C2","D2","A3","B3","C3","D3","A4","B4","C4","D4","A5","B5","C5","D5","A6","B6","C6","D6"]

print("La puerta con mas habitantes del edificio es: " , puertas[edificio.index(max(edificio))] )
