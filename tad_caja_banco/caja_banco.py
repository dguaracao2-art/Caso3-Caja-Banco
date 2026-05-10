from modelo.cola import Cola

class CajaBanco:
    def __init__(self):
        self._fila = Cola()

    def registrar_cliente(self, persona):
        self._fila.push(persona)

    def atender_siguiente(self):
        return self._fila.pop()

    def cliente_abandona(self, nombre_buscar):
        # Filtramos la lista interna para sacar a la persona
        lista_temporal = []
        encontrado = False

        for p in self._fila.items:
            if p.nombre != nombre_buscar:
                lista_temporal.append(p)
            else:
                encontrado = True
                print(f"🏃 {nombre_buscar} se cansó de esperar y salió de la fila.")
        
        # Actualizamos la fila con los que se quedaron
        self._fila.items = lista_temporal
        return encontrado