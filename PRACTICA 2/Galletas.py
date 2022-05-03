class Galletas:
    cont = 0
  

    def __init__(self):  
          

        self.marca = input("Introduce marca de las galletas: ")
        self.sabor = input("Introduce sabor: ")
        self.precio = input("Introduce el precio: ")
        Galletas.cont += 1
  

    def imprimeGalletas(self):  
        print("Marca:", self.marca, "Sabor:", self.sabor, "Precio:","$"+self.precio)  
        
        