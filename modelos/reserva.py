from excepciones.excepciones_personalizadas import (
    OperacionNoPermitidaError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
)
from modelos.cliente import Cliente
from modelos.servicio import Servicio


class Reserva:
    """Representa una reserva realizada por un cliente."""

    ESTADO_PENDIENTE = "PENDIENTE"
    ESTADO_CONFIRMADA = "CONFIRMADA"
    ESTADO_PROCESADA = "PROCESADA"
    ESTADO_CANCELADA = "CANCELADA"

    def __init__(
        self,
        codigo: str,
        cliente: Cliente,
        servicio: Servicio,
        duracion: float,
        descuento: float = 0.0,
        impuesto: float = 0.0
    ) -> None:
        """Inicializa y valida una reserva."""

        if not isinstance(codigo, str):
            raise ReservaInvalidaError(
                "El código de la reserva debe ser texto."
            )

        codigo = codigo.strip()

        if not codigo:
            raise ReservaInvalidaError(
                "El código de la reserva no puede estar vacío."
            )

        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "La reserva debe tener un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "La reserva debe tener un servicio válido."
            )

        if not servicio.disponible:
            raise ServicioNoDisponibleError(
                "El servicio seleccionado no está disponible."
            )

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
        ):
            raise ReservaInvalidaError(
                "La duración debe ser un valor numérico."
            )

        if duracion <= 0:
            raise ReservaInvalidaError(
                "La duración debe ser mayor que cero."
            )

        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
        ):
            raise ReservaInvalidaError(
                "El descuento debe ser un valor numérico."
            )

        if not 0 <= descuento <= 1:
            raise ReservaInvalidaError(
                "El descuento debe estar entre 0 y 1."
            )

        if (
            isinstance(impuesto, bool)
            or not isinstance(impuesto, (int, float))
        ):
            raise ReservaInvalidaError(
                "El impuesto debe ser un valor numérico."
            )

        if not 0 <= impuesto <= 1:
            raise ReservaInvalidaError(
                "El impuesto debe estar entre 0 y 1."
            )

        self._codigo = codigo
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = self.ESTADO_PENDIENTE

        self._costo_total = servicio.calcular_costo(
            duracion=duracion,
            descuento=descuento,
            impuesto=impuesto
        )

    @property
    def codigo(self) -> str:
        """Devuelve el código de la reserva."""

        return self._codigo

    @property
    def cliente(self) -> Cliente:
        """Devuelve el cliente de la reserva."""

        return self._cliente

    @property
    def servicio(self) -> Servicio:
        """Devuelve el servicio reservado."""

        return self._servicio

    @property
    def duracion(self) -> float:
        """Devuelve la duración de la reserva."""

        return self._duracion

    @property
    def estado(self) -> str:
        """Devuelve el estado actual de la reserva."""

        return self._estado

    @property
    def costo_total(self) -> float:
        """Devuelve el costo total calculado."""

        return self._costo_total

    def confirmar(self) -> None:
        """Confirma una reserva pendiente."""

        if self.estado != self.ESTADO_PENDIENTE:
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = self.ESTADO_CONFIRMADA

    def procesar(self) -> None:
        """Procesa una reserva previamente confirmada."""

        if self.estado != self.ESTADO_CONFIRMADA:
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada antes de procesarla."
            )

        self._estado = self.ESTADO_PROCESADA

    def cancelar(self) -> None:
        """Cancela una reserva pendiente o confirmada."""

        if self.estado == self.ESTADO_CANCELADA:
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        if self.estado == self.ESTADO_PROCESADA:
            raise OperacionNoPermitidaError(
                "Una reserva procesada no puede cancelarse."
            )

        self._estado = self.ESTADO_CANCELADA

    def mostrar_resumen(self) -> str:
        """Devuelve el resumen completo de la reserva."""

        return (
            f"Reserva: {self.codigo} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} | "
            f"Estado: {self.estado} | "
            f"Costo total: ${self.costo_total:,.0f}"
        )