# TODO: 
# - Cleanup.
# - Pruebas unitarias siguiendo el cálculo de pruebas válidas y no válidas.

from random import randint
from os import system, name

TITULOS = ("Juguemos al Blackjack",
            "Configuración inicial - Dos jugadores",
            "Configuración inicial - Un jugador contra la máquina")

BARAJA = "A234567890JKQ"
PALOS = "♠♥♦♣"

MODOS_JUEGO_VALIDOS = 1, 2


def clear():
    """
    Limpia la terminal.
    """
    if name == 'nt':
        _ = system('cls')


def pause():
    """
    Hace una pausa hasta que el usuario pulsa la tecla ENTER.
    """
    input("Pulsa ENTER para continuar...")


def generar_mazo() -> str:
    """
    Genera un mazo multiplicando el valor de la constante BARAJA cuatro veces, asignandole el valor total junto a su respectivo palo a baraja_completa.

    Returns:
        str: La baraja completa.
    """
    baraja_completa = ""

    for palo in PALOS:
        for carta in BARAJA:
            baraja_completa += carta + palo
    
    return baraja_completa


def seleccionar_carta_azar(baraja_juego) -> str:
    """
    Selecciona una carta al azar de la baraja del mazo y la devuelve junto a su palo.

    Args:
        baraja_juego (str): Una cadena que representa todas las cartas del mazo.

    Returns:
        str: La carta seleccionada junto a su palo.
    """
    if baraja_juego == "":
            return ""
    
    indice_carta = range(0, len(baraja_juego), 2)

    carta_random = randint(0, len(indice_carta) - 1)
    
    carta = baraja_juego[indice_carta[carta_random]]
    
    palo = baraja_juego[indice_carta[carta_random] + 1]
    
    return carta + palo


def sumar_puntos_jugador(mano_jugador: str) -> int:
    """
    Itera por la mano del jugador y devuelve el total de puntos respecto a la suma de las cartas que tenga.

    Args:
        mano_jugador (str): La mano del jugador.

    Returns:
        coste_total (int): La suma total de puntos que tiene la mano del jugador
    """
    coste_total = 0
    for cartas in mano_jugador:
        coste_total += coste_de_carta(cartas, coste_total)
    
    return coste_total


def sumar_cartas_jugador(mano_jugador: str) -> str:
    """
    Recibe la mano del jugador, le suma una carta al azar y la resta a su vez del mazo de juego.

    Si el mazo está vacío, muestra un mensaje y no realiza ningún cambio.

    Args:
        mano_jugador (str): La mano actual del jugador

    Returns:
        mano_jugador (str): La mano del jugador actualizada con la nueva carta seleccionada al azar.
    """
    global mazo_inicial

    if mazo_inicial == "":
        print("No hay cartas en el mazo.")
        return mano_jugador

    carta = seleccionar_carta_azar(mazo_inicial)

    mazo_inicial = mazo_inicial.replace(carta, "", 1)

    mano_jugador += carta

    return mano_jugador


def mostrar_mano_jugador(nombre_jugador: str, mano_jugador: str, resultado_victoria: int) -> str:
    """
    Muestra el número, nombre, cartas y puntuación total del jugador.

    Ejemplo: "J1 - jugador_1 - 0♠3♥2♦5♣ (20)"

    Args:
        nombre_jugador (str): El nombre del jugador.
        mano_jugador (str): Las cartas que tiene el jugador en la mano.
        resultado_victoria (int): Indica si la partida ha finalizado.

    Returns:
        str: Cadena con el nombre del jugador, las cartas en su mano y su puntuación total.
    """
    puntos = sumar_puntos_jugador(mano_jugador)

    if puntos > 21 and resultado_victoria == 0:
        return f"{nombre_jugador} - {mano_jugador} (**se pasa**)"
    else:
        return f"{nombre_jugador} - {mano_jugador} ({(puntos)})"


def pedir_num(msg: str) -> int:
    """
    Solicita al usuario que ingrese un número válido y lo devuelve.

    Seguirá solicitando entrada hasta que se introduzca un número correcto.

    Args:
        msg (str): El mensaje que se muestra al usuario a la hora de solicitar la entrada.

    Returns:
        int: El número ingresado por el usuario, convertido a entero.
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
    Valida si el parámetro introducido puede convertirse a un entero, retornando False en caso contrario.

    Args:
        numero (str): La cadena a validar.

    Returns:
        bool: True si el string es número válido, False en caso contrario.
    """
    try:
        int(numero)
        return True
    except ValueError:
        return False


