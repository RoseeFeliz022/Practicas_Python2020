#1
# numero = 1
# cantidad = 0
# suma = 0
# while numero != 0:
#     numero = int(input("Ingrese el numero que desee: "))
#     suma = suma + numero
#     cantidad = cantidad + 1

# print(f"Ha marcado 0, sus intentos fueron {cantidad} la suma total es: {suma}")
    
#2
# def Menu():
#     print ("Bienvenido al Menu: 1. Convertir de Celsius a Fahrenheit, 2. Convertir de dolar a pesos, 3. Convertir metros a pies, 4. Salir")


# Menu()
# n = int(input("Ingrese el numero de la opcion deseada: "))
# while n < 4:
#     if n == 1:
#         x= input("Ingrese el grado: ")
#         print((int(x) * 9/5) + 32)
#         Menu()
#         n = int(input("Ingrese el numero de la opcion deseada: "))
#     elif n == 2:
#         y= input("Ingrese el monto: ")
#         print(int(y) * 58.44)
#         Menu()
#         n = int(input("Ingrese el numero de la opcion deseada: "))
#     else:
#         n == 3
#         z= input("Ingrese la medida: ")
#         print(int(z) * 3.281)
#         Menu()
#         n = int(input("Ingrese el numero de la opcion deseada: ")) 

# print("Gracias por usar mi programa")

#3
# n= int(input("Ingrese el numero que desee"))
# d=5
# while  d <= 1000:
#     print(n * d)
#     d += 5


#4
# sueldo= int(input("Ingrese el sueldo: "))
# top1 = 416202.00
# top2 = 624329.00
# top3 = 867123.00
# sueldo_anual= sueldo * 12
# isr = 0;

# if sueldo_anual <= top1:
#     print ("Excento")
# elif sueldo_anual <= top2:
#     excedente = sueldo_anual - top1
#     isr = excedente * 0.15
# elif sueldo_anual <= top3:
#     excedente = sueldo_anual - top2
#     isr= 31216.00 + (excedente * 0.20)
# else:
#     excedente = sueldo_anual - top3
#     isr = 79776.00 + (excedente * 0.25)

# ars= sueldo * 0.0304
# afp= sueldo * 0.0287
 
# print(f"Se descuenta a su sueldo anual {sueldo_anual}: un isr de {isr}, de la ars es de {ars*12} y de la afp es de {afp*12}")

#5
banco = int(input("Bienvenido. Elija el banco de su preferencia: 1. Banco ABC, 2. BanReservas "))
servicio = int(input("Elija el servicio a realizar: 1. Retiro, 2. Transferencia "))
while servicio !=3:
    if servicio == 1:
        carga1000 = 9000
        carga500 = 9500
        carga100 = 9900

        def sacar_dinero(cantidad):
            global carga1000, carga500, carga100
            if cantidad <= 10000:
                de1000 = int(cantidad / 1000)
                cantidad = cantidad % 1000
                if de1000 >= carga1000:
                    cantidad = cantidad + (de1000 - carga1000) * 1000
                    de1000 = carga1000
 
                de500 = int(cantidad / 500)
                cantidad = cantidad % 500
                if de500 >= carga500:
                    cantidad = cantidad + (de500 - carga500) * 500
                    de500 = carga500
 
                de100 = int(cantidad / 100)
                cantidad = cantidad % 100
                if de100 >= carga100:
                    cantidad = cantidad + (de100 - carga100) * 100
                    de100 = carga100
 
                if cantidad == 0:
                    carga1000 = carga1000 - de1000
                    carga500 = carga500 - de500
                    carga100 = carga100 - de100
                    return [de1000, de500, de100]
                else:
                   return [0, 0, 0]
            else:
                return [-1, -1, -1]

        try:
            c = int(input('Ingrese el monto a retirar: '))
            resultado=sacar_dinero(c)
            if resultado==[0,0,0]:
                print ('No hay desglose de billetes')
            elif resultado==[-1,-1,-1]:
                print ('Excede el limite de retiro')
            else:
                print ('Billetes de 1000:', resultado[0])
                print ('Billetes de 500:', resultado[1])
                print ('Billetes de 100:', resultado[2])
        except:
            print ('Importe incorrecto')
    elif servicio == 2:
        transferencia = int(input("Digite el monto a transferir: "))
        if transferencia <= 2000:
            print (f"Ha transferido RD$ {transferencia} pesos. Su transferencia ha sido realizada con éxito")
        else:
            print ("Usted ha excedido el limte de transferencia (2000). Intentelo de nuevo.")
    else:
        print ("Gracias por preferirnos")








