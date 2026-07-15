from excepciones.excepciones_personalizadas import ReservaInvalidaError


def convertir_duracion(valor: str) -> int:
    """Convierte una duración escrita como texto en un número entero."""

    if not isinstance(valor, str):
        raise ReservaInvalidaError(
            "La duración debe recibirse como una cadena de texto."
        )

    try:
        duracion = int(valor)

    except ValueError as error_original:
        raise ReservaInvalidaError(
            "La duración debe escribirse como un número entero."
        ) from error_original

    if duracion <= 0:
        raise ReservaInvalidaError(
            "La duración debe ser mayor que cero."
        )

    return duracion