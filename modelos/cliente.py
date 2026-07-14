import re

from excepciones.excepciones_personalizadas import ClienteInvalidoError
from modelos.entidad import Entidad


class Cliente(Entidad):
    """Representa un cliente registrado en Software FJ."""

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        telefono: str
    ) -> None:
        """Inicializa un cliente y valida sus datos."""

        super().__init__(identificacion)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del cliente."""

        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Valida y almacena el nombre del cliente."""

        if not isinstance(valor, str):
            raise ClienteInvalidoError(
                "El nombre debe ser una cadena de texto."
            )

        valor = valor.strip()

        if len(valor) < 3:
            raise ClienteInvalidoError(
                "El nombre debe tener al menos tres caracteres."
            )

        self._nombre = valor

    @property
    def correo(self) -> str:
        """Devuelve el correo electrónico del cliente."""

        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        """Valida y almacena el correo electrónico."""

        if not isinstance(valor, str):
            raise ClienteInvalidoError(
                "El correo debe ser una cadena de texto."
            )

        valor = valor.strip().lower()
        patron_correo = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not re.match(patron_correo, valor):
            raise ClienteInvalidoError(
                "El correo electrónico no tiene un formato válido."
            )

        self._correo = valor

    @property
    def telefono(self) -> str:
        """Devuelve el teléfono del cliente."""

        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        """Valida y almacena el teléfono."""

        if not isinstance(valor, str):
            raise ClienteInvalidoError(
                "El teléfono debe ingresarse como texto."
            )

        valor = valor.strip()

        if not valor.isdigit():
            raise ClienteInvalidoError(
                "El teléfono debe contener solamente números."
            )

        if len(valor) < 7 or len(valor) > 15:
            raise ClienteInvalidoError(
                "El teléfono debe tener entre 7 y 15 números."
            )

        self._telefono = valor

    def mostrar_informacion(self) -> str:
        """Devuelve la información principal del cliente."""

        return (
            f"Cliente: {self.nombre} | "
            f"Identificación: {self.identificador} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )