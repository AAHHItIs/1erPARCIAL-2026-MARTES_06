class Pokemon:
    def __init__(self, nombre: str, tipo: str, nivel: int = 1)
    if not 1 <= nivel <= 100:
        raise ValueError("El nivel debe estar entre 1 y 100")
    self.nombre = nombre
    self.tipo = tipo
    self.nivel = nivel

def subir_nivel(self):
    if self.nivel < 100:
        self.nivel += 1
    
def __str__(self):
    return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"