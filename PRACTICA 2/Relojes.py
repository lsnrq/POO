class Relojes:
    cont = 0
  

    def __init__(self):  

        self.marca = input("Introduce marca del reloj: ")
        self.modelo = input("Introduce modelo: ")
        self.color = input("Introduce el color: ")
        Relojes.cont += 1
  

    def imprimeR(self):  
        print("Marca:", self.marca, "Modelo:", self.modelo, "Color:",self.color)  
        