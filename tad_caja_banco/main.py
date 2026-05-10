from modelo.persona import Persona
def ejecutar_simulacion():
    cola_banco = [] 
    print("--- LLEGADA DE CLIENTES ---")
    clientes = ["Gabriel Leyton", "Bryan Chimbo", "Danny Guaraca"]
    
    objetos_persona = []
    for nombre in clientes:
        p = Persona(nombre)
        objetos_persona.append(p)
        print(f">> Turno #{p.turno} - {p.nombre} toma un turno y espera.")
        
        cola_banco.append(p) 

    print("\n" + "."*3)
    print("--- ATENCIÓN EN CAJA ---")

    while len(cola_banco) > 0:
        atendido = cola_banco.pop(0)
        print(f"[CAJERO] Turno #{atendido.turno} - {atendido.nombre} ha sido atendida.")

if __name__ == "__main__":
    ejecutar_simulacion()