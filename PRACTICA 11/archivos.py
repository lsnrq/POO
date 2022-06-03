import csv


try: #try para errores y excepciones
    with open('practica11.csv') as f:
        reader = csv.reader(f)  #lectura de archivo .csv y extraer valores para las calificaciones
        for valor in reader:
            c1 = int(valor[3]) #100
            c2 = int(valor[4]) #78
            c3 = int(valor[5]) #99
            c4 = int(valor[5]) #87
            c5 = int(valor[6]) #58
            c6 = int(valor[7]) #67
            c7 = int(valor[8]) #98
            c8 = int(valor[9]) #78
            c9 = int(valor[10]) #99
            c10 = int(valor[11]) #69
    
    
    class Alumno():
        def __init__(self, nombre, matricula, calif1, calif2, calif3, calif4, calif5, calif6, calif7, promedio):
            self.nombre = nombre
            self.matricula = matricula
            self.calif1 = calif1
            self.calif2 = calif2
            self.calif3 = calif3
            self.calif4 = calif4
            self.calif5 = calif5
            self.calif6 = calif6
            self.calif7 = calif7
            self.promedio = promedio
    
    
        def __str__(self):  #metodo __str__() para imprimir en el archivo de texto
            return ("Nombre: "f"{self.nombre}"+
                    "\nMatricula: "f"{self.matricula}"+
                    "\nCalificacion 1: "f"{self.calif1}"+
                    "\nCalificacion 2: "f"{self.calif2}"+
                    "\nCalificacion 3: "f"{self.calif3}"+
                    "\nCalificacion 4: " f"{self.calif4}"+
                    "\nCalificacion 5: "f"{self.calif5}"+
                    "\nCalificacion 6: "f"{self.calif6}"+
                    "\nCalificacion 7: "f"{self.calif7}"+"\nPromedio:"f"{self.promedio}")
        
    
    alumno1 = Alumno("Luis Enrique",1275919,c1,c2,c3,c4,c5,c6,c7,(c1+c2+c3+c4+c5+c6+c7)/7)
    alumno2 = Alumno("Gabriela",121112,c2,c3,c1,c10,c9,c8,c2,(c2+c3+c1+c10+c9+c8+c2)/7)
    alumno3 = Alumno("Sebastian",15159,c9,c2,c2,c3,c4,c1,c7,(c9+c2+c2+c3+c4+c1+c7)/7)
   
    
    txt1 = str(alumno1)
    txt2 = str(alumno2)
    txt3 = str(alumno3)
    
    
    arch = open('texto.txt','w')
    arch.write(txt1)
    arch.write("\n\n")
    arch = open('texto.txt','a')
    arch.write(txt2)
    arch.write("\n\n")
    arch.write(txt3)
    arch.close()
    print("Se genero el archivo de texto correctamente.")

except TypeError:
    print("Solo se puede concatenar str (no int) a str")
except FileNotFoundError:
    print("Archivo no encontrado o no existe")
except ZeroDivisionError:
    print("No se puede dividir enre 0 ")
except  IndexError:
    print("Lista fuera del rango")