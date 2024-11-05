# TODO: 
# - Hacer un cálculo diferente para el As dependiendo del valor total de la mano del jugador en cuestión.
# - Documentar todo el código.
# - Cleanup.
# - Pruebas unitarias siguiendo el cálculo de pruebas válidas y no válidas.

# NOTE:
# - Cambiar la funcion definir_nombre_jugador para el modo vs máquina. <- DONE

from random import randint
from utils import *

TITULOS = ("Juguemos al Blackjack",
            "Configuración inicial - Dos jugadores",
            "Configuración inicial - Un jugador contra la máquina")

BARAJA = "A234567890JKQ"
MODOS_JUEGO_VALIDOS = 1, 2


def generar_mazo() -> str:
    """Genera un mazo multiplicando el valor de la constante BARAJA cuatro veces, asignandole el valor total a baraja_completa.

    Returns:
        str: La baraja completa.
    """
    baraja_completa: str = ""
    for _ in range (4):
        baraja_completa += BARAJA
    return baraja_completa


def seleccionar_carta_azar(baraja_juego) -> str:
    """

    Args:
        bajara_juego (str): 

    Returns:
        baraja_juego (str): 
    """
    if baraja_juego != "":
        return baraja_juego[randint(0, len(baraja_juego) - 1)]
    return ""


def sumar_puntos_jugador(mano_jugador: str) -> int:
    """

    Args:
        mano_jugador (str): 

    Returns:
        coste_total (int): 
    """
    coste_total = 0
    for cartas in mano_jugador:
        coste_total += coste_de_carta(cartas)
    
    return coste_total


def sumar_cartas_jugador(mano_jugador: str) -> str:
    """

    Args:
        mano_jugador (str): 

    Returns:
        mano_jugador (str): 
    """
    global mazo_inicial
    if mazo_inicial == "":
        print("No hay cartas en el mazo.")
        return mano_jugador
    carta = seleccionar_carta_azar(mazo_inicial)
    mazo_inicial = mazo_inicial.replace(carta, "", 1)
    mano_jugador += carta
    return mano_jugador


def mostrar_mano_jugador(nombre_jugador: str, mano_jugador: str) -> str:
    """

    Args:
        nombre_jugador (str): 
        mano_jugador (str): 

    Returns:
        str: 
    """
    return f"{nombre_jugador} - {mano_jugador} ({(sumar_puntos_jugador(mano_jugador))})"


def pedir_num(msg: str) -> int:
    """

    Args:
        msg (str): 

    Returns:
        int: 
    """
    numero = None
    while numero == None:
        numero = input(msg)
        if validar_num(numero):
            return int(numero)
        else:
            print("**ERROR** Debes introducir un número correcto.")
            numero = None


def validar_num(numero: str) -> bool:
    """

    Args:
        numero (str): 

    Returns:
        bool: 
    """
    try:
        int(numero)
        return True
    except ValueError:
        return False


def validar_modo_juego(modo_juego: int) -> bool:
    """

    Args:
        modo_juego (int): 

    Returns:
        bool: 
    """
    if modo_juego not in MODOS_JUEGO_VALIDOS:
        return False
    return True


def escojer_modo_juego(opcion_modo_juego: int) -> bool:
    """

    Args:
        opcion_modo_juego (int): 

    Returns:
        int: 
    """
    if opcion_modo_juego == MODOS_JUEGO_VALIDOS[0]:
        return 1
    return 2


def preguntar_modo_juego() -> int:
    """Solicita al usuario el modo de juego desea, siendo 1 para dos jugadores y 2 para jugar contra un NPC.

    Returns:
        int: El modo de juego elegido.
    """
    jugadores = None
    clear()
    print(mostrar_titulo(TITULOS, 0))
    print("1. Dos jugadores.")
    print("2. Un jugador contra la máquina.")
    while jugadores is None:
        try:
            jugadores = pedir_num("\nIntroduzca el modo de juego que deseas: ")
            if validar_modo_juego(jugadores) is True:
                if escojer_modo_juego(jugadores) == 1:
                    return 1
                return 2
        except ValueError:
            print("**ERROR** Debes introducir un número correcto.")


