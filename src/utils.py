from os import system, name


# Funcion para limpiar la consola
def clear():
    if name == 'nt':
        _ = system('cls')


# Función para "pausar" la ejecución de un programa hasta que el usuario pulse ENTER.
def pause():
    input("Pulsa ENTER para continuar...")