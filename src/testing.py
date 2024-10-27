
################################################################################
# TODO
# - Crear funcion para importar cartas al mazo de los jugadores.
# - Funcion for que itere por el mazo del jugador y diga cuantos puntos tiene.
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
    return "Tu mazo no contiene cartas!"


# FUNCION PARA BORRAR UNA CARTA AL AZAR DEL MAZO
def restar_carta_azar(baraja_juego) -> str:
    """
    
    """
    restar_carta = seleccionar_carta_azar(baraja_juego)
    if baraja_juego != "":
        baraja_juego = baraja_juego.replace(restar_carta, "", 1)
    return baraja_juego


# Funcion para determinar el coste real de la carta
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
    elif carta == "0":
        carta = 10
    elif carta == "J":
        carta = 11
    else:
        carta = 12
    return carta


def main():
    """
    Probando lógica y funciones que probablemente usará el blackjack (aún no se ni como se juega xd)
    """
    mazo_inicial = generar_mazo()

    for _ in range(0, 4):
        carta = seleccionar_carta_azar(mazo_inicial)
        carta_coste = coste_de_carta(carta)
        print(f"CARTA {carta} DE COSTE {carta_coste}")

    for _ in range (len(mazo_inicial)):
        mazo_inicial = restar_carta_azar(mazo_inicial)
        print("La carta ha sido eliminada con éxito.")

    print(seleccionar_carta_azar(mazo_inicial))


if __name__ == "__main__":
    main()