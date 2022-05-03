from Cuaderno import Cuaderno
from Laptop import Laptop
from Boxeadores import Boxeadores
from Relojes import Relojes
from Galletas import Galletas


condicion = True
while condicion != 6:
    print("1. Clase 1: CUADERNOS")
    print("2. Clase 2: LAPTOPS")
    print("3. Clase 3: BOXEADORES")
    print("4. Clase 4: RELOJES")
    print("5. Clase 5: GALLETAS")
    print("6. Salir")

    op = int(input("Digita una opcion: "))

    if op == 1:
        opp = True
        while opp != 3:
            print("\nCuadernos")
            print("1. Capturar clase")
            print("2. Imprimir clase")
            print("3. Regresar")

            op1=int(input("Digita una opcion: "))
            if op1 == 1:
              c1 = Cuaderno()
              c2 = Cuaderno()
              c3 = Cuaderno() 
            elif op1 == 2:
                print("Cuaderno 1:")
                c1.imprimeCuaderno()
                print("Cuaderno 2:")
                c2.imprimeCuaderno()
                print("Cuaderno 3:")
                c3.imprimeCuaderno()
            elif op1 == 3:
                print("\nHasta luego, vuelva pronto!\n\n")
                break

    if op == 2:
        opp = True
        while opp != 3:
            print("\nLaptops")
            print("1. Capturar clase")
            print("2. Imprimir clase")
            print("3. Regresar")

            op1=int(input("Digita una opcion: "))
            if op1 == 1:
              l1 = Laptop()
              l2 = Laptop()
              l3 = Laptop() 
            elif op1 == 2:
                print("Laptop 1:")
                l1.imprimeLaptop()
                print("Laptop 2:")
                l2.imprimeLaptop()
                print("Laptop 3:")
                l3.imprimeLaptop()
            elif op1 == 3:
             print("\nHasta luego, vuelva pronto!\n\n")
             break  
         
    if op == 3:
            opp = True
            while opp != 3:
                print("\nBoxeadores")
                print("1. Capturar clase")
                print("2. Imprimir clase")
                print("3. Regresar")

                op1=int(input("Digita una opcion: "))
                if op1 == 1:
                  b1 = Boxeadores()
                  b2 = Boxeadores()
                  b3 = Boxeadores() 
                elif op1 == 2:
                    print("Boxeador 1:")
                    b1.imprimeBox()
                    print("Boxeador 2:")
                    b2.imprimeBox()
                    print("Boxeador 3:")
                    b3.imprimeBox()
                elif op1 == 3:
                 print("\nHasta luego, vuelva pronto!\n\n")
                 break    

    if op == 4:
            opp = True
            while opp != 3:
                print("\nRelojes")
                print("1. Capturar clase")
                print("2. Imprimir clase")
                print("3. Regresar")

                op1=int(input("Digita una opcion: "))
                if op1 == 1:
                  r1 = Relojes()
                  r2 = Relojes()
                  r3 = Relojes() 
                elif op1 == 2:
                    print("Reloj 1:")
                    r1.imprimeR()
                    print("Reloj 2:")
                    r2.imprimeR()
                    print("Reloj 3:")
                    r3.imprimeR()
                elif op1 == 3:
                 print("\nHasta luego, vuelva pronto!\n\n")
                 break 
             
    if op == 5:
            opp = True
            while opp != 3:
                print("\nGalletas")
                print("1. Capturar clase")
                print("2. Imprimir clase")
                print("3. Regresar")

                op1=int(input("Digita una opcion: "))
                if op1 == 1:
                  g1 = Galletas()
                  g2 = Galletas()
                  g3 = Galletas() 
                elif op1 == 2:
                    print("Galletas 1:")
                    g1.imprimeGalletas()
                    print("Galletas 2:")
                    g2.imprimeGalletas()
                    print("Galletas 3:")
                    g3.imprimeGalletas()
                elif op1 == 3:
                 print("\nHasta luego, vuelva pronto!\n\n")
                 break    
        
    if op == 6:
        print("\n\nHasta luego, vuelva pronto!\n\n")
        break
  