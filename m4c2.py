class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas
    
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f"Datos del automóvil: {super().__str__()}, {self.velocidad} Km/h, {self.cilindrada}cc"

# Solicitar la cantidad de vehículos al usuario
cantidad_vehiculos = int(input("¿Cuántos vehículos desea insertar? "))

vehiculos = []

# Solicitar los datos de cada automóvil
for i in range(cantidad_vehiculos):
    print(f"\nDatos del automóvil {i+1}")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    num_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en Km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))

    automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
    vehiculos.append(automovil)

# Imprimir los vehículos por pantalla
print("\nImprimiendo por pantalla los vehículos:")
for i, vehiculo in enumerate(vehiculos):
    print(f"Datos del automóvil {i+1}: {str(vehiculo)}")

# **********
#    codificando la segunda parte ****************

# Definición de las clases
class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.puestos = puestos

    def __str__(self):
        return f"{super().__str__()}, Puestos: {self.puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"{super().__str__()}, Carga: {self.carga} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

# Creación de las instancias
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# Impresión de las instancias
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

# Verificación de las relaciones de la instancia de motocicleta con otras clases
print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))

# **********
#    codificando la tercera parte ****************
#  Nota: Me he tomado la libertad de tomar esta tercera parte de forma mas personalizada
#  he tratado de integrar la funcionalidad de la parte 1 2 y 3 y tratar de entregar
#  algo mas coherente, segun mi criterio. pero siempre siguiendo la rubrica de evaluacion.

import csv


class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def get_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Número de ruedas: {self.nro_ruedas}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"


