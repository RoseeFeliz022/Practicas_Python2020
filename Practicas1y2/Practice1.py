#1
print(4<2)
#2
nombre = "Bernardino"
input("Bienvenido " + nombre)
#3
numero = 5
if numero %2 == 0:
    print("par")
else: 
    print("impar")
#4
dos = 2
tres = 3
print(dos > tres)
#5
dolar = 100
tasa = 58.44
peso_dom = dolar * tasa
print(peso_dom)
#6
celsius_grade = 32
fahrenheit_grade = (celsius_grade * 9/5 + 32)
print(fahrenheit_grade)
#7
nota1 = 90
nota2 = 95
nota3 = 77
nota4 = 92
promedio= ((nota1 + nota2 + nota3 + nota4)/4)
if promedio <= 49:
    print("F")
elif promedio <= 59:
    print ("E")
elif promedio <= 69:
    print("D")
elif promedio <= 79:
    print("C")
elif promedio <= 89:
    print("B")
elif promedio <= 100:
    print("A")
else:
    print("Error al calcular el promedio")
#8
monto = 1000000
interes_anual = monto * 0.025
cant_cuotas = 60
cuota_mens = (monto + interes_anual) / cant_cuotas
print (cuota_mens)