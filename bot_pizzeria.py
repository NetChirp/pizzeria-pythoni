# --- MIS CONSTANTES ---
COLOR_AZUL: str = "\033[34m"
COLOR_AMARILLO: str = "\033[33m"
COLOR_VERDE: str = "\033[32m"
COLOR_ROJO: str = "\033[31m"
RESETEO_COLOR: str = "\033[0m"

# --- DATOS INICIALES ---
menu = ["Margarita", "Cuatro Quesos", "Pepperoni", "Hawaiana"]
stock_ingredientes = ["queso", "tomate", "cebolla", "aceitunas", "champiñones", "jamon"]

carrito_pizzas = []
ingredientes_solicitados = (
    []
)  # Aquí entra to do lo que escriba el usuario. Tanto correcto como incorrecto.

print(f"{COLOR_AMARILLO}¡Bienvenido a Pizzería Pythoni!{RESETEO_COLOR}")
print(
    f"{COLOR_VERDE}Comandos disponibles: 'pedir', 'extra', 'ver', 'pagar', 'salir'{RESETEO_COLOR}"
)

# --- INICIO DE PROGRAMA ---


def mostrar_seleccionado():
    print(f"--- {COLOR_AZUL}PIZZAS E INGREDIENTES SELECCIONADOS{RESETEO_COLOR} ---")

    print(f"--- {COLOR_ROJO}Pizzas{RESETEO_COLOR} ---")
    for pizza in carrito_pizzas:
        print(f"* {pizza}")

    print(f"--- {COLOR_ROJO}Ingredientes{RESETEO_COLOR} ---")
    for ingrediente in ingredientes_solicitados:
        print(f"* {ingrediente}")


def mostrar_menu():
    print("--- MENU ---")
    for pizza in menu:
        print(f"* {pizza}")
    print("------------")


def mostrar_stock_ingredientes():
    print("--- EXTRA ---")
    for ingrediente in stock_ingredientes:
        print(f"* {ingrediente}")
    print("------------")


def anadir_pizza(pizza):
    for i in range(len(menu)):
        if pizza in menu:
            carrito_pizzas.append(pizza)
            print(f"{COLOR_AZUL}Pizza {pizza} añadida al carrito{RESETEO_COLOR}")
            break


def anadir_ingrediente(ingrediente):
    ingredientes_solicitados.append(ingrediente)


continuar: bool = True
while continuar:
    print("----------")
    comando: str = input("¿Qué deseas hacer?\n-> ")
    match comando.lower():
        case "pedir":
            mostrar_menu()
            seleccion_pizza: str = input(
                "Cual de estas pizzas desea pedir?\nSelección: "
            )
            anadir_pizza(seleccion_pizza.title())
        case "extra":
            mostrar_stock_ingredientes()
            ingrediente_solicitado: str = input("Que ingrediente deseas extra?\n -> ")
            anadir_ingrediente(ingrediente_solicitado)
            print(
                f"{COLOR_VERDE}Ingrediente {ingrediente_solicitado} añadido al carrito{RESETEO_COLOR}"
            )
        case "ver":
            mostrar_seleccionado()
        case "pagar":
            break
        case "salir":
            print(f"{COLOR_AMARILLO}Mamma Mia{RESETEO_COLOR}")
            break
        case _:
            print(f"{COLOR_ROJO}Comando desconocido{RESETEO_COLOR}")
