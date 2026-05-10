class Persona:

    contador_turnos = 0

    def __init__(self, nombre):
        self._nombre = nombre

        Persona.contador_turnos += 1
        self.turno = Persona.contador_turnos

    @property
    def nombre(self):
        return self._nombre

    def __str__(self):
        return f"Turno #{self.turno} - {self._nombre}"