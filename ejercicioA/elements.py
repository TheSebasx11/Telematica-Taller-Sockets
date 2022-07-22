class Elemento:
    def __init__(self, cedula, nombre, apellidos, nota1, nota2, nota3, nota4):
        self.cedula=cedula
        self.nombre=nombre
        self.apellidos=apellidos
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.nota4=nota4
    
    def Definitiva(self):
        return (float(self.nota1) + float(self.nota2) + float(self.nota3) + float(self.nota4))/4