def coste_de_carta(carta: str) -> int:
    """
    Calcula el valor de la carta pasada por parámetro según las reglas del Blackjack:
    - La carta 'A' tiene un coste de 11.
    - Las cartas del 2 al 9 tienen un coste igual a su número.
    - Las cartas '0', 'J', 'Q' y 'K' tienen un coste de 10.

    Args:
        carta (str): La carta cuyo coste se va a calcular.

    Returns:
        int: El coste asociado a la carta proporcionada.
    """
    if carta == "A":
        return 11
    elif "2" <= carta <= "9":
        return int(carta)
    elif carta in "0JQK":
        return 10


# Función para definir el nombre del jugador en concreto.
def definir_nombre_jugador(modo_juego: int, numero_jugador = "") -> str:
    """

    Args:
        modo_juego (int): 
        numero_jugador (str): 

    Returns:
        nombre_jugador (str): 
    """
    print(mostrar_titulo(TITULOS, modo_juego))
    nombre_jugador = input(f"Introduce el nombre del jugador {numero_jugador}: ").strip().capitalize()
    if nombre_jugador == "":
        nombre_jugador = f"jugador_{numero_jugador}"
    nombre_jugador = f"J{numero_jugador} - " + nombre_jugador
    clear()
    return nombre_jugador


def mostrar_info_ronda(rondas: int, nombre_jugador_1: str, nombre_jugador_2: str, mano_jugador_1: str, mano_jugador_2: str, resultado_victoria:int = 0) -> str:
    """Función que irá mostrando la información de cada ronda.

    Args:
        rondas (int): 
        nombre_jugador_1 (str):
        nombre_jugador_2 (str):
        mano_jugador_1 (str):
        mano_jugador_2 (str):
        resultado_victoria (int):

    Returns:
        str:
    """
    rondas_string = ""


    if rondas == 1:
        rondas_string = f"Inicio de partida - Ronda {rondas}"
        informacion_partida = f"{rondas_string}\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2)}"
    elif rondas == 4:
        rondas_string = f"JUEGO TERMINADO - Ronda {rondas - 1}"
        informacion_partida = f"{rondas_string}\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2)}"
    else:
        rondas_string = f"Ronda {rondas}"
        informacion_partida = f"{rondas_string}\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2)}"


    if resultado_victoria == 1:
        informacion_partida = f"{rondas_string}\n\n¡Gana {nombre_jugador_1}!\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2)}"

    elif resultado_victoria == 2:
        informacion_partida = f"{rondas_string}\n\n¡Gana {nombre_jugador_2}!\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2)}"

    elif resultado_victoria == 3:
        informacion_partida = f"{rondas_string}\n\n¡Empate!\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2)}"
    
    elif resultado_victoria == 4:
        informacion_partida = f"{rondas_string}\n\nGame over ¡Los dos os habéis pasado!\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2)}"

    return informacion_partida


# Función para printear el título del flujo actual del programa.
def mostrar_titulo(TITULOS: str, pos_titulo: int) -> str:
    """

    """
    titulo = TITULOS[pos_titulo]
    return titulo + "\n"


# Funcion para determinar el ganador.
def condicion_victoria(mano_jugador_1, mano_jugador_2) -> int:
    """

    """
    # resultado_victoria 1: Gana jugador 1
    # resultado_victoria 2: Gana jugador 2
    # resultado_victoria 3: Empate
    # resultado_victoria 4: Doble derrota


    puntos_jugador_1 = sumar_puntos_jugador(mano_jugador_1)
    puntos_jugador_2 = sumar_puntos_jugador(mano_jugador_2)


    if puntos_jugador_1 == puntos_jugador_2:
        resultado_victoria = 3

    elif puntos_jugador_1 > 21 and puntos_jugador_2 > 21:
        resultado_victoria = 4

    elif puntos_jugador_1 > 21:
        resultado_victoria = 2

    elif puntos_jugador_2 > 21:
        resultado_victoria = 1
    
    elif puntos_jugador_1 - 21 > puntos_jugador_2 - 21:
        resultado_victoria = 1

    elif puntos_jugador_1 - 21 < puntos_jugador_2 - 21:
        resultado_victoria = 2

    return resultado_victoria


