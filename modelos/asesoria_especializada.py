from excepciones.excepciones_personalizadas import ServicioInvalidoError
from modelos.servicio import Servicio


class AsesoriaEspecializada(Servicio):
    """Representa un servicio de asesoría especializada."""

    NIVELES_VALIDOS = {
        "Junior": 1.00,
        "Semisenior": 1.15,
        "Senior": 1.30,
    }

    def __init__(
        self,
        codigo: str,
        nombre: str,
        tarifa_hora: float,
        especialidad: str,
        nivel_experiencia: str,
        disponible: bool = True
    ) -> None:
        """Inicializa una asesoría especializada."""

        super().__init__(
            codigo=codigo,
            nombre=nombre,
            disponible=disponible
        )

        self._tarifa_hora = tarifa_hora
        self._especialidad = especialidad
        self._nivel_experiencia = nivel_experiencia

        self.validar_parametros()

    @property
    def tarifa_hora(self) -> float:
        """Devuelve la tarifa base por hora."""

        return self._tarifa_hora

    @property
    def especialidad(self) -> str:
        """Devuelve la especialidad de la asesoría."""

        return self._especialidad

    @property
    def nivel_experiencia(self) -> str:
        """Devuelve el nivel de experiencia."""

        return self._nivel_experiencia

    def validar_parametros(self) -> None:
        """Valida los datos particulares de la asesoría."""

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

        if not isinstance(self._especialidad, str):
            raise ServicioInvalidoError(
                "La especialidad debe ser texto."
            )

        self._especialidad = self._especialidad.strip()

        if not self._especialidad:
            raise ServicioInvalidoError(
                "La especialidad es obligatoria."
            )

        if not isinstance(self._nivel_experiencia, str):
            raise ServicioInvalidoError(
                "El nivel de experiencia debe ser texto."
            )

        self._nivel_experiencia = (
            self._nivel_experiencia.strip().capitalize()
        )

        if self._nivel_experiencia not in self.NIVELES_VALIDOS:
            raise ServicioInvalidoError(
                "El nivel debe ser Junior, Semisenior o Senior."
            )

    def calcular_costo(
        self,
        duracion: float,
        descuento: float = 0.0,
        impuesto: float = 0.0
    ) -> float:
        """Calcula el costo de la asesoría."""

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

        factor_experiencia = self.NIVELES_VALIDOS[
            self.nivel_experiencia
        ]

        subtotal = (
            self.tarifa_hora
            * duracion
            * factor_experiencia
        )

        # Las asesorías de cinco horas o más reciben 10 % automático.
        if duracion >= 5:
            subtotal *= 0.90

        subtotal_con_descuento = subtotal * (1 - descuento)
        total = subtotal_con_descuento * (1 + impuesto)

        return total

    def describir_servicio(self) -> str:
        """Devuelve la descripción de la asesoría."""

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"Asesoría: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Especialidad: {self.especialidad} | "
            f"Nivel: {self.nivel_experiencia} | "
            f"Tarifa por hora: ${self.tarifa_hora:,.0f} | "
            f"Estado: {estado}"
        )