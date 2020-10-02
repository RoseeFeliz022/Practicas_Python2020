import sqlite3
# class Person:
#     def __init__(self, Name, Number):
#         self.Name = Name
#         self.Number = Number


conn = sqlite3.connect("Agenda.db")

cursor = conn.cursor()

# query1 = """ 
# CREATE TABLE Agenda (contactId integer primary key autoincrement, contactName text, contactNumber integer);
# """

# query2 = """
# INSERT INTO Agenda VALUES (NULL,'Juan',1234567890),
# (NULL,'Maria',9876543210),(NULL, 'Pedro',4861237530),
# (NULL,'Lea',4265897310), (NULL, 'Luis',1534867590),
# (NULL,'Alexa',1597534299),(NULL,'Gilbert',7418529630),
# (NULL,'Lenny',9639518427), (NULL,'Mark',7412589630),
# (NULL,'Pedro',5556783451);;
# """

# query3 = """
# SELECT * FROM Agenda;
# """

# query4 = """
# SELECT * FROM Agenda WHERE contactId= 11;
# """

# query5 = """
# UPDATE Agenda SET contactName = 'Reid', contactNumber = 1597534862 WHERE contactId = 2;
# """

# query6 = """
# DELETE FROM Agenda WHERE contactId = 12;
# """

# cursor.execute(query3)

# result = cursor.fetchall()
# print(result)

def insertar(p):
    with conn:
        cursor.execute(""" INSERT INTO Agenda VALUES (NULL,?,?) """, (p.Name,p.Number))
        print ("Usted ha agregado este contacto nuevo " + p.Name, p.Number)


def mostrar():
    with conn:
        cursor.execute(""" SELECT * FROM Agenda """)
        r = cursor.fetchall()
        print(r)


def buscar(a3):
    with conn:
        cursor.execute(""" SELECT * FROM Agenda WHERE contactId = ? """, (a3,))
        r = cursor.fetchall()
        print(r)

def actualizar(a4,a5):
    with conn:
        cursor.execute(""" UPDATE Agenda SET contactNumber = ? WHERE contactId = ? """, (a5, a4))


def eliminar(a6):
    with conn:
        cursor.execute(""" DELETE FROM Agenda WHERE contactId = ? """, (a6,))


c = 0
def imprimir_texto():
    print ("1. Agregar contacto nuevo, 2. Ver lista de contactos, 3.Buscar contacto, 4. Actualizar contacto, 5. Borrar contacto, 6.Salir: ")
    global c
    c = int(input())
    print ("Su ultima elección fue: " + str(c))


imprimir_texto()
def menu():
    global c
    if c == 1:
        a1 = input("Escriba el nombre: ")
        a2 = int(input("Escriba el numero: "))
        p = Person(a1,a2)
        insertar(p)
        imprimir_texto()
    elif c == 2:
        mostrar()
        imprimir_texto()
    elif c == 3:
        a3 = int(input("Ingrese el Id del contacto: "))
        buscar(a3)
        imprimir_texto()
    elif c == 4:
        a4 = int(input("Ingrese el Id del contacto: "))
        a5 = int(input("Ingrese el nuevo numero del contacto: "))
        actualizar(a4,a5)
        imprimir_texto()
    elif c == 5:
        a6 = int(input("Ingrese el Id del contacto: "))
        eliminar(a6)
        imprimir_texto()
    elif c == 6:
        print ("Usted ha salido de la agenda")




while c != 6:
    menu()

conn.commit()

conn.close()