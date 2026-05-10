from modelo.cola import Cola
import time

def ejecutar_banco():
    caja = Cola()
    # Lista de clientes manual para no usar Faker
    clientes_entrantes = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez"]

    print("---INICIO DE JORNADA BANCARIA---")

   
    print("\n>>> REGISTRANDO LLEGADA DE CLIENTES:")
    for nombre in clientes_entrantes:
        caja.encolar(nombre)
        print(f"📥 Cliente en fila: {nombre}")
        time.sleep(0.5)

    print(f"\nEstado actual: {len(caja.items)} personas esperando.")
    print(f"Siguiente ticket para: {caja.primero()}")


    print("\n>>> ATENDIENDO EN VENTANILLA:")
    while not caja.esta_vacia():
        cliente_siendo_atendido = caja.desencolar()
        print(f"✅ Atendiendo a {cliente_siendo_atendido}...")
        time.sleep(1) # Simulación de tiempo de trámite
        print(f"[Transacción completada]")

    print("\n---COLA VACÍA: Fin de la atención---")

if __name__ == "__main__":
    ejecutar_banco()