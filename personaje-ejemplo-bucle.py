class Personaje:
    def __init__(self, nombre, vida=100):
        self.nombre = nombre
        self.vida = vida [cite: 52]

    def recibir_golpe(self):
        self.vida -= 10 [cite: 53]
        print(f"{self.nombre} recibió un golpe. Vida restante: {self.vida}")

# 1. Creamos el objeto
mario = Personaje("Mario") [cite: 54]

# 2. El Bucle For (La Cajera)
# Queremos que reciba 3 golpes seguidos
golpes = [1, 2, 3] 

for golpe in golpes:
    mario.recibir_golpe()