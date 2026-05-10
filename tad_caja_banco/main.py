from modelo.persona import Persona
from caja_banco import CajaBanco


def main():
    caja = CajaBanco()

    nombres = [
        "Pedro Loor",
        "Carmen Intriago",
        "Jorge Menéndez",
        "Valeria Cedeño",
        "Roberto Anchundia",
    ]

    print("=" * 40)
    print(" Banco del Pacífico — Caja #1")
    print("=" * 40)

    print("\nClientes llegando a la fila:\n")
    for nombre in nombres:
        persona = Persona(nombre)
        caja.agregar_persona(persona)
        print(f"  >> {persona} toma un turno y espera.")

    print("\nCajero listo. Iniciando atención...\n")
    while not caja.esta_vacia():
        persona = caja.atender()
        print(f"  [CAJERO] {persona} ha sido atendida.")

    print("\nTodos los clientes han sido atendidos.")


main()

caja = CajaBanco()
caja.agregar_persona(Persona("Pedro Loor"))
caja.agregar_persona(Persona("Carmen Intriago"))
caja.agregar_persona(Persona("Jorge Menéndez"))

resultado = caja.persona_abandona("Carmen Intriago")
print(resultado)
persona = caja.atender()
print(persona.nombre) 