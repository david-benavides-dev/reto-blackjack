# Al entrar debe preguntar el modo de juego:
#     1. Dos jugadores.
#     2. Un jugador contra la máquina.
# Premisas generales:
#     El código debe estar escrito en Python.
#     No se pueden usar listas, tuplas o diccionarios. Evitar sentencias while True, break, continue y pass.
#     Código legible y buenas prácticas de programación, incluyendo el principio de responsabilidad única, nombres de métodos y variables correctas y descriptivas con nomenclatura camelCase o palabras separadas por "_".
#     Entregar el programa junto con pruebas unitarias de las funciones utilizadas.
#     Para corregirlo, el programa debe pasar los test que se hayan diseñado.
#     Para las pruebas a funciones que contengan un input() ver Pruebas Unitarias con "monkeypatch" y "capfd".
#     Se deben realizar todas las comprobaciones necesarias para que el programa no genere errores/excepciones.
#     El programa debe estar documentado/comentado con docstrings y comentarios internos. Ver Documentar el código
#     Si se detecta copia entre retos o de cualquier otra fuente, la entrega quedará eliminada.
# ### Objetivo del juego:
# 	Conseguir 21 puntos o plantarse con más puntos que el otro jugador.
# ### Funcionamiento:
# 	1. Gana el jugador que tenga la puntuación más alta sin pasarse de 21 puntos.
# 	2. La baraja de cartas es la cadena de caracteres "A234567890JKQ". Las cartas tienen los siguientes puntos:
# 		A -> 1 o 10 (según le venga mejor al resto de cartas que tiene en su poder el jugador)
# 		2...9 -> el propio valor del número.
# 		0, J, Q, K -> 10
  
# 	3. Cada jugador irá solicitando cartas por turnos, después del primer turno obligatorio, un jugador puede plantarse cuando lo decida.
# 	4. Después de cada turno, se debe mostrar la información de la ronda o turno, las cartas y puntos de cada jugador:
# 		RONDA 3
# 		J1 - jugador1 - A3K (14)
# 		J2 - jugador2 - A44 (18)
  
# 	5. Cuando un jugador se pasa de 21, automáticamente pierde y gana el otro jugador.
# 	6. Las cartas de los jugadores y puntuaciones se revelan a la vez después de pasar el turno ambos jugadores, es decir, cada jugador decide pedir una carta más o plantarse y a continuación se muestra la información de cada jugador.
#  		RONDA 3
# 		J1 - jugador1 - 63K (19)
# 		J2 - jugador2 - J4Q **se pasa**
# 	7. El programa debe solicitar el modo de juego y a continuación el nombre o apodo del o los jugadores.
# 	8. Cada jugador pide una carta por turno o se planta. Como mínimo un jugador debe solicitar una carta, es decir, la primera vez no se le da la opción a plantarse. Pero el resto de turnos si.
# 	9. El juego acaba cuando ambos jugadores se plantan. Mientras que un jugador no se pase de 21 puntos y no se plante se debe preguntar si quiere una carta más.
# 	10. Cuando finaliza el juego se debe mostrar lo siguiente (4 posibilidades):
# 
# JUEGO TERMINADO - Ronda 3
# Game over ¡Los dos os habéis pasado!
# J1 - jugador1 - 4K9 (23)
# J2 - jugador2 - J70 (27)
# 
# JUEGO TERMINADO - Ronda 3
# ¡Empate!
# J1 - jugador1 - 4K5 (19)
# J2 - jugador2 - A9 (19)
# 
# JUEGO TERMINADO - Ronda 3
# ¡Gana J1 - jugador1!
# J1 - jugador1 - JQA (21)
# J2 - jugador2 - 491J (24)
# 
# JUEGO TERMINADO - Ronda 3
# ¡Gana J2 - jugador2!
# J1 - jugador1 - 3K5 (18)
# J2 - jugador2 - 28Q (20)

from random import randint
from utils import *

TITULOS = ("Juguemos al Blackjack",
            "Configuración inicial - Dos jugadores",
            "Configuración inicial - Un jugador contra la máquina")

BARAJA = "A234567890JKQ"
MODOS_JUEGO_VALIDOS = 1, 2


def generar_mazo() -> str:
    """
    
    """
    baraja_completa: str = ""
    for _ in range (4):
        baraja_completa += BARAJA
    return baraja_completa


def seleccionar_carta_azar(baraja_juego) -> str:
    """
    
    """
    if baraja_juego != "":
        return baraja_juego[randint(0, len(baraja_juego) - 1)]
    return ""


def sumar_puntos_jugador(mano_jugador: str) -> int|str:
    """
    
    """
    coste_total = 0
    for cartas in mano_jugador:
        coste_total += coste_de_carta(cartas)
    
    return coste_total


def sumar_cartas_jugador(mano_jugador: str) -> str:
    """
    
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
    
    """
    return f"{nombre_jugador} - {mano_jugador} ({(sumar_puntos_jugador(mano_jugador))})"


def pedir_num(msg: str) -> int:
    """
    
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
    
    """
    try:
        int(numero)
        return True
    except ValueError:
        return False


def validar_modo_juego(modo_juego: int) -> bool:
    """
    
    """
    if modo_juego not in MODOS_JUEGO_VALIDOS:
        return False
    return True


def escojer_modo_juego(opcion_modo_juego: int) -> bool:
    """
    
    """
    if opcion_modo_juego == MODOS_JUEGO_VALIDOS[0]:
        return 1
    return 2


def preguntar_modo_juego() -> int:
    """
    Pregunta al usuario qué modelo de juego desea inicializar, siendo 1 para dos jugadores y 2 para jugar contra un NPC.
    Returns:
        int: El modelo de juego elegido.
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


def coste_de_carta(carta) -> int:
    """
    
    """
    if carta == "A":
        return 1
    elif "2" <= carta <= "9":
        return int(carta)
    elif carta in "0JQK":
        return 10


# Función para definir el nombre del jugador en concreto.
def definir_nombre_jugador(modo_juego: int, numero_jugador = "") -> str:
    """
    
    """
    print(mostrar_titulo(TITULOS, modo_juego))
    if modo_juego == 1:
        nombre_jugador = input(f"Introduce el nombre del jugador {numero_jugador}: ").strip().capitalize()
        if nombre_jugador == "":
            nombre_jugador = f"jugador_{numero_jugador}"
    else:
        nombre_jugador = f"MAQUINA"
    nombre_jugador = f"J{numero_jugador} - " + nombre_jugador
    clear()
    return nombre_jugador


# Función que irá mostrando la información de cada ronda.
def mostrar_info_ronda(rondas: int, nombre_jugador_1: str, nombre_jugador_2: str, mano_jugador_1: str, mano_jugador_2: str, resultado_victoria:int = 0) -> str:
    """

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

        if input("\n¿Jugar de nuevo?\nS/N: ").lower() == "s":
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
        nombre_jugador_1 = definir_nombre_jugador(1, numero_jugador = "1")
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

        if input("\n¿Jugar de nuevo?\nS/N: ").lower() in "s" or "si":
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