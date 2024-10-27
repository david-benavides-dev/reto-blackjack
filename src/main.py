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

BARAJA = "A234567890JKQ"

MODOS_JUEGO_VALIDOS = 1, 2

# Control de flujo para seleccionar el modo de juego:
# 1. usuario introduce input
# 2. valida entrada para entero
# 3. comprobacion si la entrada está en la constante modos_juego_validos
# 4. retorna variable valor que determina 1 o 2 jugadores
# NOTE: TERMINADO

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


def preguntar_modo_juego() -> bool:
    """
    
    """
    jugadores = None
    print("1. Dos jugadores.")
    print("2. Un jugador contra la máquina.")
    while jugadores is None:
        jugadores = pedir_num("Introduzca el modo de juego que deseas: ")
        if validar_modo_juego(jugadores) is True:
            if escojer_modo_juego(jugadores) == 1:
                return print("1PLAYER_TEST")
            return print("2PLAYER_TEST")
        print("**ERROR** Debes introducir un número correcto.")
        jugadores = None


def main():
    preguntar_modo_juego()


if __name__ == "__main__":
    main()