class Particular(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def get_info(self):
        return super().get_info() + f", Número de puestos: {self.nro_puestos}"


class Carga(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def get_info(self):
        return super().get_info() + f", Carga: {self.carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo, velocidad="", cilindrada=""):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.tipo = tipo

    def get_info(self):
        return super().get_info() + f", Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def get_info(self):
        return super().get_info() + f", Motor: {self.motor}, Cuadro: {self.cuadro}, Número de radios: {self.nro_radios}"


class VehiculoManager:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar_datos_csv(self, vehiculos):
        try:
            with open(self.archivo, 'w', newline='') as file:
                writer = csv.writer(file)
                for vehiculo in vehiculos:
                    writer.writerow([type(vehiculo).__name__, str(vehiculo.__dict__)])
            print("Datos guardados correctamente en el archivo vehiculos.csv")
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")

    def leer_datos_csv(self):
        try:
            vehiculos = {
                'Particular': [],
                'Carga': [],
                'Bicicleta': [],
                'Motocicleta': []
            }
            with open(self.archivo, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    tipo_vehiculo = row[0]
                    atributos = eval(row[1])
                    if tipo_vehiculo == 'Particular':
                        vehiculo = Particular(**atributos)
                        vehiculos['Particular'].append(vehiculo)
                    elif tipo_vehiculo == 'Carga':
                        vehiculo = Carga(**atributos)
                        vehiculos['Carga'].append(vehiculo)
                    elif tipo_vehiculo == 'Bicicleta':
                        vehiculo = Bicicleta(**atributos)
                        vehiculos['Bicicleta'].append(vehiculo)
                    elif tipo_vehiculo == 'Motocicleta':
                        motor=atributos.pop('motor','')
                        vehiculo = Motocicleta(marca=atributos['marca'],modelo=atributos['modelo'], nro_ruedas=atributos['nro_ruedas'], tipo=atributos['tipo'], motor=motor, cuadro=atributos['cuadro'], nro_radios=atributos['nro_radios'])
                        vehiculos['Motocicleta'].append(vehiculo)
            return vehiculos
        except Exception as e:
            print(f"Error al leer los datos del archivo: {e}")


# Crear vehículos
particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# Guardar vehículos en archivo CSV
vehiculos = [particular, carga, bicicleta, motocicleta]
manager = VehiculoManager("vehiculos.csv")
manager.guardar_datos_csv(vehiculos)

# Leer vehículos del archivo CSV y mostrar información
vehiculos_recuperados = manager.leer_datos_csv()

print("Lista de Vehiculos Particular:")
for vehiculo in vehiculos_recuperados['Particular']:
    print(vehiculo.get_info())

print("\nLista de Vehiculos Carga:")
for vehiculo in vehiculos_recuperados['Carga']:
    print(vehiculo.get_info())

print("\nLista de Vehiculos Bicicleta:")
for vehiculo in vehiculos_recuperados['Bicicleta']:
    print(vehiculo.get_info())

print("\nLista de Vehiculos Motocicleta:")
for vehiculo in vehiculos_recuperados['Motocicleta']:
    print(vehiculo.get_info())

#  Solo para para cumplir con la rubrica 4 que dice: 
# "Bosqueja un diagrama de clases para representar el problema distinguiendo clases, atributos, métodos y relación entre clases"

# Clases:
# 0.	Clase Vehiculo
# •	Atributos:
# •	marca (tipo: str)
# •	modelo (tipo: str)
# •	nro_ruedas (tipo: int)
# •	Métodos:
# •	get_info() (tipo: str)

# 1.	Clase Automovil (subclase de vehículo)
# •	Atributos adicionales:
# •	velocidad (tipo: int)
# •	cilindrada (tipo: int)
# •	Métodos:
# •	get_info() (tipo: str)

# 2.	Clase Particular (subclase de Automovil)
# •	Atributos adicionales:
# •	nro_puestos (tipo: int)
# •	Métodos adicionales:
# •	get_info() (tipo: str)

# 3.	Clase Carga (subclase de Automovil)
# •	Atributos adicionales:
# •	carga (tipo: int)
# •	Métodos adicionales:
# •	get_info() (tipo: str)

# 4.	Clase Bicicleta (subclase de Vehiculo)
# •	Atributos adicionales:
# •	tipo (tipo: str)
# •	Métodos adicionales:
# •	get_info() (tipo: str)

# 5.	Clase Motocicleta (subclase de Bicicleta)
# •	Atributos adicionales:
# •	motor (tipo: str)
# •	cuadro (tipo: str)
# •	nro_radios (tipo: int)
# •	Métodos adicionales:
# •	get_info() (tipo: str)

# 6.	Clase VehiculoManager
# •	Atributos:
# •	archivo (tipo: str)
# •	Métodos:
# •	guardar_datos_csv(vehiculos) (tipo: None)
# •	leer_datos_csv() (tipo: dict)

# Relaciones:
# •	Particular, Carga, Bicicleta, y Motocicleta son subclases de la clase base Vehiculo, lo que indica una relación de herencia.
# •	Motocicleta es una subclase de Bicicleta, lo que indica una relación de herencia adicional.
# •	VehiculoManager interactúa con las demás clases para gestionar la carga y lectura de datos desde y hacia un archivo CSV, lo que indica una relación de dependencia entre VehiculoManager y las demás clases.

# ahora el dibujo que representa lo anteriormente descrito:

# +-----------------------+
# |     Vehiculo          |
# +-----------------------+
# | - marca: str          |
# | - modelo: str         |
# | - nro_ruedas: int     |
# +-----------------------+
# | + get_info(): str     |
# +--------------------- -+
#           ^           ^
#           |           |
#           |           |
# +----------------+   +----------------+          +-------------------+
# |   Automovil    |   |    Bicicleta   |          |   Motocicleta     |
# +----------------+   +----------------+          +-------------------+
# |- velocidad:str |   | - tipo: str    |          | - motor: str      |
# |- cilindrada:str|   +----------------+ <------- | - cuadro: str     |
# +----------------+   |+ get_info():str|          | - nro_radios: int |
# |+ get_info():str|   +----------------+          +-------------------+
# +-------------- -+                               |+ get_info():str   |  
#      ^        ^                                  +-------------------+ 
#      |        |______________________
#      |                               |
# +------------------+         +------------------+   
# |    Particular    |         |      Carga       |
# +------------------+         +------------------+   
# |- nro_puestos: str|         | - carga: str     |
# +------------------+         +------------------+   
# | + get_info(): str|         | + get_info(): str|
# +------------------+         +------------------+   






