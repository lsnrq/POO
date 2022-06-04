class MagnumOpus:
    def __init__(self, nombre, identificacion, bateria, accion, plato):
        self.nombre = nombre
        self.identificacion = identificacion
        self.bateria = bateria
        self.accion = accion
        self.plato = plato

    def __str__(self):
        return (f"{self.nombre} {self.identificacion} {self.bateria} {self.accion} {self.plato}")

