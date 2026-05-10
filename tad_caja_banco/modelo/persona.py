class Persona:
    _contador_turnos = 1 

    def __init__(self, nombre):
        self._nombre = nombre
        self._turno = Persona._contador_turnos
        Persona._contador_turnos += 1 

    @property
    def nombre(self):
        return self._nombre

    @property
    def turno(self):
        return self._turno

    def __str__(self):
        return f"Turno #{self._turno} - {self._nombre}"