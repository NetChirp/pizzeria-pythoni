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
    git clone https://github.com/NetChirp/pizzeria-pythoni/
    cd pizzeria-pythoni
    ```

2.  Ejecuta el script de Python:
    ```bash
    python3 bot_pizzeria.py
    ``` 

