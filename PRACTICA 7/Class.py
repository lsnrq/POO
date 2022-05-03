from Bird import Bird



class AngryBirds(Bird):
    def __init__(self, nombre, color, habilidad, velocidad):
        self.nombre = nombre
        self.color = color
        self.habilidad = habilidad
        self.velocidad = velocidad
    angry=  ["Blue","Azul","Dividirse",500], ["Chuck","Amarillo","Veloz",1200], ["Hal","Verde","Boomerang",700]

    
class Blue(Bird):
    
    def __init__(self, nombre, color, habilidad, velocidad):
        self.nombre = nombre
        self.color = color
        self.habilidad = habilidad
        self.velocidad = velocidad
        
    
    def atributos():
        blue = AngryBirds.angry[0] 
        print(blue)         
        
    def imprime():      
        print("El pájaro Blue atacó y se dividió en tres.")



class Chuck(Bird):
    
    def __init__(self, nombre, color, habilidad, velocidad):
        self.nombre = nombre
        self.color = color
        self.habilidad = habilidad
        self.velocidad = velocidad
        
    def atributos():
        chuck = AngryBirds.angry[1]
        print(chuck)    
        
    def imprime():
        print("El pájaro Chuck atacó y se hizo más veloz")
        
        
        
class Hal(Bird):
    
    def __init__(self, nombre, color, habilidad, velocidad):
        self.nombre = nombre
        self.color = color
        self.habilidad = habilidad
        self.velocidad = velocidad

    def atributos():
        hal = AngryBirds.angry[2] 
        print(hal)        
        
    def imprime():       
        print("El pájaro Hal atacó y genero un tornado.")


