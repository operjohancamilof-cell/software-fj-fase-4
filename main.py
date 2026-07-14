from excepciones.excepciones_personalizadas import ClienteInvalidoError
from modelos.entidad import Entidad
from utilidades.configuracion_logs import configurar_logger


logger = configurar_logger()


class EntidadPrueba(Entidad):
    """Clase temporal utilizada para comprobar la abstracción."""

    def mostrar_informacion(self) -> str:
        return f"Entidad de prueba: {self.identificador}"


def probar_excepcion() -> None:
    """Comprueba las excepciones y el archivo de logs."""

    print("\n--- PRUEBA 1: EXCEPCIÓN PERSONALIZADA ---")

    try:
        nombre = ""

        if not nombre:
            raise ClienteInvalidoError(
                "El nombre del cliente no puede estar vacío."
            )

    except ClienteInvalidoError as error:
        print(f"Error controlado: {error}")
        logger.error(
            "No fue posible crear el cliente: %s",
            error
        )

    else:
        print("El cliente fue creado correctamente.")
        logger.info("Cliente creado correctamente.")

    finally:
        print("La prueba de excepciones finalizó.")
        logger.info("Finalizó la prueba de excepciones.")


def probar_entidad() -> None:
    """Comprueba el funcionamiento de la clase abstracta Entidad."""

    print("\n--- PRUEBA 2: CLASE ABSTRACTA ENTIDAD ---")

    try:
        entidad = EntidadPrueba("CLI-001")
        print(entidad.mostrar_informacion())

    except (TypeError, ValueError) as error:
        print(f"Error al crear la entidad: {error}")
        logger.error(
            "No fue posible crear la entidad: %s",
            error
        )

    else:
        print("La entidad fue creada correctamente.")
        logger.info(
            "Entidad creada correctamente con identificador %s.",
            entidad.identificador
        )

    finally:
        print("La prueba de la clase Entidad finalizó.")
        logger.info("Finalizó la prueba de la clase Entidad.")


if __name__ == "__main__":
    print("SISTEMA INTEGRAL SOFTWARE FJ")

    probar_excepcion()
    probar_entidad()

    print("\nEjecución finalizada correctamente.")