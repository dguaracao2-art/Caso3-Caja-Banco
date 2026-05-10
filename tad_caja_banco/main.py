# main.py

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
        print(f"  >> {persona.nombre} toma un turno y espera.")

    print("\nCajero listo. Iniciando atención...\n")
    while not caja.esta_vacia():
        persona = caja.atender()
        print(f"  [CAJERO] La persona {persona.nombre} ha sido atendida.")

    print("\nTodos los clientes han sido atendidos.")


main()