def validar_modo_juego(modo_juego: int) -> bool:
    """
    Valida si el modo de juego seleccionado es válido.

    Esta función verifica si el modo de juego proporcionado está en la lista de modos de juego válidos (`MODOS_JUEGO_VALIDOS`).
    Si el modo de juego es válido, la función devuelve `True`; de lo contrario, devuelve `False`.

    Args:
        modo_juego (int): El modo de juego a validar.

    Returns:
        bool: 
            - `True` si el modo de juego es válido.
            - `False` si el modo de juego no es válido.
    """
    if modo_juego not in MODOS_JUEGO_VALIDOS:
        return False
    return True


def escojer_modo_juego(opcion_modo_juego: int) -> bool:
    """
    Selecciona el modo de juego basado en la opción proporcionada.

    Esta función evalúa la opción proporcionada (`opcion_modo_juego`) y devuelve un valor que representa el modo de juego seleccionado.
    Si la opción es válida (es igual al primer valor de `MODOS_JUEGO_VALIDOS`), la función retorna 1. En caso contrario, retorna 2.

    Args:
        opcion_modo_juego (int): La opción de modo de juego seleccionada por el usuario.

    Returns:
        int: 
            - 1 si la opción corresponde al primer modo de juego válido.
            - 2 si la opción no corresponde al primer modo de juego válido.
    """
    if opcion_modo_juego == MODOS_JUEGO_VALIDOS[0]:
        return 1
    return 2


