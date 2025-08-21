from pathlib import Path

S = Path("notas.txt") 

def saldo():
    nombre = input("Ingrese el nombre del cliente: ")
    try:
        with open(S, "r", encoding="utf-8") as f:
            next(f)#Aqui salto el encabezado del archivo
            for linea in f:
                cedula, nom, saldo = linea.strip().split(",")
                if nom.lower() == nombre:
                    print(f"El saldo de {nom} es: {saldo}")
                    return
        print(" Cliente no encontrado.")
    except IOError:
        print(" ERROR.")


def mayores():
    contador = 0
    try:
        with open(S, "r", encoding="utf-8") as f:
            next(f)
            for linea in f:
                _, _, saldo = linea.strip().split(",")
                if float(saldo) > 50:
                    contador += 1
        print(f"Clientes con saldo mayor a 50: {contador}")
    except IOError:
        print(" ERROR")


def ordenados():
    clientes = []
    try:
        with open(S, "r", encoding="utf-8") as f:
            next(f)
            for linea in f:
                cedula, nombre, saldo = linea.strip().split(",")
                clientes.append((nombre, float(saldo)))
        clientes.sort(key=lambda x: x[1])  # ordenar por saldo
        print("\n Clientes ordenados por saldo:")
        for nombre, saldo in clientes:
            print(f"{nombre} - {saldo}")
    except IOError:
        print("ERROR.")


def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Buscar saldo por nombre")
        print("2. Contar clientes con saldo mayor a 50")
        print("3. Listar clientes ordenados por saldo")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            saldo()
        elif opcion == "2":
            mayores()
        elif opcion == "3":
            ordenados()
        elif opcion == "4":
            print(" Saliendo")
            break
        else:
            print(" ERROR")


if __name__ == "__main__":
    menu()

