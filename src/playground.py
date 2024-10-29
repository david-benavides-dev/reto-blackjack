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


def restar_carta_azar(baraja_juego) -> str:
    """
    
    """
    restar_carta = seleccionar_carta_azar(baraja_juego)
    if baraja_juego != "":
        baraja_juego = baraja_juego.replace(restar_carta, "", 1)
    return baraja_juego


def sumar_puntos_jugador(mano_jugador: str) -> int:
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
    
    """
    jugadores = None
    clear()
    print("1. Dos jugadores.")
    print("2. Un jugador contra la máquina.")
    while jugadores is None:
        jugadores = pedir_num("Introduzca el modo de juego que deseas: ")
        if validar_modo_juego(jugadores) is True:
            if escojer_modo_juego(jugadores) == 1:
                return 1
            return 2
        print("**ERROR** Debes introducir un número correcto.")
        jugadores = None


# TODO ver2 de coste carta maybe?
def coste_de_carta(carta) -> int:
    if carta == "A":
        return 1
    elif "2" <= carta <= "9":
        return int(carta)
    elif carta in "0JQK":
        return 10


def coste_de_carta_2(carta) -> int:
    # TODO Simplificar el resultado <- DONE en ver2 maybe?
    """
    
    """
    if carta == "A":
        carta = 1
    elif carta == "2":
        carta = 2
    elif carta == "3":
        carta = 3
    elif carta == "4":
        carta = 4
    elif carta == "5":
        carta = 5
    elif carta == "6":
        carta = 6
    elif carta == "7":
        carta = 7
    elif carta == "8":
        carta = 8
    elif carta == "9":
        carta = 9
    elif carta in "0JQK":
        carta = 10
    return carta


def jugar(modo_juego: int):
    """
    
    """
    if modo_juego == 1:
        # Crea la partida, generando el mazo y creando variables default para cada jugador / reglas del juego.

        rondas = 0
        global mazo_inicial
        mazo_inicial = generar_mazo()
        clear()
        # Preguntamos y establecemos los nombres del jugador 1 y 2.
        # TODO Crear funcion para crear y formatear los nombres correctamente.
        nombre_jugador_1 = input("Introduce el nombre del jugador uno: ").strip()
        if nombre_jugador_1 == "":
            nombre_jugador_1 = "jugador_1"
        nombre_jugador_1 = "J1 - " + nombre_jugador_1
        print(f"{nombre_jugador_1}\n")

        nombre_jugador_2 = input("Introduce el nombre del jugador dos: ").strip()
        if nombre_jugador_2 == "":
            nombre_jugador_2 = "jugador_2"
        nombre_jugador_1 = "J1 - " + nombre_jugador_2
        print(f"{nombre_jugador_2}")

        input("¿Comenzar juego?...")
        clear()

        # Inicializamos la mano de los dos jugadores con dos empty strings
        mano_jugador_1 = ""
        mano_jugador_2 = ""

        while rondas < 3:
            # if rondas == 3:
                mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)
                mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)
                print(mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1))
                print(mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2))
                rondas +=1
                input()





        


def main():
    empezar_juego = None
    while empezar_juego is None:
        modo_juego = preguntar_modo_juego()
        jugar(modo_juego)


    # jugar()
    # carta_A = "A"
    # carta_1 = "1"
    # carta_K = "K"
    # carta_2 = "2"
    # carta_0 = "0"


    # print(coste_de_carta(carta_A))
    # print(coste_de_carta(carta_1))
    # print(coste_de_carta(carta_K))
    # print(coste_de_carta(carta_2))
    # print(coste_de_carta(carta_0))


if __name__ == "__main__":
    main()