# Función para empezar a jugar
def jugar(modo_juego: int):
    """
    
    """
    global mazo_inicial

    if modo_juego == 1:
        # Crea la partida, generando el mazo y creando variables default para cada jugador / reglas del juego.

        mazo_inicial = generar_mazo()
        clear()

        # Preguntamos y establecemos los nombres del jugador 1 y 2.
        nombre_jugador_1 = definir_nombre_jugador(modo_juego, numero_jugador = "1")
        nombre_jugador_2 = definir_nombre_jugador(modo_juego, numero_jugador = "2")

        print(f"Los jugadores de esta partida son:\n\n{nombre_jugador_1}\n{nombre_jugador_2}")
        input("\nPulsa ENTER para comenzar el juego...")
        clear()

        # Inicializamos la mano de los dos jugadores con dos empty strings
        mano_jugador_1 = ""
        mano_jugador_2 = ""

        # En la primera ronda, los dos jugadores comienzan con una carta
        mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)
        mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)

        # Inicio de las rondas.
        rondas = 1
        while rondas <= 3:
            clear()
            print(mostrar_info_ronda(rondas, nombre_jugador_1, nombre_jugador_2, mano_jugador_1, mano_jugador_2))
            opcion = input(f"\nJUGADOR {nombre_jugador_1} - ¿Quieres carta?: ").strip().lower()
            if opcion == "s" or opcion == "si":
                mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)

            opcion = input(f"\nJUGADOR {nombre_jugador_2} - ¿Quieres carta?: ").strip().lower()
            if opcion == "s" or opcion == "si":
                mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)

            rondas += 1


        clear()
        print(mostrar_info_ronda(rondas, nombre_jugador_1, nombre_jugador_2, mano_jugador_1, mano_jugador_2))
        input("\n")

        jugador_ganador = condicion_victoria(mano_jugador_1, mano_jugador_2)

        clear()
        print(mostrar_info_ronda(4, nombre_jugador_1, nombre_jugador_2, mano_jugador_1, mano_jugador_2, jugador_ganador))

        if input("\n¿Jugar de nuevo?\nS/N: ").capitalize() == "S":
            modo_juego = preguntar_modo_juego()
            jugar(modo_juego)
        else:
            print("Bye bye...")
            exit()


#####################################################################################################################################
#####################################################################################################################################


    elif modo_juego == 2:
        # Crea la partida, generando el mazo y creando variables default para cada jugador / reglas del juego.
        mazo_inicial = generar_mazo()
        clear()

        # Preguntamos y establecemos el nombre del jugador 1
        nombre_jugador_1 = definir_nombre_jugador(2, numero_jugador = "1")
        nombre_jugador_2 = f"J2 - MAQUINA"

        print(f"Los jugadores de esta partida son:\n\n{nombre_jugador_1}\n{nombre_jugador_2}")
        input("\nPulsa ENTER para comenzar el juego...")
        clear()

        # Inicializamos la mano de los dos jugadores con dos empty strings
        mano_jugador_1 = ""
        mano_jugador_2 = ""

        # En la primera ronda, los dos jugadores comienzan con una carta
        mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)
        mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)

        # Inicio de las rondas.
        rondas = 1
        while rondas <= 3:
            clear()
            print(mostrar_info_ronda(rondas, nombre_jugador_1, nombre_jugador_2, mano_jugador_1, mano_jugador_2))
            opcion = input(f"\nJUGADOR {nombre_jugador_1} - ¿Quieres carta?: ").strip().lower()
            if opcion == "s" or opcion == "si":
                mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)

            opcion_maquina = randint(0,100)
            if opcion_maquina > 50:
                mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)

            rondas += 1


        clear()
        print(mostrar_info_ronda(rondas, nombre_jugador_1, nombre_jugador_2, mano_jugador_1, mano_jugador_2))
        input("\n")

        jugador_ganador = condicion_victoria(mano_jugador_1, mano_jugador_2)

        clear()
        print(mostrar_info_ronda(4, nombre_jugador_1, nombre_jugador_2, mano_jugador_1, mano_jugador_2, jugador_ganador))

        if input("\n¿Jugar de nuevo?\nS/N: ").capitalize() == "S":
            modo_juego = preguntar_modo_juego()
            jugar(modo_juego)
        else:
            print("Bye bye...")
            exit()

def main():
    modo_juego = preguntar_modo_juego()
    jugar(modo_juego)


if __name__ == "__main__":
    main()