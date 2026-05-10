class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        """Requerimiento 1: Agregar al final"""
        self.items.append(item)

    def desencolar(self):
        """Requerimiento 2: Atender al primero"""
        if self.esta_vacia():
            return None
        return self.items.pop(0)

    def primero(self):
        if self.esta_vacia():
            return None
        return self.items[0]