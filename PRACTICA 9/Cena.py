from MagnumOpus import MagnumOpus



class robot_cena(MagnumOpus):
    def __init__(self, nombre, identificacion, bateria, accion, plato):
        super().__init__(nombre, identificacion, bateria, accion, plato)
        self.bateria = self.bateria - 10
        self.accion = accion
        self.plato = "cena"
        print(f"Nombre: {self.nombre}\nId: {self.identificacion}\nBateria: {self.bateria}\nUltima accion: {self.accion}\nPlato: {self.plato}")

