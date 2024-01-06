
class Personaje:
    #def __init__ es para inicializar los atributos del personaje
    def __init__(self, nombre, fuerza, vida, inteligencia, defensa):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__vida = vida
        self.__inteligencia = inteligencia
        self.__defensa = defensa
 #def atributos es para mostrar los atributos del personaje
    def atributos(self):
        print(self.__nombre, ":", sep="")
        print("Fuerza:", self.__fuerza)
        print("Vida:", self.__vida)
        print("Inteligencia:", self.__inteligencia)
        print("Defensa:", self.__defensa)


# def subir_nivel es para subir los atributos del personaje
def subir_nivel(self , fuerza, inteligencia, defensa):
    self.__fuerza = self.__fuerza + fuerza
    self.__inteligencia = self.__inteligencia + inteligencia
    self.__defensa = self.__defensa + defensa

#esta_vivo es para saber si el personaje esta vivo o no
def esta_vivo(self):
    return self.__vida > 0

#def morir es para que el personaje muera
def __morir(self):
    self.__vida = 0
    print("El personaje ha muerto")

 #def daño es para calcular el daño que hace el personaje
def daño(self, enemigo):
    return self.__fuerza - enemigo.__fuerza

 #def atacar es para que el personaje ataque al enemigo
def atacar(self, enemigo):
    daño = self.daño(enemigo)
    enemigo.__vida = enemigo.__vida - daño
    print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
    if enemigo.esta_vivo():
       print("La vida de", enemigo.__nombre, "es", enemigo.__vida)
    else:
        enemigo.__morir()


mi_personaje = Personaje("Arthur", 10, 100, 5, 5)
mi_enemigo = Personaje("Mordred", 8, 100, 5, 3)


mi_personaje.atacar(mi_enemigo)
