from repository.repo_json import RepoJson
from services.persona_service import PersonaService
from services.cliente_service import ClienteService
from services.producto_service import ProductoService


repo = RepoJson("data/db.json")

persona_service = PersonaService(repo)
cliente_service = ClienteService(repo)
producto_service = ProductoService(repo)


def menu_personas():
    opcion = ""

    while opcion != "0":
        print("\n========== MENÚ PERSONAS ==========")
        print("1. Registrar persona")
        print("2. Listar personas")
        print("3. Modificar persona")
        print("4. Eliminar persona")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            persona_service.registrar()
        elif opcion == "2":
            persona_service.listar()
        elif opcion == "3":
            persona_service.modificar()
        elif opcion == "4":
            persona_service.eliminar()
        elif opcion == "0":
            print("Volviendo al menú principal...")
        else:
            print("Opción incorrecta.")


def menu_clientes():
    opcion = ""

    while opcion != "0":
        print("\n========== MENÚ CLIENTES ==========")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente_service.registrar()
        elif opcion == "2":
            cliente_service.listar()
        elif opcion == "3":
            cliente_service.modificar()
        elif opcion == "4":
            cliente_service.eliminar()
        elif opcion == "0":
            print("Volviendo al menú principal...")
        else:
            print("Opción incorrecta.")


def menu_productos():
    opcion = ""

    while opcion != "0":
        print("\n========== MENÚ PRODUCTOS ==========")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto_service.registrar()
        elif opcion == "2":
            producto_service.listar()
        elif opcion == "3":
            producto_service.modificar()
        elif opcion == "4":
            producto_service.eliminar()
        elif opcion == "0":
            print("Volviendo al menú principal...")
        else:
            print("Opción incorrecta.")


def menu_principal():
    opcion = ""

    while opcion != "0":
        print("\n== SISTEMA DE GESTIÓN ==")
        print("1. Gestión de personas")
        print("2. Gestión de clientes")
        print("3. Gestión de productos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_personas()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_productos()
        elif opcion == "0":
            print("Saliendo del sistema...")
        else:
            print("Opción incorrecta.")


menu_principal()