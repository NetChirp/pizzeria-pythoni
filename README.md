

# El bot de la pizzería "Pythoni"

## Objetivo
Vas a programar el "cerebro" de un robot camarero. Tu programa debe mantener una conversación con el cliente para tomar su pedido y, al final, limpiar los datos para enviarlos a cocina.

> **Importante:** Puedes (y se recomienda) usar funciones (`def`) para organizar mejor tu código.  
> Por ejemplo, podrías tener funciones como `pedir_pizza`, `añadir_extra`, `ver_pedido`, `generar_ticket`, etc.

## Código inicial (Copia y pega)
Empieza tu fichero `bot_pizzeria.py` con estos datos. No pierdas tiempo inventando el menú.

```python
# --- DATOS INICIALES ---
menu = ["Margarita", "Cuatro Quesos", "Pepperoni", "Hawaiana"]
stock_ingredientes = ["queso", "tomate", "cebolla", "aceitunas", "champiñones", "jamon"]

carrito_pizzas = []
ingredientes_solicitados = []  # Aquí entra todo lo que escriba el usuario. Tanto correcto como incorrecto.

print("¡Bienvenido a Pizzería Pythoni!")
print("Comandos disponibles: 'pedir', 'extra', 'ver', 'pagar', 'salir'")
````

---

## Fase 1: La conversación (Bucle y `match`)

Crea un **bucle infinito** que pregunte constantemente: `¿Qué deseas hacer?`.  
Usa `match` para reaccionar a los siguientes comandos (convierte la entrada a minúsculas para evitar errores):

1. **`pedir`**    
    - Muestra el menú.
    - Pregunta el nombre de la pizza.
    - Si existe en `menu`, agrégala a `carrito_pizzas`.
    - Si no, muestra un mensaje indicando que no existe.
2. **`extra`**
    - Pregunta qué ingrediente quiere.
    - **IMPORTANTE:** Agrégalo a `ingredientes_solicitados` tal cual lo escriba el usuario, sin comprobar si existe en el stock todavía.
3. **`ver`**
    - Muestra las pizzas pedidas y los extras solicitados hasta el momento.
4. **`pagar`** o **`salir`**
    - Rompe el bucle para finalizar la toma de pedidos.
5. **Cualquier otra cosa**
    - Muestra un mensaje de error: `"Comando desconocido"`.

---

## Fase 2: El filtro de cocina (List Comprehension)

Cuando el cliente decida `pagar` y el bucle termine, debes procesar los datos:

1. Usa una **List Comprehension** para crear una nueva lista llamada `ingredientes_finales`:    
    - Debe contener **solo** los ingredientes solicitados que realmente existan en `stock_ingredientes`.
    - Al guardarlos, asegúrate de que tengan la primera letra mayúscula (formato Título, por ejemplo `"queso"` → `"Queso"`).
2. Si la lista final es más pequeña que la lista solicitada, imprime un aviso:  
    _`"AVISO: Algunos ingredientes solicitados no están en stock y se han eliminado."`_

---

## Fase 3: El ticket

Imprime el resumen final:

- Lista de Pizzas.
- Lista de Ingredientes Extra (la lista **limpia y filtrada**, es decir, `ingredientes_finales`).
Puedes crear una función `imprimir_ticket(carrito_pizzas, ingredientes_finales)` para esta parte.

---

## Ejemplos de salida esperada

### Ejemplo 1: El cliente perfecto (Todo existe)

```bash
¡Bienvenido a Pizzería Pythoni!
Comandos disponibles: 'pedir', 'extra', 'ver', 'pagar', 'salir'

¿Qué deseas hacer? -> PEDIR
Menú: ['Margarita', 'Cuatro Quesos', 'Pepperoni', 'Hawaiana']
Nombre de la pizza: margarita
Margarita añadida.

¿Qué deseas hacer? -> extra
¿Qué ingrediente extra quieres añadir? queso
Anotado: queso (Confirmaremos disponibilidad al pagar).

¿Qué deseas hacer? -> pagar
Cerrando pedido y enviando a cocina...

==============================
      TICKET FINAL      
==============================
Pizzas:
- Margarita

Ingredientes Extra Válidos:
Queso
==============================
```

### Ejemplo 2: El cliente confuso (Filtro en acción)

```bash
¿Qué deseas hacer? -> pedir
Nombre de la pizza: Carbonara
Lo siento, esa pizza no está en el menú.

¿Qué deseas hacer? -> pedir
Nombre de la pizza: Pepperoni
Pepperoni añadida.

¿Qué deseas hacer? -> extra
¿Qué ingrediente extra quieres añadir? jamon
Anotado: jamon (Confirmaremos disponibilidad al pagar).

¿Qué deseas hacer? -> extra
¿Qué ingrediente extra quieres añadir? cerveza
Anotado: cerveza (Confirmaremos disponibilidad al pagar).

¿Qué deseas hacer? -> extra
¿Qué ingrediente extra quieres añadir? unicornio
Anotado: unicornio (Confirmaremos disponibilidad al pagar).

¿Qué deseas hacer? -> ver
Pizzas: ['Pepperoni']
Extras pendientes de revisión: ['jamon', 'cerveza', 'unicornio']

¿Qué deseas hacer? -> pagar
Cerrando pedido y enviando a cocina...

AVISO: Algunos ingredientes solicitados no están en stock y se han eliminado.

==============================
      TICKET FINAL      
==============================
Pizzas:
- Pepperoni

Ingredientes Extra Válidos:
Jamon
==============================
```
