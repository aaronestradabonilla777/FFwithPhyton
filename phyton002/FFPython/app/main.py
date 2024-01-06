
class Personaje:
    def __init__(self, nombre, fuerza, vida, inteligencia, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida
        self.inteligencia = inteligencia
        self.defensa = defensa

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza:", self.fuerza)
        print("Vida:", self.vida)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
# def subir_nivel es para subir los atributos del personaje
def subir_nivel(self):
    self.fuerza = self.fuerza + fuerza
    self.inteligencia = self.inteligencia + inteligencia
    self.defensa = self.defensa + defensa

#esta_vivo es para saber si el personaje esta vivo o no
def esta_vivo(self):
    return self.vida > 0
#def morir es para que el personaje muera
def morir(self):
    self.vida = 0
    print("El personaje ha muerto")

def daño(self, enemigo):
    return self.fuerza - enemigo.defensa

def atacar(self, enemigo):
    daño = self.daño(enemigo)
    enemigo.vida = enemigo.vida - daño
    print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
    print("La vida de", enemigo.nombre, "es", enemigo.vida)


mi_personaje = Personaje("Arthur", 10, 100, 5, 5)
mi_personaje.atributos()



