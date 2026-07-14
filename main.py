from excepciones.excepciones_personalizadas import ClienteInvalidoError
from modelos.cliente import Cliente
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
    """Comprueba el funcionamiento de la clase Entidad."""

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


def probar_cliente_valido() -> None:
    """Comprueba la creación correcta de un cliente."""

    print("\n--- PRUEBA 3: CLIENTE VÁLIDO ---")

    try:
        cliente = Cliente(
            identificacion="10203040",
            nombre="Johan Camilo Forero",
            correo="johan.forero@email.com",
            telefono="3001234567"
        )

    except (ClienteInvalidoError, TypeError, ValueError) as error:
        print(f"Error al crear el cliente: {error}")
        logger.error(
            "No fue posible crear el cliente válido: %s",
            error
        )

    else:
        print(cliente.mostrar_informacion())
        print("El cliente válido fue creado correctamente.")

        logger.info(
            "Cliente creado correctamente con identificación %s.",
            cliente.identificador
        )

    finally:
        print("La prueba del cliente válido finalizó.")
        logger.info("Finalizó la prueba del cliente válido.")


def probar_cliente_invalido() -> None:
    """Comprueba el control de un correo inválido."""

    print("\n--- PRUEBA 4: CLIENTE CON CORREO INVÁLIDO ---")

    try:
        Cliente(
            identificacion="10203041",
            nombre="María López",
            correo="correo-invalido",
            telefono="3007654321"
        )

    except ClienteInvalidoError as error:
        print(f"Error controlado: {error}")

        logger.error(
            "No fue posible crear el cliente por datos inválidos: %s",
            error
        )

    else:
        print("El cliente fue creado, pero no debía ser aceptado.")
        logger.warning(
            "Se aceptó incorrectamente un cliente con correo inválido."
        )

    finally:
        print("La prueba del cliente inválido finalizó.")
        logger.info("Finalizó la prueba del cliente inválido.")


if __name__ == "__main__":
    print("SISTEMA INTEGRAL SOFTWARE FJ")

    probar_excepcion()
    probar_entidad()
    probar_cliente_valido()
    probar_cliente_invalido()

    print("\nEjecución finalizada correctamente.")