from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase abstracta general para las entidades de Software FJ."""

    def __init__(self, identificador: str) -> None:
        """Inicializa una entidad con un identificador válido."""

        if not isinstance(identificador, str):
            raise TypeError(
                "El identificador debe ser una cadena de texto."
            )

        identificador = identificador.strip()

        if not identificador:
            raise ValueError(
                "El identificador no puede estar vacío."
            )

        self._identificador = identificador

    @property
    def identificador(self) -> str:
        """Devuelve el identificador de la entidad."""

        return self._identificador

    @abstractmethod
    def mostrar_informacion(self) -> str:
        """Devuelve la información principal de la entidad."""

        raise NotImplementedError