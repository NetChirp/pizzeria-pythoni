# 🍕 Pizzería Pythoni Bot 🤖

## Descripción del Proyecto

Este repositorio contiene la solución al ejercicio del **Bot de la Pizzería "Pythoni"**. El objetivo es simular el "cerebro" de un robot camarero que interactúa con un cliente para tomar un pedido de pizzas y extras.

El programa gestiona el proceso completo: desde la selección de pizzas del menú y la solicitud de ingredientes extra, hasta el procesamiento final del pedido, incluyendo la verificación de stock y la generación de un ticket final.

---

## 🚀 Características y Funcionalidades

El bot soporta los siguientes comandos interactivos en un bucle continuo:

- **`pedir`**: Muestra el menú de pizzas y permite añadir una pizza válida al carrito.
- **`extra`**: Muestra los ingredientes en stock y registra el ingrediente solicitado por el usuario (sin validar el stock inicialmente).
- **`ver`**: Muestra un resumen de las pizzas añadidas y los ingredientes extra solicitados hasta el momento.
- **`pagar`**: Finaliza el pedido, procesa los ingredientes extra, genera el ticket y finaliza el programa.
- **`salir`**: Finaliza el programa sin generar el ticket.

### ✨ Aspectos destacados del código

- **Estructura Modular:** Uso de **funciones (`def`)** para organizar el código (ej. `mostrar_menu`, `anadir_pizza`, `imprimir_ticket`).
- **Manejo de Comandos:** Implementación del _flow_ de la conversación mediante un **bucle `while`** y la estructura de control **`match/case`** para gestionar los comandos.
- **Limpieza de Datos:** Uso de una **List Comprehension** para filtrar eficientemente los ingredientes solicitados, verificando su existencia en el _stock_ e implementando un formato de título (`.title()`) para la salida final.
- **Experiencia de Usuario:** Uso de **secuencias de escape ANSI** (variables `COLOR_*`) para proporcionar _feedback_ visual con colores en la consola.

---

## 🛠️ Instalación y Uso

### Prerrequisitos

Necesitas tener **Python 3.10 o superior** instalado en tu sistema para ejecutar el programa (debido al uso de `match/case`).

### Ejecución

1.  Clona este repositorio:

    ```bash
    git clone [https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories](https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories)
    cd [nombre del repositorio]
    ```

2.  Ejecuta el script de Python:
    ```bash
    python bot_pizzeria.py
    ```

### Interacción

## Una vez que el programa se inicie, podrás interactuar con el bot usando los comandos disponibles. El bot te guiará a través del proceso de pedido:

## 📝 Código Clave (Fase 2: List Comprehension)

La limpieza y el filtrado de los ingredientes solicitados, que constituye la parte más importante del ejercicio, se realiza en el comando **`pagar`**:

```python
case "pagar":
    # 1. List Comprehension para filtrar y formatear
    ingredientes_finales = [
        ingrediente.title()
        for ingrediente in ingredientes_solicitados
        if ingrediente in stock_ingredientes
    ]

    # 2. Aviso de ingredientes eliminados
    if len(ingredientes_finales) < len(ingredientes_solicitados):
        print(
            f"{COLOR_AMARILLO}AVISO: Algunos ingredientes solicitados no están en stock y se han eliminado.{RESETEO_COLOR}"
        )

    # 3. Impresión del ticket
    imprimir_ticket()
    # ...
```
