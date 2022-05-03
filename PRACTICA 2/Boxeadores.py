class Boxeadores:
    cont = 0
  

    def __init__(self):  
          

        self.nombre = input("Introduce el nombre del boxeador: ")
        self.edad = input("Introduce edad del boxeador: ")
        self.peso = input("Introduce peso del boxeador en kilogramos: ")
        self.nacion = input("Introduce nacionalidad del boxeador: ")
        Boxeadores.cont += 1
  

    def imprimeBox(self):  
        print("Nombre:", self.nombre, "Edad:", self.edad, "Peso:",self.peso+"KG","Nacionalidad:",self.nacion)        
  