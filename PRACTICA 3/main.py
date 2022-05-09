from Estudiante import *



condicion = True
while condicion != 3:
    print("1. Capturar Alumnos")
    print("2. Mostrar Alumnos")
    print("3. Salir")

    op = int(input("Digita una opcion: "))

    if op == 1:
        c1 = Estudiante() #Variable c1 es igual a la clase Estudiante del archivo Estudiante
        c1.AsignarNombre() #Se manda llamar el metodo AsignarNombre desde la clase Estudiante
        c1.AsignarEstado() #Se manda a llamar el metodo AsignarEstado desde la clase Estudiante
        c2 = Estudiante()
        c2.AsignarNombre()
        c2.AsignarEstado()
        c3 = Estudiante()
        c3.AsignarNombre()
        c3.AsignarEstado()
        c4 = Estudiante()
        c4.AsignarNombre()
        c4.AsignarEstado()
        c5 = Estudiante()
        c5.AsignarNombre()
        c5.AsignarEstado()
        

    if op == 2:
        print("\nAlumno 1:")     #5 objetos serán creados con datos fijos que el programador defina.   
        fijo1 = mostrarFijos("Gabriela", "14002", "POO", 90 )
        print("Nombre: {}\nNumero de control: {}\nMateria: {}\nCalificacion: {}".format(fijo1.getNombre(), fijo1.getNumero(), fijo1.getMateria(), fijo1.getCalif()))
        print("Estado: ")
        fijo1.Estado() #Imprimir estado aprobado/reprobado
        print()
        
        print("\nAlumno 2:")
        fijo2 = mostrarFijos("René", "19890", "POO", 100)
        print("Nombre: {}\nNumero de control: {}\nMateria: {}\nCalificacion: {}".format(fijo2.getNombre(), fijo2.getNumero(), fijo2.getMateria(), fijo2.getCalif()))
        fijo2.Estado()
        print() 
        
        print("\nAlumno 3:")
        fijo3 = mostrarFijos("Adrián", "19298", "POO", 60)
        print("Nombre: {}\nNumero de control: {}\nMateria: {}\nCalificacion: {}".format(fijo3.getNombre(), fijo3.getNumero(), fijo3.getMateria(), fijo3.getCalif()))
        fijo3.Estado()
        print() 
        
        print("\nAlumno 4:")
        fijo4 = mostrarFijos("José", "20203", "POO", 55)
        print("Nombre: {}\nNumero de control: {}\nMateria: {}\nCalificacion: {}".format(fijo4.getNombre(), fijo4.getNumero(), fijo4.getMateria(), fijo4.getCalif()))
        fijo4.Estado()
        print() 
        
        print("\nAlumno 5:")
        fijo5 = mostrarFijos("Julio", "44124", "POO", 80)
        print("Nombre: {}\nNumero de control: {}\nMateria: {}\nCalificacion: {} ".format(fijo5.getNombre(), fijo5.getNumero(), fijo5.getMateria(), fijo5.getCalif()))
        fijo5.Estado()
        print()    
        
            
        print("\nAlumno 6:")    #5 objetos que reciban cómo parámetros los valores e implementa el método AsignarNombre. (El usuario introduce los datos)
        c1.imprimeEstudiante()  
        print("\nAlumno 7:")
        c2.imprimeEstudiante()
        print("\nAlumno 8:")
        c3.imprimeEstudiante()
        print("\nAlumno 9:")
        c4.imprimeEstudiante()
        print("\nAlumno 10:")
        c5.imprimeEstudiante() # <- c1 = Estudiante(), se manda a llamar el metodo imprimeEstudiante
        print()

         
    if op == 3:
        print("\n\nFin del programa\n\n")
        break