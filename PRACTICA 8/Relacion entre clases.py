
class Equipo():
   def __init__(self, nombre, division, entrenador, participacion, victorias, derrotas):
       self.nombre = nombre
       self.division = division
       self.entrenador = entrenador
       self.participacion = participacion
       self.victorias = victorias
       self.derrotas = derrotas
       
   def __str__(self):
       return (f"{self.nombre}"+"\nDivision: "f"{self.division}")
   

class Jugador():
    def __init__(self, numero, nombre, puntos, pos, estatura, equipo, torneo):
        self.numero = numero
        self.nombre = nombre
        self.puntos = puntos
        self.pos = pos
        self.estatura = estatura
        self.equipo = equipo
        self.torneo = torneo
        
    def __str__(self):
        return ("Numero de uniforme: "f"{self.numero}"+"\nNombre: "f"{self.nombre}"+"\nEquipo: "f"{self.equipo}"+"\n" f"{self.torneo}")
   

class Torneo():
    def __init__(self, nombre, region, nEquipos, nJugados, nPendientes):
        self.nombre = nombre
        self.region = region
        self.nEquipos = nEquipos
        self.nJugados = nJugados
        self.nPendientes = nPendientes
        
    def __str__(self):
        return ("Torneo: "f"{self.nombre}"+
                "\nRegion: "f"{self.region}"+
                "\nEquipos participantes: "f"{self.nEquipos}"+
                "\nPartidos jugados: "f"{self.nJugados}"+
                "\nPartidos pendientes: "f"{self.nPendientes}")
                 
    
x = Torneo("Apertura 2022","Mexico",5,34,3)

   
    
    #Equipos
Equipo1 = Equipo("Tijuana","A","Eduardo Lopez",10,2,8)
print()
Equipo2 = Equipo("Mazatlan","A","Javier Hernandez",12,5,7)
print()
Equipo3 = Equipo("Guadalajara","A","Guardiola",11,0,11)
print()
Equipo4 = Equipo("Monterrey","A","Alberto Medina",5,1,4)
print()
Equipo5 = Equipo("Culiacan","A","Rafael Marquez",9,3,6)

