#1
# class Persona:
#     def __init__(self, nombre, apellido, edad, pesolb, tamañoM):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.peso = pesolb
#         self.tamaño = tamañoM

#     def comer(self, desayunokcal, comidakcal, cenakcal):
#         self.desayuno = desayunokcal
#         self.comida = comidakcal
#         self.cena = cenakcal

#     def dormir(self, hora_sueño):
#         self.hora_sueño = hora_sueño

#     def caminar(self, pasosDiarios):
#         self.pasos = pasosDiarios

# paciente = Persona("Juan", "Matos", 25, 170, 2.11)
# print (paciente)

# class Edificio:
#     def __init__(self, pisos, color, alturaM, baseM):
#         self.numeroPisos = pisos
#         self.color = color
#         self.altura = alturaM
#         self.base = baseM

#     def agregarApartamentos (self, numeroApart):
#         self.apartamentosxnivel = numeroApart

#     def agregarCloset (self):
#         pass

#     def agregarGabinetes (self):
#         pass

#     def agregarCont_baños (self):
#         pass

# a1 = Edificio (4, "Aqua", 20, 75 * 50)
# print (a1)

# class Celular:
#     def __init__(self, marca, operador, OS, plan):
#         self.marca = marca
#         self.operador = operador
#         self.sistemaOperativo= OS
#         self.plan = plan

#     def llamar(self):
#         pass

#     def enviarMensajes (self):
#         pass

#     def listenMusic (self):
#         pass

#     def revisarCorreo (self):
#         pass

#     def revisarRedesSociales (self):
#         pass

#     def leerNoticias (self):
#         pass

# note5 = Celular ("Samsung", "Claro", "Android", "Postpago")
# print (note5)

#2
# class Estudiante:
#     def __init__ (self, nombre, apellido, grado, nivel, materia):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.grado = grado
#         self.nivel = nivel
#         self.materia = materia

#     def promedio (self, nota08, nota09, nota10, nota11, exam_final):
#         self.notaAgosto = nota08
#         self.notaSeptiembre = nota09
#         self.notaOctubre = nota10
#         self.notaNoviembre = nota11
#         self.notaExamenFinal = exam_final
#         self.promedio_gral = ((nota08 + nota09 + nota10 + nota11 + exam_final)/5)
#         if self.promedio_gral <= 100:
#             print (self.promedio_gral)
#         else:
#             print ("Hay un error en los datos ingresados, intentelo de nuevo.")

# norberto = Estudiante ("Norberto", "Fadul", 6, "medio", "Lengua Española")
# norberto.promedio(89, 94, 84, 96, 90)

#3
# class Aritmetica:
#     def __init__(self, x, y):
#         self.number1 = x
#         self.number2 = y

#     def sumar(self):
#         self.suma = self.number1 + self.number2
#         print (self.suma)

#     def restar(self):
#         self.resta = self.number1 - self.number2
#         print (self.resta)

#     def multiplicar(self):
#         self.multiplicación = self.number1 * self.number2
#         print (self.multiplicación)

#     def dividir(self):
#         self.división = self.number1 / self.number2
#         print (self.división)


# operaciones_basicas = Aritmetica(144, 12)
# operaciones_basicas.dividir()

#4
# class Personaje:
#     def __init__ (self, papel, escena, pelicula):
#         self.papel = papel
#         self.numero_escena = escena
#         self.nombre_pelicula = pelicula

#     def moverArriba (self, saltar):
#         self.salto = saltar
#         print ("Salto 1 metro")

#     def moverAbajo ():
#         pass

#     def moverDerecha ():
#         pass

#     def moverIzquierda ():
#         pass

# class Mario (Personaje):
#     pass

# mario = Mario ("principal", "todas", "Super Mario Bros")
# mario.moverArriba()

# class Koopa (Personaje):
#     pass

# koopa = Koopa ("segundo", "tercera y cuarta", "Super Mario Bros")
# koopa.moverDerecha()

#5
class Carro:
    def __init__ (self, color, marca, puertas, combustible, galones):
        self.marca = marca
        self.cantidad_ruedas = 4
        self.cantidad_puertas = puertas
        self.tipo_combustible = combustible
        self.galones_combustible = galones 
        self.color = color
        self.encendido = False
    

    def enciende(self):
        if self.galones_combustible > 0:
            print ("enciende ")

    def apagar(self):
        pass

    def acelera(self):
        pass

    def frena(self):
        pass

cAzul = Carro ("azul", "Toyota", 4, "gasolina", 12)
print (cAzul)