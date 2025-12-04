# --- MIS CONSTANTES ---
COLOR_AZUL: str = "\033[34m"
COLOR_AMARILLO: str = "\033[33m"
COLOR_VERDE: str = "\033[32m"
COLOR_ROJO: str = "\033[31m"
RESETEO_COLOR:str = "\033[0m"

# --- DATOS INICIALES ---
menu = ["Margarita", "Cuatro Quesos", "Pepperoni", "Hawaiana"]
stock_ingredientes = ["queso", "tomate", "cebolla", "aceitunas", "champiñones", "jamon"]

carrito_pizzas = []
ingredientes_solicitados = []  # Aquí entra todo lo que escriba el usuario. Tanto correcto como incorrecto.

print(f"{COLOR_AMARILLO}¡Bienvenido a Pizzería Pythoni!{RESETEO_COLOR}")
print(f"{COLOR_VERDE}Comandos disponibles: 'pedir', 'extra', 'ver', 'pagar', 'salir'{RESETEO_COLOR}")

# --- INICIO DE PROGRAMA ---

def mostrar_menu():
    print("--- MENU ---")
    for i in menu:
        print(i)
    print("------------")

def comprobar_pizza(pizza):
    for i in range(len(menu)):
        if menu[i] == pizza:
            carrito_pizzas.append(pizza)


continuar: bool = True
while continuar:
    print("----------")
    comando: str = input("¿Qué deseas hacer?\nAcción: ")
    match comando.lower():
        case "pedir":
            mostrar_menu()
            seleccion_pizza: str = input("Cual de estas pizzas desea pedir?\nSelección: ")

        case "extra":
            pass
        case "ver":
            pass
        case "pagar":
            pass
        case "salir":
            pass
        case _:
            print(f"{COLOR_ROJO} Comando desconocido {RESETEO_COLOR}")
