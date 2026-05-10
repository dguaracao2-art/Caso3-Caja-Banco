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

    def persona_abandona(self, nombre):
        aux1 = Cola()
        aux2 = Cola()

        encontrado = False

        # Sacar personas de la cola original
        while not self._cola.isEmpty():
            persona = self._cola.pop()

            if persona.nombre == nombre and not encontrado:
                encontrado = True
            else:
                aux1.push(persona)

        # Invertir
        while not aux1.isEmpty():
            aux2.push(aux1.pop())

        # Restaurar orden original
        while not aux2.isEmpty():
            self._cola.push(aux2.pop())

        return encontrado