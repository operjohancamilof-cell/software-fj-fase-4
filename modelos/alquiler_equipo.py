from excepciones.excepciones_personalizadas import ServicioInvalidoError
from modelos.servicio import Servicio


class AlquilerEquipo(Servicio):
    """Representa el servicio de alquiler de equipos."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        tarifa_dia: float,
        cantidad_disponible: int,
        disponible: bool = True
    ) -> None:
        """Inicializa un equipo disponible para alquiler."""

        super().__init__(
            codigo=codigo,
            nombre=nombre,
            disponible=disponible
        )

        self._tarifa_dia = tarifa_dia
        self._cantidad_disponible = cantidad_disponible

        self.validar_parametros()

    @property
    def tarifa_dia(self) -> float:
        """Devuelve la tarifa diaria del equipo."""

        return self._tarifa_dia

    @property
    def cantidad_disponible(self) -> int:
        """Devuelve la cantidad de equipos disponibles."""

        return self._cantidad_disponible

    def validar_parametros(self) -> None:
        """Valida la tarifa y la cantidad disponible."""

        if (
            isinstance(self._tarifa_dia, bool)
            or not isinstance(self._tarifa_dia, (int, float))
        ):
            raise ServicioInvalidoError(
                "La tarifa diaria debe ser un valor numérico."
            )

        if self._tarifa_dia <= 0:
            raise ServicioInvalidoError(
                "La tarifa diaria debe ser mayor que cero."
            )

        if (
            isinstance(self._cantidad_disponible, bool)
            or not isinstance(self._cantidad_disponible, int)
        ):
            raise ServicioInvalidoError(
                "La cantidad disponible debe ser un número entero."
            )

        if self._cantidad_disponible < 0:
            raise ServicioInvalidoError(
                "La cantidad disponible no puede ser negativa."
            )

    def validar_cantidad_solicitada(
        self,
        cantidad_solicitada: int
    ) -> None:
        """Valida la cantidad de equipos solicitada."""

        if (
            isinstance(cantidad_solicitada, bool)
            or not isinstance(cantidad_solicitada, int)
        ):
            raise ServicioInvalidoError(
                "La cantidad solicitada debe ser un número entero."
            )

        if cantidad_solicitada <= 0:
            raise ServicioInvalidoError(
                "La cantidad solicitada debe ser mayor que cero."
            )

        if cantidad_solicitada > self.cantidad_disponible:
            raise ServicioInvalidoError(
                "La cantidad solicitada supera la cantidad disponible."
            )

    def calcular_costo(
        self,
        duracion: float,
        descuento: float = 0.0,
        impuesto: float = 0.0,
        cantidad: int = 1
    ) -> float:
        """Calcula el costo del alquiler de uno o varios equipos."""

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
        ):
            raise ServicioInvalidoError(
                "La duración debe ser un valor numérico."
            )

        if duracion <= 0:
            raise ServicioInvalidoError(
                "La duración debe ser mayor que cero."
            )

        self.validar_cantidad_solicitada(cantidad)

        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
        ):
            raise ServicioInvalidoError(
                "El descuento debe ser un valor numérico."
            )

        if not 0 <= descuento <= 1:
            raise ServicioInvalidoError(
                "El descuento debe estar entre 0 y 1."
            )

        if (
            isinstance(impuesto, bool)
            or not isinstance(impuesto, (int, float))
        ):
            raise ServicioInvalidoError(
                "El impuesto debe ser un valor numérico."
            )

        if not 0 <= impuesto <= 1:
            raise ServicioInvalidoError(
                "El impuesto debe estar entre 0 y 1."
            )

        subtotal = self.tarifa_dia * duracion * cantidad
        subtotal_con_descuento = subtotal * (1 - descuento)
        total = subtotal_con_descuento * (1 + impuesto)

        return total

    def describir_servicio(self) -> str:
        """Devuelve la descripción del alquiler de equipos."""

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"Equipo: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Cantidad disponible: {self.cantidad_disponible} | "
            f"Tarifa diaria: ${self.tarifa_dia:,.0f} | "
            f"Estado: {estado}"
        )