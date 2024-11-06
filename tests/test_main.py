import pytest
from src.main import *


# PRUEBAS DE LA FUNCION GENERAR_MAZO
@pytest.mark.parametrize(
    "expected",
    [
        "A♠2♠3♠4♠5♠6♠7♠8♠9♠0♠J♠K♠Q♠A♥2♥3♥4♥5♥6♥7♥8♥9♥0♥J♥K♥Q♥A♦2♦3♦4♦5♦6♦7♦8♦9♦0♦J♦K♦Q♦A♣2♣3♣4♣5♣6♣7♣8♣9♣0♣J♣K♣Q♣",
    ]
)
def test_generar_mazo_params(expected):
    assert generar_mazo() == expected


# PRUEBAS DE LA FUNCION SELECCIONAR_CARTA_AZAR
def test_seleccionar_carta_azar():
    mazo = generar_mazo()
    carta_azar = seleccionar_carta_azar(mazo)
    assert len(carta_azar) == 2
    assert carta_azar[:-1] in "A234567890JKQ"
    assert carta_azar[-1] in "♠♥♦♣"


# PRUEBAS DE LA FUNCION SUMAR_PUNTOS_JUGADOR
@pytest.mark.parametrize(
    "mano_jugador, expected",
    [
        ("A♠2♠3", 16),
        ("7♠8♠9♠", 24),
        ("", 0),
    ]
)
def test_sumar_puntos_jugador_params(mano_jugador, expected):
    assert sumar_puntos_jugador(mano_jugador) == expected


# PRUEBAS DE LA FUNCION COSTE_DE_CARTA
@pytest.mark.parametrize(
    "carta, puntuacion, expected",
    [
        ("A", 10, 11),
        ("A", 12, 1),
        ("5", 0, 5),
        ("J", 0, 10),
        ("K", 0, 10),
        ("0", 0, 10),
        ("2", 0, 2),
    ]
)
def test_coste_de_carta(carta, puntuacion, expected):
    assert coste_de_carta(carta, puntuacion) == expected


# PRUEBAS DE LA FUNCION TEST_CONDICION_VICTORIA
@pytest.mark.parametrize(
    "mano_jugador_1, mano_jugador_2, expected",
    [
        ("56", "87", 2),
        ("J6", "109", 2),
        ("89", "K3", 1),
        ("1011", "J6", 2),
        ("78", "97", 2),
        ("001", "001", 3),
        ("6666", "66666", 4),
    ]
)
def test_condicion_victoria(mano_jugador_1, mano_jugador_2, expected):
    assert condicion_victoria(mano_jugador_1, mano_jugador_2) == expected


# PRUEBAS DE LA FUNCION TEST_MOSTRAR_MANO_JUGADOR
def test_mostrar_mano_jugador():
    resultado = mostrar_mano_jugador("Jugador 1", "A♠2♦", 0)
    assert "Jugador 1 - A♠2♦" in resultado
    assert "(13)" in resultado


# PRUEBAS DE LA FUNCION VALIDAR_NUM
@pytest.mark.parametrize(
    "numero, expected",
    [
        ("5", True),
        ("a", False),
        ("12", True),
    ]
)
def test_validar_num(numero, expected):
    assert validar_num(numero) == expected


# PRUEBAS DE LA FUNCION VALIDAR_MODO_JUEGO
@pytest.mark.parametrize(
    "modo_juego, expected", 
    [
        (1, True),
        (2, True),
        (3, False),
        (0, False),
    ]
)
def test_validar_modo_juego(modo_juego, expected):
    assert validar_modo_juego(modo_juego) == expected


# PRUEBAS DE LA FUNCION ESCOGER_MODO_JUEGO
@pytest.mark.parametrize(
    "opcion, expected", 
    [
        (1, 1),
        (2, 2),
    ]
)
def test_escoger_modo_juego(opcion, expected):
    assert escoger_modo_juego(opcion) == expected


# PRUEBAS DE LA FUNCION MOSTRAR_TITULO
def test_mostrar_titulo():
    titulo = mostrar_titulo(("Titulo 1", "Titulo 2"), 0)
    assert titulo == "Titulo 1\n"
    titulo = mostrar_titulo(("Titulo 1", "Titulo 2"), 1)
    assert titulo == "Titulo 2\n"