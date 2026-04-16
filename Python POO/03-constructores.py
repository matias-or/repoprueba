# Actualmente estoy viendo JS, aprendiendo a manejar objetos, clases, etc.
# La sintaxi es 

class Persona:

    # constructor
    def __init__(self, nombre,anio):
        self.nombre = nombre
        self.anio = anio
    # metodo
    def descripcion(self):
        return f'Nombre: {self.nombre}, Año: {self.anio}'

    def comentario(self, frase):
        return f'{self.nombre} dice: {frase}'

# creo un objeto
doctor = Persona('Jose', 26)

print('Mostrando descripcion:')
print(doctor.descripcion())
print(doctor.nombre)

# usar el objeto dentro de otra función
def numeroXNombre(name):
    # name = input('Ingresar nombre: ')
    if name == 'Jose':
        print(name)
    else:
        print("the name doesn't exists")

numeroXNombre(doctor.nombre)