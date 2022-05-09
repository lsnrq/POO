class Estudiante:
    cont = 0 
  

    def __init__(self):  
        self.numero_control = input("Introduce el numero de control del estudiante: ")
        self.materia = input("Introduce la materia del estudiante: ")

        Estudiante.cont += 1
        
   
    def AsignarNombre(self): #Metodo  para asignar nombre al estudiante
        self.nombre = input("Introduce el nombre del alumno: ")
        Estudiante.cont += 1 #Al introducir el nombre del alumno se suma al contador
        
        
    def AsignarEstado(self): #Introducir la calificacion del alumno para despues asignarle el estado aprobado/reprobado.
        self.calif = int(input("Introduce la calificacion del alumno: "))
        Estudiante.cont +=1
    
    
    def imprimeEstudiante(self):     
        self.estado = self.calif
        print()
        print("Nombre:", self.nombre)
        print("Numero de control:", self.numero_control)
        print("Materia:", self.materia)
        print("Calificacion:", self.calif)
        print("Estado:")
        if self.estado >= 60:
            print("APROBADO\n")
            return self.estado
        else:
            print("REPROBADO\n")
            return self.estado
        
    
class mostrarFijos(): #En esta clase se mostraran los datos creados fijamente en el archivo main
        def __init__(self, nombre=str, numero=str, materia=str, calif=int):
            self.nombre = nombre
            self.numero = numero
            self.materia = materia
            self.calif = calif
            
        def getNombre(self):
            return self.nombre
        
        def getNumero(self):
            return self.numero
        
        def getMateria(self):
            return self.materia
        
        def getCalif(self):
            return self.calif
        
        
        def Estado(self):
            self.estado = self.calif
                
            if self.estado >= 60:
                print("APROBADO\n")
                return self.estado
            else:
                print("REPROBADO\n")
                return self.estado
            

    
        

  
