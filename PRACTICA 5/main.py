from Cuenta import Cuenta
from Banco import Banco

print("\nBANCO\n")
banco = Banco()
condicion = True
while condicion != 3:
    print("1. Registrarse")
    print("2. Iniciar sesion")
    print("3. Salir")

    op = int(input("Digita una opcion: "))

    if op == 1:
        print("Es necesario un deposito para poder registrarse.")
        cuenta = Cuenta(input("Nombre: "), int(input("Depositar: $")))
        banco.nuevoCliente(cuenta)
        print("\nTe has registrado correctamente!\n")
    elif op == 2:
        PIN = int(input("Cual es tu PIN? "))
        nombre = input("Cual es tu nombre?  ")
        clienteRegistrado = banco.iniciarSesion(nombre, PIN)
        if clienteRegistrado:
            print("Bienvenido")
            sesionIniciada = True
            while sesionIniciada != 4:
                print("1. Retirar")
                print("2. Depositar")
                print("3. Saldo")
                print("4. Regresar a inicio")

                op1 = int(input("Digita una opcion: "))
                if op1 == 1:
                    print()
                    clienteRegistrado.retiro(int(input("Retirar: ")))
                elif op1 == 2:
                    clienteRegistrado.depositar(int(input("Depositar: $")))
                elif op1 == 3:
                    clienteRegistrado.verSaldo1()
                if op1 == 4:
                    print("\nHasta luego, vuelva pronto!\n\n")
                    break
        else:
            print("Introduce una cuenta correcta")
            continue
        
    if op == 3:
        print("\n\nHasta luego, vuelva pronto!\n\n")
        break
    
    
