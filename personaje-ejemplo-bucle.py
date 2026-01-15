class Personaje:
    def __init__(self, nombre, vida=100):
        self.nombre = nombre
        self.vida = vida

    def recibir_golpe(self):
        self.vida = self.vida - 10
        print(f"{self.nombre} recibió un golpe. Vida restante: {self.vida}")

# 1. Creamos el objeto (Sin etiquetas de referencia)
mario = Personaje("Mario")

# 2. El Bucle For (Simulando 3 golpes)
golpes = [1, 2, 3]
for golpe in golpes:
    mario.recibir_golpe()