from Desayuno import robot_desayuno
from Comida import robot_comida
from Cena import robot_cena
    

condicion = True

while condicion!=False:
    print("""
    1. Desayuno
    2. Comida
    3. Cena
    4. Salir
    """)
    eleccion = int(input("Que deseas hacer? "))
    if eleccion == 1:
        print("""
        1. Desayuno
        2. Salir
        """)
        eleccion_desayuno = int(input("Que deseas hacer? "))
        if eleccion_desayuno == 1:
            print("""
            1. Robot 1
            2. Robot 2
            3. Robot 3
            """)
            eleccion_robot = int(input("Que robot deseas? "))
            if eleccion_robot == 1:
                robot_1 = robot_desayuno("Robot 1", "123456789", 100, "desayuno", "desayuno")
            elif eleccion_robot == 2:
                robot_2 = robot_desayuno("Robot 2", "987654321", 100, "desayuno", "desayuno")
            elif eleccion_robot ==3:
                robot_3 = robot_desayuno("Robot 3", "12312344", 100, "desayuno", "desayuno")
            else:
                print("El robot no existe")
            if eleccion_robot == 1 or 2 or 3:
                print("""
                      1. Preparar ingredientes
                      """)
            eleccion_pasos = int(input("Que robot deseas? "))
            if eleccion_pasos ==1:
                print("Haz preparado los ingredientes")
                robot_1 = robot_desayuno("mini Robot", "123456789", 90, "Preparar ingredientes", "desayuno")     
                print("""
                      2. Cocinar
                      """)
                eleccion_pasos2 = int(input("Elige la opcion 2 para cocinar "))      
                if eleccion_pasos2 == 2:
                    print("Haz cocinado")
                    robot_1 = robot_desayuno("mini Robot", "123456789", 80, "Cocinar", "desayuno")     
                    print("""
                          3. servir
                          """)
                    eleccion_pasos3 = int(input("Elige la opcion 3 para servir "))      
                    if eleccion_pasos3 == 3:
                       print("¡Hurra! El plato estaba delicioso\n")
                       robot_1 = robot_desayuno("mini Robot", "123456789", 50, "Servir", "desayuno")   
                            
        elif eleccion_desayuno == 2:
            print("Hasta luego, vuelva pronto.")
            break
    elif eleccion == 2:
        print("""
        1. Comida
        2. Salir
        """)
        eleccion_comida = int(input("Que deseas hacer? "))
        if eleccion_comida == 1:
            print("""
            1. Robot 1
            2. Robot 2
            3. Robot 3
            """)
            eleccion_robot = int(input("Que robot deseas? "))
            if eleccion_robot == 1:
                robot_1 = robot_comida("mini Robot", "123456789", 100, "comida", "comida")
            elif eleccion_robot == 2:
                robot_2 = robot_comida("mini Robot", "987654321", 100, "comida", "comida")
            elif eleccion_robot ==3:
                robot_3 = robot_comida("mini Robot", "12312344", 100, "comida", "comida")
            else:
                print("El robot no existe")
            if eleccion_robot == 1 or 2 or 3:
                print("""
                      1. Preparar ingredientes
                      """)
            eleccion_pasos = int(input("Que robot deseas? "))
            if eleccion_pasos ==1:
                print("\nHaz preparado los ingredientes\n")
                robot_1 = robot_comida("mini Robot", "123456789", 90, "Preparar ingredientes", "comida")     
                print("""
                      2. Cocinar
                      """)
                eleccion_pasos2 = int(input("Elige la opcion 2 para cocinar "))      
                if eleccion_pasos2 == 2:
                    print("\nHaz cocinado\n")
                    robot_1 = robot_comida("mini Robot", "123456789", 80, "Cocinar", "comida")     
                    print("""
                          3. servir
                          """)
                    eleccion_pasos3 = int(input("Elige la opcion 3 para servir "))      
                    if eleccion_pasos3 == 3:
                       print("\n¡Hurra! El plato estaba delicioso\n")
                       robot_1 = robot_comida("mini Robot", "123456789", 50, "Servir", "comida")   
    elif eleccion == 3:
        print("""
        1. Cena
        2. Salir
            """)
        eleccion_robot = int(input("Que robot deseas? "))
        if eleccion_robot == 1:
            robot_1 = robot_cena("mini Robot", "123456789", 100, "cena", "cena")
        elif eleccion_robot == 2:
            robot_2 = robot_cena("mini Robot", "987654321", 100, "cena", "cena")
        elif eleccion_robot ==3:
            robot_3 = robot_cena("mini Robot", "12312344", 100, "cena", "cena")
        else:
            print("El robot no existe")
        if eleccion_robot == 1 or 2 or 3:
            print("""
                  1. Preparar ingredientes
                  """)
        eleccion_pasos = int(input("Que robot deseas? "))
        if eleccion_pasos ==1:
            print("\nHaz preparado los ingredientes\n")
            robot_1 = robot_cena("mini Robot", "123456789", 90, "Preparar ingredientes", "cena")     
            print("""
                  2. Cocinar
                  """)
            eleccion_pasos2 = int(input("Elige la opcion 2 para cocinar "))      
            if eleccion_pasos2 == 2:
                print("\nHaz cocinado\n")
                robot_1 = robot_cena("mini Robot", "123456789", 80, "Cocinar", "cena")     
                print("""
                      3. servir
                      """)
                eleccion_pasos3 = int(input("Elige la opcion 3 para servir "))      
                if eleccion_pasos3 == 3:
                   print("\n¡Hurra! El plato estaba delicioso\n")
                   robot_1 = robot_cena("mini Robot", "123456789", 50, "Servir", "cena")   
    elif eleccion == 4:
        condicion = False
        print("Hasta luego, vuelva pronto.")
    else:
        print("El robot no existe")
        
