from modelo.cola import Cola


class CajaBanco:

    def __init__(self):
        self._cola = Cola()

    def agregar_persona(self, persona):
        self._cola.push(persona)

    def atender(self):
        return self._cola.pop()

    def esta_vacia(self):
        return self._cola.isEmpty()