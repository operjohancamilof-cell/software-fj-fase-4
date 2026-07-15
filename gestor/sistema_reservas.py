from excepciones.excepciones_personalizadas import (
    ClienteInvalidoError,
    ReservaInvalidaError,
    ServicioInvalidoError,
)
from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.servicio import Servicio


class SistemaReservas:
    """Gestiona clientes, servicios y reservas mediante listas internas."""

    def __init__(self) -> None:
        """Inicializa las listas internas del sistema."""

        self._clientes: list[Cliente] = []
        self._servicios: list[Servicio] = []
        self._reservas: list[Reserva] = []

    @property
    def clientes(self) -> list[Cliente]:
        """Devuelve una copia de la lista de clientes."""

        return self._clientes.copy()

    @property
    def servicios(self) -> list[Servicio]:
        """Devuelve una copia de la lista de servicios."""

        return self._servicios.copy()

    @property
    def reservas(self) -> list[Reserva]:
        """Devuelve una copia de la lista de reservas."""

        return self._reservas.copy()

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente y evita identificaciones duplicadas."""

        if not isinstance(cliente, Cliente):
            raise ClienteInvalidoError(
                "Solo se pueden registrar objetos de tipo Cliente."
            )

        for cliente_registrado in self._clientes:
            if (
                cliente_registrado.identificador
                == cliente.identificador
            ):
                raise ClienteInvalidoError(
                    "Ya existe un cliente con la identificación "
                    f"{cliente.identificador}."
                )

        self._clientes.append(cliente)

    def registrar_servicio(self, servicio: Servicio) -> None:
        """Registra un servicio y evita códigos duplicados."""

        if not isinstance(servicio, Servicio):
            raise ServicioInvalidoError(
                "Solo se pueden registrar objetos de tipo Servicio."
            )

        for servicio_registrado in self._servicios:
            if servicio_registrado.codigo == servicio.codigo:
                raise ServicioInvalidoError(
                    "Ya existe un servicio con el código "
                    f"{servicio.codigo}."
                )

        self._servicios.append(servicio)

    def registrar_reserva(self, reserva: Reserva) -> None:
        """Registra una reserva y evita códigos duplicados."""

        if not isinstance(reserva, Reserva):
            raise ReservaInvalidaError(
                "Solo se pueden registrar objetos de tipo Reserva."
            )

        for reserva_registrada in self._reservas:
            if reserva_registrada.codigo == reserva.codigo:
                raise ReservaInvalidaError(
                    "Ya existe una reserva con el código "
                    f"{reserva.codigo}."
                )

        self._reservas.append(reserva)

    def buscar_cliente(self, identificacion: str) -> Cliente:
        """Busca un cliente por su identificación."""

        for cliente in self._clientes:
            if cliente.identificador == identificacion:
                return cliente

        raise ClienteInvalidoError(
            f"No existe un cliente con la identificación {identificacion}."
        )

    def buscar_servicio(self, codigo: str) -> Servicio:
        """Busca un servicio por su código."""

        for servicio in self._servicios:
            if servicio.codigo == codigo:
                return servicio

        raise ServicioInvalidoError(
            f"No existe un servicio con el código {codigo}."
        )

    def buscar_reserva(self, codigo: str) -> Reserva:
        """Busca una reserva por su código."""

        for reserva in self._reservas:
            if reserva.codigo == codigo:
                return reserva

        raise ReservaInvalidaError(
            f"No existe una reserva con el código {codigo}."
        )

    def mostrar_resumen(self) -> str:
        """Devuelve la cantidad de registros almacenados."""

        return (
            f"Clientes registrados: {len(self._clientes)}\n"
            f"Servicios registrados: {len(self._servicios)}\n"
            f"Reservas registradas: {len(self._reservas)}"
        )