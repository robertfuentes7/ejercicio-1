# 1. Creamos el molde llamado Personaje [cite: 51]
class Personaje:
    # Definimos que tenga nombre y vida (por defecto 100) [cite: 52]
    def __init__(self, nombre, vida=100):
        self.nombre = nombre
        self.vida = vida

    # 2. Función para restar 10 de vida [cite: 53]
    def recibir_golpe(self):
        self.vida = self.vida - 10
        print(f"{self.nombre} ha recibido un golpe. Vida actual: {self.vida}")

# 3. Creamos el objeto 'Mario' y lo hacemos recibir un golpe [cite: 54]
mario = Personaje("Mario")
mario.recibir_golpe()