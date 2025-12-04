# --- MIS CONSTANTES ---
COLOR_AZUL = "\033[34m"
COLOR_AMARILLO = "\033[33m"
COLOR_VERDE = "\033[32m"
COLOR_ROJO = "\033[31m"
RESETEO_COLOR = "\033[0m"

# --- DATOS INICIALES ---
menu = ["Margarita", "Cuatro Quesos", "Pepperoni", "Hawaiana"]
stock_ingredientes = ["queso", "tomate", "cebolla", "aceitunas", "champiñones", "jamon"]

carrito_pizzas = []
ingredientes_solicitados = []  # Aquí entra todo lo que escriba el usuario. Tanto correcto como incorrecto.

print(f"{COLOR_AMARILLO}¡Bienvenido a Pizzería Pythoni!{RESETEO_COLOR}")
print(f"{COLOR_VERDE}Comandos disponibles: 'pedir', 'extra', 'ver', 'pagar', 'salir'{RESETEO_COLOR}")

# --- INICIO DE PROGRAMA ---

def mostrar_menu():
    for i in range(len(menu)):
        print(menu[i])


continuar: bool = True
while continuar:
    mostrar_menu()
    print("----------")
    comando: str = input("¿Qué deseas hacer?")
    match comando.lower():
        case "pedir":
            pass
        case "extra":
            pass
        case "ver":
            pass
        case "pagar":
            pass
        case "salir":
            pass
        case _:
            print(f"{COLOR_ROJO} Opción no valida!{RESETEO_COLOR}")
