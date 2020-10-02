import sqlite3
class Person:
    def __init__(self, Name, Number):
        self.Name = Name
        self.Number = Number


#Participantes: Ruddy De Gracia, Ramona Sencion, Rosee Féliz
conn = sqlite3.connect("listadecontactos.db")

cursor = conn.cursor()

query1 = """ 
CREATE TABLE Contactos (contactId integer primary key autoincrement, contactName text, contactNumber integer);
"""

def insertar(p):
    with conn:
        cursor.execute(""" INSERT INTO Contactos VALUES (NULL,?,?) """, (p.Name,p.Number))
        print ("Usted ha agregado este contacto nuevo " + p.Name, p.Number)


def mostrar():
    with conn:
        cursor.execute(""" SELECT * FROM Contactos """)
        r = cursor.fetchall()
        print(r)


def buscar(a3):
    with conn:
        cursor.execute(""" SELECT * FROM Contactos WHERE contactId = ? """, (a3,))
        r = cursor.fetchall()
        print(r)

def actualizar(a4,a5):
    with conn:
        cursor.execute(""" UPDATE Contactos SET contactNumber = ? WHERE contactId = ? """, (a5, a4))


def eliminar(a6):
    with conn:
        cursor.execute(""" DELETE FROM Contactos WHERE contactId = ? """, (a6,))


c = 0
def imprimir_texto():
    print ("1. Agregar contacto nuevo, 2. Ver lista de contactos, 3.Buscar contacto, 4. Actualizar contacto, 5. Borrar contacto, 6.Salir: ")
    global c
    c = int(input())
    print ("Su ultima elección fue: " + str(c))


imprimir_texto()
def menu():
    #print ("1. Agregar contacto nuevo, 2. Ver lista de contactos, 3.Buscar contacto, 4. Actualizar contacto, 5. Borrar contacto, 6.Salir: ")
    #imprimir_texto()
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
# cursor.execute(query3)

# result = cursor.fetchall()
# print(result)

# conn.commit()

# conn.close()