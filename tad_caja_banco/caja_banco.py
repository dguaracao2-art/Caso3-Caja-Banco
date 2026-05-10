from modelo.cola import Cola

class CajaBanco:
    def __init__(self):
        self._cola = Cola()

    def registrar_llegada(self, persona):
        self._cola.push(persona)

    def atender_cliente(self):
        return self._cola.pop()

    def cliente_abandona(self, nombre_cliente):
        # Filtramos la lista: dejamos a todos menos al que se va (Requerimiento 2)
        nueva_fila = []
        for p in self._cola.items:
            if p.nombre != nombre_cliente:
                nueva_fila.append(p)
            else:
                print(f"❌ {nombre_cliente} abandonó la fila.")
        
        self._cola.items = nueva_fila