def preguntar_modo_juego() -> int:
    """
    Solicita al usuario el modo de juego desea, siendo 1 para dos jugadores y 2 para jugar contra un NPC.

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


def coste_de_carta(carta: str, puntuacion: int) -> int:
    """
    Calcula el valor de la carta pasada por parámetro según las reglas del Blackjack:
    - La carta 'A' tiene un coste de 11 de base (salvo que la puntuación del jugador vaya a exceder 21, en cuyo caso su coste es 1)
    - Las cartas del 2 al 9 tienen un coste igual a su número.
    - Las cartas '0', 'J', 'Q' y 'K' tienen un coste de 10.

    Args:
        carta (str): La carta cuyo coste se va a calcular.

    Returns:
        int: El coste asociado a la carta proporcionada.
    """
    if carta == "A":
        if puntuacion + 11 > 21:
            return 1
        return 11
    elif "2" <= carta <= "9":
        return int(carta)
    elif carta in "0JQK":
        return 10
    else:
        return 0 #TODO


def definir_nombre_jugador(modo_juego: int, numero_jugador: str = "") -> str:
    """
    Solicita al usuario el nombre del jugador y lo formatea según el número del jugador y el modo de juego.

    Si no se ingresa un nombre, se utiliza un valor por defecto.

    Args:
        modo_juego (int): El modo de juego actual, utilizado para mostrar el título correspondiente.
        numero_jugador (str, opcional): El número del jugador que se está definiendo (por defecto es una cadena vacía).

    Returns:
        str: El nombre del jugador, formateado como "J{numero_jugador} - {nombre_jugador}".
    """
    print(mostrar_titulo(TITULOS, modo_juego))
    nombre_jugador = input(f"Introduce el nombre del jugador {numero_jugador}: ").strip().capitalize()
    if nombre_jugador == "":
        nombre_jugador = f"jugador_{numero_jugador}"
    nombre_jugador = f"J{numero_jugador} - " + nombre_jugador
    clear()
    return nombre_jugador


def mostrar_info_ronda(rondas: int, nombre_jugador_1: str, nombre_jugador_2: str, mano_jugador_1: str, mano_jugador_2: str, resultado_victoria: int = 0) -> str:
    """
    Muestra la información de cada ronda de la partida, incluyendo las manos de los jugadores y el resultado de la ronda.

    Args:
        rondas (int): El número de la ronda actual en el juego.
        nombre_jugador_1 (str): El nombre del jugador 1.
        nombre_jugador_2 (str): El nombre del jugador 2.
        mano_jugador_1 (str): Las cartas que tiene el jugador 1 en su mano.
        mano_jugador_2 (str): Las cartas que tiene el jugador 2 en su mano.
        resultado_victoria (int, opcional): El resultado de la ronda (0 si no hay resultado, 1 si gana el jugador 1, 
                                            2 si gana el jugador 2, 3 si es empate, 4 si ambos jugadores se pasan). 
                                            El valor por defecto es 0.

    Returns:
        str: Una cadena que contiene la información de la ronda, incluyendo el número de ronda, las manos de los jugadores y el resultado.
    """
    rondas_string = ""


    if rondas == 1:
        rondas_string = f"Inicio de partida - Ronda {rondas}"
        informacion_partida = f"{rondas_string}\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1, resultado_victoria)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2, resultado_victoria)}"
    elif rondas == 4:
        rondas_string = f"JUEGO TERMINADO - Ronda {rondas - 1}"
        informacion_partida = f"{rondas_string}\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1, resultado_victoria)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2, resultado_victoria)}"
    else:
        rondas_string = f"Ronda {rondas}"
        informacion_partida = f"{rondas_string}\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1, resultado_victoria)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2, resultado_victoria)}"


    if resultado_victoria == 1:
        informacion_partida = f"{rondas_string}\n\n¡Gana {nombre_jugador_1}!\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1, resultado_victoria)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2, resultado_victoria)}"

    elif resultado_victoria == 2:
        informacion_partida = f"{rondas_string}\n\n¡Gana {nombre_jugador_2}!\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1, resultado_victoria)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2, resultado_victoria)}"

    elif resultado_victoria == 3:
        informacion_partida = f"{rondas_string}\n\n¡Empate!\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1, resultado_victoria)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2, resultado_victoria)}"
    
    elif resultado_victoria == 4:
        informacion_partida = f"{rondas_string}\n\nGame over ¡Los dos os habéis pasado!\n\n{mostrar_mano_jugador(nombre_jugador_1, mano_jugador_1, resultado_victoria)}\n{mostrar_mano_jugador(nombre_jugador_2, mano_jugador_2, resultado_victoria)}"

    return informacion_partida


def mostrar_titulo(TITULOS: str, pos_titulo: int) -> str:
    """
    Muestra el título ubicado en la posición especificada dentro de la constante TITULOS.

    Args:
        TITULOS (str): Una cadena de texto que contiene una lista de títulos separados por algún delimitador (por ejemplo, comas o saltos de línea).
        pos_titulo (int): El índice del título a mostrar dentro de la lista de títulos.

    Returns:
        str: El título correspondiente a la posición especificada, seguido de un salto de línea.
    """
    titulo = TITULOS[pos_titulo]
    return titulo + "\n"


def condicion_victoria(mano_jugador_1: str, mano_jugador_2: str) -> int:
    """
    Determina el resultado de la partida entre dos jugadores basándose en los puntos obtenidos en sus manos.
    
    Las condiciones para el resultado son las siguientes:
    - Si ambos jugadores tienen la misma cantidad de puntos, el resultado es un empate (3).
    - Si ambos jugadores superan los 21 puntos (se pasan), el resultado es una doble derrota (4).
    - Si solo un jugador se pasa de 21 puntos, el otro jugador gana (1 o 2 dependiendo del jugador).
    - Si ninguno se pasa de 21 puntos, el jugador con los puntos más cercanos a 21 gana. Si el jugador 1 está más cerca de 21, gana el jugador 1, de lo contrario gana el jugador 2.

    Args:
        mano_jugador_1 (str): Las cartas del jugador 1, representadas como una cadena.
        mano_jugador_2 (str): Las cartas del jugador 2, representadas como una cadena.

    Returns:
        int: El resultado de la partida:
            - 1 si gana el jugador 1,
            - 2 si gana el jugador 2,
            - 3 si hay empate,
            - 4 si ambos jugadores se pasan de 21 puntos.
    """
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


def jugar(modo_juego: int):
    """
    Inicia el juego dependiendo del modo seleccionado (jugador vs. jugador o jugador vs. máquina).

    El juego se desarrolla en rondas donde los jugadores pueden optar por pedir más cartas o plantarse.
    Dependiendo del modo de juego, el jugador puede competir contra otro jugador o contra la máquina.
    El juego termina cuando se alcanzan tres rondas o cuando uno de los jugadores supera los 21 puntos.
    Hay tres formas de acabar la partida: en empate, ganando un jugador, o pasándose ambos de 21 puntos.

    Flujo del juego:
    1. Se genera el mazo y se establece el/los nombre/s de el/los jugador/es.
    2. En la primera ronda, ambos jugadores reciben una carta.
    3. Para cada ronda, cada jugador decide si quiere recibir una carta adicional o plantarse:
        - Si un jugador decide plantarse, no se le preguntará si desea recibir cartas por el resto de la partida.
        - Si el jugador quiere una carta, se le suma una nueva carta a su mano.
    4. El juego se repite durante un máximo de 3 rondas(o hasta que un jugador se pase de 21 puntos).
    5. Al final de cada ronda, se evalúa quién ha ganado (basándose en las cartas de la mano de cada jugador).
    6. Al finalizar, se ofrece la opción de volver a jugar. Si el jugador elige no jugar más, el juego termina junto al mensaje "Bye bye".

    Args:
        modo_juego (int): El modo de juego seleccionado.
    """
    global mazo_inicial

    if modo_juego == 1:
        # Crea la partida, generando el mazo y creando variables default para cada jugador / reglas del juego.
        mazo_inicial = generar_mazo()
        clear()

        # Pregunta y establece el nombres de los jugadores 1 y 2.
        nombre_jugador_1 = definir_nombre_jugador(modo_juego, numero_jugador = "1")
        nombre_jugador_2 = definir_nombre_jugador(modo_juego, numero_jugador = "2")

        print(f"Los jugadores de esta partida son:\n\n{nombre_jugador_1}\n{nombre_jugador_2}")
        input("\nPulsa ENTER para comenzar el juego...")
        clear()

        # Inicializa la mano de los dos jugadores.
        mano_jugador_1 = ""
        mano_jugador_2 = ""

        # En la primera ronda, los dos jugadores comienzan con una carta.
        mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)
        mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)

        # Variables de control para las rondas y plantarse.
        rondas = 1
        jugador_1_plantar = False
        jugador_2_plantar = False

        # Bucle principal del juego (3 rondas).
        while rondas <= 3:
            clear()
            print(mostrar_info_ronda(rondas, nombre_jugador_1, nombre_jugador_2, mano_jugador_1, mano_jugador_2))

            if jugador_1_plantar is False:
                opcion = input(f"\nJUGADOR {nombre_jugador_1} - ¿Quieres carta?: ").strip().lower()
                if opcion == "s" or opcion == "si":
                    mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)
                else:
                    jugador_1_plantar = True

            if jugador_2_plantar is False:
                opcion = input(f"\nJUGADOR {nombre_jugador_2} - ¿Quieres carta?: ").strip().lower()
                if opcion == "s" or opcion == "si":
                    mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)
                else:
                    jugador_2_plantar = True

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


    elif modo_juego == 2:
        # Crea la partida, generando el mazo y creando variables default para cada jugador / reglas del juego.
        mazo_inicial = generar_mazo()
        clear()

        # Preguntamos y establece el nombre del jugador 1
        nombre_jugador_1 = definir_nombre_jugador(2, numero_jugador = "1")
        nombre_jugador_2 = f"J2 - MAQUINA"

        print(f"Los jugadores de esta partida son:\n\n{nombre_jugador_1}\n{nombre_jugador_2}")
        input("\nPulsa ENTER para comenzar el juego...")
        clear()

        # Inicializa la mano de los dos jugadores.
        mano_jugador_1 = ""
        mano_jugador_2 = ""

        # En la primera ronda, los dos jugadores comienzan con una carta.
        mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)
        mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)

        # Variables de control para las rondas y plantarse.
        rondas = 1
        jugador_1_plantar = False
        jugador_2_plantar = False

        # Bucle principal del juego (3 rondas).
        while rondas <= 3:
            clear()
            print(mostrar_info_ronda(rondas, nombre_jugador_1, nombre_jugador_2, mano_jugador_1, mano_jugador_2))

            if jugador_1_plantar is False:
                opcion = input(f"\nJUGADOR {nombre_jugador_1} - ¿Quieres carta?: ").strip().lower()
                if opcion == "s" or opcion == "si":
                    mano_jugador_1 = sumar_cartas_jugador(mano_jugador_1)
                else:
                    jugador_1_plantar = True

            if jugador_2_plantar is False:
                opcion_maquina = randint(0,100)
                if opcion_maquina > 50:
                    mano_jugador_2 = sumar_cartas_jugador(mano_jugador_2)
                else:
                    jugador_2_plantar = True

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