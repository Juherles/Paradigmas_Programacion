class Estudiante:
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        if promedio >= 3.0:
            print("El estudiante aprueba con promedio:", promedio)
        else:
            print("El estudiante no aprueba con promedio:", promedio)

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

estudiante = Estudiante(nota1, nota2, nota3)
estudiante.mostrar_resultado()