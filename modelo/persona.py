# modelo/persona.py

class Persona:

    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    def __str__(self):
        return self._nombre