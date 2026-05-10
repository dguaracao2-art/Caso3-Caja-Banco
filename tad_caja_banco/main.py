from modelo.persona import Persona
from tad_caja_banco.caja_banco import CajaBanco

def iniciar():
    banco = CajaBanco()

    print("--- 🏦 BIENVENIDO AL BANCO ---")
    
    # REQUERIMIENTO 1: Registramos personas (Los turnos se generan solos)
    banco.registrar_cliente(Persona("Juan Perez"))
    banco.registrar_cliente(Persona("Maria Garcia"))
    banco.registrar_cliente(Persona("Carlos Lopez"))

    # REQUERIMIENTO 2: Alguien decide irse
    banco.cliente_abandona("Maria Garcia")

    # ATENCIÓN EN CAJA
    print("\n--- ATENCIÓN EN VENTANILLA ---")
    while not banco._fila.isEmpty():
        cliente = banco.atender_siguiente()
        print(f"✅ Atendiendo a: {cliente}")

if __name__ == "__main__":
    iniciar()