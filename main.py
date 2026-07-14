from excepciones.excepciones_personalizadas import (
    ClienteInvalidoError,
    ServicioInvalidoError,
)
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.cliente import Cliente
from modelos.entidad import Entidad
from modelos.servicio import Servicio
from modelos.reserva_sala import ReservaSala
from utilidades.configuracion_logs import configurar_logger


logger = configurar_logger()


class EntidadPrueba(Entidad):
    """Clase temporal utilizada para comprobar la abstracción."""

    def mostrar_informacion(self) -> str:
        return f"Entidad de prueba: {self.identificador}"
    
class ServicioPrueba(Servicio):
    """Clase temporal utilizada para comprobar la clase Servicio."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        tarifa_base: float,
        disponible: bool = True
    ) -> None:
        """Inicializa un servicio temporal."""

        super().__init__(
            codigo=codigo,
            nombre=nombre,
            disponible=disponible
        )

        self.tarifa_base = tarifa_base
        self.validar_parametros()

    def validar_parametros(self) -> None:
        """Valida la tarifa del servicio temporal."""

        if not isinstance(self.tarifa_base, (int, float)):
            raise ServicioInvalidoError(
                "La tarifa base debe ser un valor numérico."
            )

        if self.tarifa_base <= 0:
            raise ServicioInvalidoError(
                "La tarifa base debe ser mayor que cero."
            )

    def calcular_costo(
        self,
        duracion: float,
        descuento: float = 0.0,
        impuesto: float = 0.0
    ) -> float:
        """Calcula el costo utilizando duración, descuento e impuesto."""

        if not isinstance(duracion, (int, float)):
            raise ServicioInvalidoError(
                "La duración debe ser un valor numérico."
            )

        if duracion <= 0:
            raise ServicioInvalidoError(
                "La duración debe ser mayor que cero."
            )

        if not 0 <= descuento <= 1:
            raise ServicioInvalidoError(
                "El descuento debe estar entre 0 y 1."
            )

        if not 0 <= impuesto <= 1:
            raise ServicioInvalidoError(
                "El impuesto debe estar entre 0 y 1."
            )

        subtotal = self.tarifa_base * duracion
        subtotal_con_descuento = subtotal * (1 - descuento)
        total = subtotal_con_descuento * (1 + impuesto)

        return total

    def describir_servicio(self) -> str:
        """Devuelve la descripción del servicio temporal."""

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"Servicio de prueba: {self.nombre} | "
            f"Estado: {estado}"
        )    


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

def probar_servicio_abstracto() -> None:
    """Comprueba la clase abstracta Servicio."""

    print("\n--- PRUEBA 5: CLASE ABSTRACTA SERVICIO ---")

    try:
        servicio = ServicioPrueba(
            codigo="SER-001",
            nombre="Servicio temporal",
            tarifa_base=50000,
            disponible=True
        )

        costo = servicio.calcular_costo(
            duracion=2,
            descuento=0.10,
            impuesto=0.19
        )

    except (ServicioInvalidoError, TypeError, ValueError) as error:
        print(f"Error al crear o calcular el servicio: {error}")

        logger.error(
            "No fue posible probar la clase Servicio: %s",
            error
        )

    else:
        print(servicio.describir_servicio())
        print(f"Costo calculado: ${costo:,.0f}")
        print("El servicio fue creado correctamente.")

        logger.info(
            "Servicio %s creado correctamente. Costo: %.2f",
            servicio.codigo,
            costo
        )

    finally:
        print("La prueba de la clase Servicio finalizó.")
        logger.info(
            "Finalizó la prueba de la clase Servicio."
        )        


def probar_reserva_sala_valida() -> None:
    """Comprueba la creación correcta de una reserva de sala."""

    print("\n--- PRUEBA 6: RESERVA DE SALA VÁLIDA ---")

    try:
        sala = ReservaSala(
            codigo="SAL-001",
            nombre="Sala de Conferencias",
            tarifa_hora=80000,
            capacidad=25,
            disponible=True
        )

        sala.validar_cantidad_personas(20)

        costo = sala.calcular_costo(
            duracion=3,
            descuento=0.05,
            impuesto=0.19
        )

    except ServicioInvalidoError as error:
        print(f"Error al crear o reservar la sala: {error}")

        logger.error(
            "No fue posible procesar la sala válida: %s",
            error
        )

    else:
        print(sala.describir_servicio())
        print("Cantidad solicitada: 20 personas")
        print("Duración solicitada: 3 horas")
        print("Descuento aplicado: 5 %")
        print("Impuesto aplicado: 19 %")
        print(f"Costo total de la reserva: ${costo:,.0f}")
        print("La reserva de sala fue calculada correctamente.")

        logger.info(
            "Sala %s procesada correctamente. Costo: %.2f",
            sala.codigo,
            costo
        )

    finally:
        print("La prueba de la sala válida finalizó.")

        logger.info(
            "Finalizó la prueba de la sala válida."
        )

def probar_reserva_sala_invalida() -> None:
    """Comprueba el control de una capacidad inválida."""

    print("\n--- PRUEBA 7: SALA CON CAPACIDAD INVÁLIDA ---")

    try:
        ReservaSala(
            codigo="SAL-002",
            nombre="Sala Pequeña",
            tarifa_hora=50000,
            capacidad=0,
            disponible=True
        )

    except ServicioInvalidoError as error:
        print(f"Error controlado: {error}")

        logger.error(
            "No fue posible crear la sala por datos inválidos: %s",
            error
        )

    else:
        print("La sala fue creada, pero no debía ser aceptada.")

        logger.warning(
            "Se aceptó incorrectamente una sala con capacidad inválida."
        )

    finally:
        print("La prueba de la sala inválida finalizó.")

        logger.info(
            "Finalizó la prueba de la sala inválida."
        )        
def probar_alquiler_equipo_valido() -> None:
    """Comprueba un alquiler correcto de equipos."""

    print("\n--- PRUEBA 8: ALQUILER DE EQUIPO VÁLIDO ---")

    try:
        equipo = AlquilerEquipo(
            codigo="EQU-001",
            nombre="Computador portátil empresarial",
            tarifa_dia=120000,
            cantidad_disponible=10,
            disponible=True
        )

        cantidad_solicitada = 3
        duracion_dias = 2

        equipo.validar_cantidad_solicitada(
            cantidad_solicitada
        )

        costo = equipo.calcular_costo(
            duracion=duracion_dias,
            descuento=0.10,
            impuesto=0.19,
            cantidad=cantidad_solicitada
        )

    except ServicioInvalidoError as error:
        print(f"Error al procesar el alquiler: {error}")

        logger.error(
            "No fue posible procesar el alquiler válido: %s",
            error
        )

    else:
        print(equipo.describir_servicio())
        print(f"Cantidad solicitada: {cantidad_solicitada}")
        print(f"Duración del alquiler: {duracion_dias} días")
        print("Descuento aplicado: 10 %")
        print("Impuesto aplicado: 19 %")
        print(f"Costo total del alquiler: ${costo:,.0f}")
        print("El alquiler fue calculado correctamente.")

        logger.info(
            "Equipo %s alquilado correctamente. Costo: %.2f",
            equipo.codigo,
            costo
        )

    finally:
        print("La prueba del alquiler válido finalizó.")

        logger.info(
            "Finalizó la prueba del alquiler válido."
        )
def probar_alquiler_equipo_invalido() -> None:
    """Comprueba una solicitud superior a la disponibilidad."""

    print(
        "\n--- PRUEBA 9: CANTIDAD DE EQUIPOS NO DISPONIBLE ---"
    )

    try:
        equipo = AlquilerEquipo(
            codigo="EQU-002",
            nombre="Proyector multimedia",
            tarifa_dia=90000,
            cantidad_disponible=4,
            disponible=True
        )

        equipo.validar_cantidad_solicitada(6)

    except ServicioInvalidoError as error:
        print(f"Error controlado: {error}")

        logger.error(
            "No fue posible procesar el alquiler "
            "por cantidad inválida: %s",
            error
        )

    else:
        print(
            "El alquiler fue aceptado, pero la cantidad "
            "no estaba disponible."
        )

        logger.warning(
            "Se aceptó incorrectamente una cantidad superior "
            "a la disponibilidad."
        )

    finally:
        print("La prueba del alquiler inválido finalizó.")

        logger.info(
            "Finalizó la prueba del alquiler inválido."
        )        


if __name__ == "__main__":
    print("SISTEMA INTEGRAL SOFTWARE FJ")

    probar_excepcion()
    probar_entidad()
    probar_cliente_valido()
    probar_cliente_invalido()
    probar_servicio_abstracto()
    probar_reserva_sala_valida()
    probar_reserva_sala_invalida()
    probar_alquiler_equipo_valido()
    probar_alquiler_equipo_invalido()

    print("\nEjecución finalizada correctamente.")