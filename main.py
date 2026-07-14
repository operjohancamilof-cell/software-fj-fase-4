from excepciones.excepciones_personalizadas import ClienteInvalidoError
from utilidades.configuracion_logs import configurar_logger


logger = configurar_logger()


def probar_excepcion() -> None:
    """Comprueba las excepciones y el archivo de logs."""

    try:
        nombre = ""

        if not nombre:
            raise ClienteInvalidoError(
                "El nombre del cliente no puede estar vacío."
            )

    except ClienteInvalidoError as error:
        print(f"Error controlado: {error}")
        logger.error("No fue posible crear el cliente: %s", error)

    else:
        print("El cliente fue creado correctamente.")
        logger.info("Cliente creado correctamente.")

    finally:
        print("La prueba de excepciones finalizó.")
        logger.info("Finalizó la prueba de excepciones.")


if __name__ == "__main__":
    probar_excepcion()