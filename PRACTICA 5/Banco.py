class Banco:
    cuentas = []

    def nuevoCliente(self, cuenta):
        self.cuentas.append(cuenta)

    def iniciarSesion(self, nombre, PIN):
        for i in range(len(self.cuentas)):
            if PIN in self.cuentas[i].persona.values() and nombre in self.cuentas[i].persona.values():
                print("\nSesion iniciada\n")
                return self.cuentas[i]
