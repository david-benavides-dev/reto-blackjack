
################################################################################
# TODO
# - Crear funcion para importar cartas a la mano de los jugadores.
# - Funcion for que itere por la mano del jugador y diga cuantos puntos tiene.
# - 
# -
################################################################################

from random import randint
BARAJA = "A234567890JKQ"



# FUNCION PARA GENERAR MAZO
def generar_mazo() -> str:
    """
    
    """
    baraja_completa: str = ""
    for _ in range (4):
        baraja_completa += BARAJA
    return baraja_completa
        

# FUNCION PARA SACAR CARTAS AL AZAR
def seleccionar_carta_azar(baraja_juego) -> str:
    """
    
    """
    if baraja_juego != "":
        return baraja_juego[randint(0, len(baraja_juego) - 1)]
    return ""


# FUNCION PARA BORRAR UNA CARTA AL AZAR DEL MAZO
def restar_carta_azar(baraja_juego) -> str:
    """
    
    """
    restar_carta = seleccionar_carta_azar(baraja_juego)
    if baraja_juego != "":
        baraja_juego = baraja_juego.replace(restar_carta, "", 1)
    return baraja_juego


# Funcion para determinar el coste real de la carta.
def coste_de_carta(carta) -> int:
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
    # NOTE: Arreglado valores de los palos.
    elif carta in "0JQK":
        carta = 10
    return carta


# TODO Funcion para sumar cartas a la mano del player
def sumar_cartas_jugador(mano_jugador: str) -> str:
    global mazo_inicial
    if mazo_inicial == "":
        print("No hay cartas en el mazo")
        return mano_jugador
    carta = seleccionar_carta_azar(mazo_inicial)
    mazo_inicial = mazo_inicial.replace(carta, "", 1)
    mano_jugador += carta
    print(f"CARTA {carta} DE COSTE {coste_de_carta(carta)} añadida a la mano del jugador correctamente.")
    return mano_jugador

def mostrar_mano_jugador(mano_jugador) -> str:
    
    return f"Tu mano contiene las siguientes cartas: "


def main():
    """
    Probando lógica y funciones que probablemente usará el blackjack (aún no se ni como se juega xd)
    """
    global mazo_inicial

    mano_jugador = ""

    mazo_inicial = generar_mazo()

    while len(mano_jugador) < 4:
        mano_jugador = sumar_cartas_jugador(mano_jugador)
        print("Mano del jugador: " + mano_jugador)
        print("MAZO_ACTUAL -> " + mazo_inicial)
        input("PRESIONA ENTER")


    # NOTE Prueba inicial de funcion coste_carta
    # for _ in range(0, 4):
    #     carta = seleccionar_carta_azar(mazo_inicial)
    #     carta_coste = coste_de_carta(carta)
    #     print(f"CARTA {carta} DE COSTE {carta_coste} añadida a la mano del jugador correctamente.")


    # NOTE Prueba inicial de la funcion restar cartas hasta acabar con el mazo completo.
    # for _ in range (len(mazo_inicial)):
    #     mazo_inicial = restar_carta_azar(mazo_inicial)
    #     print("La carta ha sido eliminada con éxito.")

    # print(seleccionar_carta_azar(mazo_inicial))


if __name__ == "__main__":
    main()