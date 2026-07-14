from excepciones.excepciones_personalizadas import ServicioInvalidoError
from modelos.servicio import Servicio


class ReservaSala(Servicio):
    """Representa el servicio de reserva de una sala."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        tarifa_hora: float,
        capacidad: int,
        disponible: bool = True
    ) -> None:
        """Inicializa una sala y valida sus datos."""

        super().__init__(
            codigo=codigo,
            nombre=nombre,
            disponible=disponible
        )

        self._tarifa_hora = tarifa_hora
        self._capacidad = capacidad

        self.validar_parametros()

    @property
    def tarifa_hora(self) -> float:
        """Devuelve la tarifa por hora de la sala."""

        return self._tarifa_hora

    @property
    def capacidad(self) -> int:
        """Devuelve la capacidad máxima de la sala."""

        return self._capacidad

    def validar_parametros(self) -> None:
        """Valida la tarifa y la capacidad de la sala."""

        if (
            isinstance(self._tarifa_hora, bool)
            or not isinstance(self._tarifa_hora, (int, float))
        ):
            raise ServicioInvalidoError(
                "La tarifa por hora debe ser un valor numérico."
            )

        if self._tarifa_hora <= 0:
            raise ServicioInvalidoError(
                "La tarifa por hora debe ser mayor que cero."
            )

        if (
            isinstance(self._capacidad, bool)
            or not isinstance(self._capacidad, int)
        ):
            raise ServicioInvalidoError(
                "La capacidad de la sala debe ser un número entero."
            )

        if self._capacidad <= 0:
            raise ServicioInvalidoError(
                "La capacidad de la sala debe ser mayor que cero."
            )

    def validar_cantidad_personas(self, cantidad_personas: int) -> None:
        """Valida que la cantidad de personas no supere la capacidad."""

        if (
            isinstance(cantidad_personas, bool)
            or not isinstance(cantidad_personas, int)
        ):
            raise ServicioInvalidoError(
                "La cantidad de personas debe ser un número entero."
            )

        if cantidad_personas <= 0:
            raise ServicioInvalidoError(
                "La cantidad de personas debe ser mayor que cero."
            )

        if cantidad_personas > self.capacidad:
            raise ServicioInvalidoError(
                "La cantidad de personas supera la capacidad de la sala."
            )

    def calcular_costo(
        self,
        duracion: float,
        descuento: float = 0.0,
        impuesto: float = 0.0
    ) -> float:
        """Calcula el costo de la reserva de la sala."""

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

        subtotal = self.tarifa_hora * duracion
        valor_descuento = subtotal * descuento
        subtotal_con_descuento = subtotal - valor_descuento
        valor_impuesto = subtotal_con_descuento * impuesto
        total = subtotal_con_descuento + valor_impuesto

        return total

    def describir_servicio(self) -> str:
        """Devuelve la descripción de la sala."""

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"Sala: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Tarifa por hora: ${self.tarifa_hora:,.0f} | "
            f"Estado: {estado}"
        )