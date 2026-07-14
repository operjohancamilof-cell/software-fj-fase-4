from excepciones.excepciones_personalizadas import ClienteInvalidoError


def probar_excepcion() -> None:
    """Comprueba que las excepciones personalizadas funcionen."""

    try:
        nombre = ""

        if not nombre:
            raise ClienteInvalidoError(
                "El nombre del cliente no puede estar vacío."
            )

    except ClienteInvalidoError as error:
        print(f"Error controlado: {error}")

    else:
        print("El cliente fue creado correctamente.")

    finally:
        print("Prueba correcta: las excepciones personalizadas funcionan.")


if __name__ == "__main__":
    probar_excepcion()