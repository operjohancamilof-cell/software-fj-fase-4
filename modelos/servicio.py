from abc import ABC, abstractmethod

from excepciones.excepciones_personalizadas import ServicioInvalidoError


class Servicio(ABC):
    """Clase abstracta para los servicios ofrecidos por Software FJ."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        disponible: bool = True
    ) -> None:
        """Inicializa los datos generales de un servicio."""

        if not isinstance(codigo, str):
            raise ServicioInvalidoError(
                "El código del servicio debe ser texto."
            )

        codigo = codigo.strip()

        if not codigo:
            raise ServicioInvalidoError(
                "El código del servicio no puede estar vacío."
            )

        if not isinstance(nombre, str):
            raise ServicioInvalidoError(
                "El nombre del servicio debe ser texto."
            )

        nombre = nombre.strip()

        if len(nombre) < 3:
            raise ServicioInvalidoError(
                "El nombre del servicio debe tener al menos tres caracteres."
            )

        if not isinstance(disponible, bool):
            raise ServicioInvalidoError(
                "La disponibilidad debe indicarse con True o False."
            )

        self._codigo = codigo
        self._nombre = nombre
        self._disponible = disponible

    @property
    def codigo(self) -> str:
        """Devuelve el código del servicio."""

        return self._codigo

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del servicio."""

        return self._nombre

    @property
    def disponible(self) -> bool:
        """Indica si el servicio está disponible."""

        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool) -> None:
        """Modifica la disponibilidad del servicio."""

        if not isinstance(valor, bool):
            raise ServicioInvalidoError(
                "La disponibilidad debe indicarse con True o False."
            )

        self._disponible = valor

    @abstractmethod
    def calcular_costo(
        self,
        duracion: float,
        descuento: float = 0.0,
        impuesto: float = 0.0
    ) -> float:
        """Calcula el costo de un servicio."""

        raise NotImplementedError

    @abstractmethod
    def describir_servicio(self) -> str:
        """Devuelve la descripción del servicio."""

        raise NotImplementedError

    @abstractmethod
    def validar_parametros(self) -> None:
        """Valida los parámetros particulares del servicio."""

        raise NotImplementedError