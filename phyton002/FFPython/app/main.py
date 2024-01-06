
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

mi_personaje = Personaje("Arthur", 10, 100, 5, 5)
mi_personaje.atributos()