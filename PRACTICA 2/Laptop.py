class Laptop:
    cont = 0
  

    def __init__(self):  
          

        self.color = input("Introduce el color de la laptop: ")
        self.espacio = input("Introduce capacidad en GB del disco duro: ")
        self.RAM = input("Introduce capacidad en GB de la RAM: ")
        Laptop.cont += 1
  

    def imprimeLaptop(self):  
        print("Color:", self.color, "Disco duro:", self.espacio+"GB", "RAM:",self.RAM+"GB")
        