#equipo 1
e1jugador1 = Jugador(11,"Rodriguez",9,"med",181,Equipo1,x)
e1jugador2 = Jugador(10, "Dominguez",12,"med",180,Equipo1,x)
e1jugador3 = Jugador(4, "Rosas",7,"med",175,Equipo1,x)
e1jugador4 = Jugador(5, "Castillo",5,"med",177,Equipo1,x)
e1jugador5 = Jugador(2, "Guzman",3,"def",190,Equipo1,x)
e1jugador6 = Jugador(3, "Hernandez",3,"def",180,Equipo1,x)
e1jugador7 = Jugador(20, "Lopez",0,"def",195,Equipo1,x)
e1jugador8 = Jugador(21, "Sanchez",25,"del",185,Equipo1,x)
e1jugador9 = Jugador(25, "Sillas",23,"del",178,Equipo1,x)
e1jugador10 = Jugador(7, "Perez",25,"del",182,Equipo1,x)
#equipo 2
e2jugador1 = Jugador(11,"Pablo",9,"med",181,Equipo2,x)
e2jugador2 = Jugador(10, "Juan",12,"med",180,Equipo2,x)
e2jugador3 = Jugador(4, "Alberto",7,"med",175,Equipo2,x)
e2jugador4 = Jugador(5, "Jose",5,"med",177,Equipo2,x)
e2jugador5 = Jugador(2, "Adrian",3,"def",190,Equipo2,x)
e2jugador6 = Jugador(3, "Luis",3,"def",180,Equipo2,x)
e2jugador7 = Jugador(20, "Alexis",0,"def",195,Equipo2,x)
e2jugador8 = Jugador(21, "Alan",25,"del",185,Equipo2,x)
e2jugador9 = Jugador(25, "Pedro",23,"del",178,Equipo2,x)
e2jugador10 = Jugador(7, "Marco",25,"del",182,Equipo2,x)
#equipo 3
e3jugador1 = Jugador(11,"Andres",9,"med",181,Equipo3,x)
e3jugador2 = Jugador(10, "Arturo",12,"med",180,Equipo3,x)
e3jugador3 = Jugador(4, "Adrian",7,"med",175,Equipo3,x)
e3jugador4 = Jugador(5, "Marcos",5,"med",177,Equipo3,x)
e3jugador5 = Jugador(2, "Carlos",3,"def",190,Equipo3,x)
e3jugador6 = Jugador(3, "Gimenez",3,"def",180,Equipo3,x)
e3jugador7 = Jugador(20, "Raul",0,"def",195,Equipo3,x)
e3jugador8 = Jugador(21, "Ponce",25,"del",185,Equipo3,x)
e3jugador9 = Jugador(25, "Maradona",23,"del",178,Equipo3,x)
e3jugador10 = Jugador(7, "Diego",25,"del",182,Equipo3,x)
#equipo 4
e4jugador1 = Jugador(11,"Christian",9,"med",181,Equipo4,x)
e4jugador2 = Jugador(10, "Gonzalo",12,"med",180,Equipo4,x)
e4jugador3 = Jugador(4, "Blanco",7,"med",175,Equipo4,x)
e4jugador4 = Jugador(5, "Esteban",5,"med",177,Equipo4,x)
e4jugador5 = Jugador(2, "Lozano",3,"def",190,Equipo4,x)
e4jugador6 = Jugador(3, "Enrique",3,"def",180,Equipo4,x)
e4jugador7 = Jugador(20, "Javier",0,"def",195,Equipo4,x)
e4jugador8 = Jugador(21, "Ramiro",25,"del",185,Equipo4,x)
e4jugador9 = Jugador(25, "Jesus",23,"del",178,Equipo4,x)
e4jugador10 = Jugador(7, "Domingo",25,"del",182,Equipo4,x)
#equipo 5
e5jugador1 = Jugador(11,"Rene",9,"med",181,Equipo5,x)
e5jugador2 = Jugador(10, "Miguel",12,"med",180,Equipo5,x)
e5jugador3 = Jugador(4, "Jorge",7,"med",175,Equipo5,x)
e5jugador4 = Jugador(5, "Erick",5,"med",177,Equipo5,x)
e5jugador5 = Jugador(2, "Bernardo",3,"def",190,Equipo5,x)
e5jugador6 = Jugador(3, "Harry",3,"def",180,Equipo5,x)
e5jugador7 = Jugador(20, "Styles",0,"def",195,Equipo5,x)
e5jugador8 = Jugador(21, "Peter",25,"del",185,Equipo5,x)
e5jugador9 = Jugador(25, "Parker",23,"del",178,Equipo5,x)
e5jugador10 = Jugador(7, "Paco",25,"del",182,Equipo5,x)

print("Equipo 1: ")
print(e1jugador1)
print()
print(e1jugador2)
print()
print(e1jugador3)
print()
print(e1jugador4)
print()
print(e1jugador5)
print()
print(e1jugador6)
print()
print(e1jugador7)
print()
print(e1jugador8)
print()
print(e1jugador9)
print()
print(e1jugador10)
print()
print("Equipo 2: ")
print(e2jugador1)
print()
print(e2jugador2)
print()
print(e2jugador3)
print()
print(e2jugador4)
print()
print(e2jugador5)
print()
print(e2jugador6)
print()
print(e2jugador7)
print()
print(e2jugador8)
print()
print(e2jugador9)
print()
print(e2jugador10)
print()
print("Equipo 3: ")
print(e3jugador1)
print()
print(e3jugador2)
print()
print(e3jugador3)
print()
print(e3jugador4)
print()
print(e3jugador5)
print()
print(e3jugador6)
print()
print(e3jugador7)
print()
print(e3jugador8)
print()
print(e3jugador9)
print()
print(e3jugador10)
print()
print("Equipo 4: ")
print(e4jugador1)
print()
print(e4jugador2)
print()
print(e4jugador3)
print()
print(e4jugador4)
print()
print(e4jugador5)
print()
print(e4jugador6)
print()
print(e4jugador7)
print()
print(e4jugador8)
print()
print(e4jugador9)
print()
print(e4jugador10)
print("Equipo 5: ")
print(e5jugador1)
print()
print(e5jugador2)
print()
print(e5jugador3)
print()
print(e5jugador4)
print()
print(e5jugador5)
print()
print(e5jugador6)
print()
print(e5jugador7)
print()
print(e5jugador8)
print()
print(e5jugador9)
print()
print(e5jugador10)