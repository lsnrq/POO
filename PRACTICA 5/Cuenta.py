class Cuenta:
    persona = {}

    def __init__(self, nombre, depositar):
        self.persona['PIN'] = int(input("Introduce tu nuevo PIN: "))
        self.persona['Nombre'] = nombre
        self.persona['Saldo'] = depositar

    def retiro(self, monto):
        if self.persona['Saldo'] >= monto:
            self.persona['Saldo'] -= monto
            print("Retirado.\n")
        else:
            print("\nLo sentimos, no hay saldo suficientes para retirar...")
            print("Usted solo tiene: ${}\n".format(self.persona['Saldo']))

    def depositar(self, monto):
        self.persona['Saldo'] += monto
        print("Has depositado: ${}".format(monto))


    def verSaldo(self):
        print("Saldo actual de la cuenta: ${}\n".format(self.persona['Saldo']))
