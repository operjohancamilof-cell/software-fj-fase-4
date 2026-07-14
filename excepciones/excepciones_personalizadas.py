class SistemaFJError(Exception):
    """Excepción general para los errores controlados del sistema."""


class ClienteInvalidoError(SistemaFJError):
    """Se genera cuando los datos de un cliente son inválidos."""


class ServicioInvalidoError(SistemaFJError):
    """Se genera cuando los datos de un servicio son inválidos."""


class ServicioNoDisponibleError(SistemaFJError):
    """Se genera cuando un servicio solicitado no está disponible."""


class ReservaInvalidaError(SistemaFJError):
    """Se genera cuando los datos de una reserva son inválidos."""


class OperacionNoPermitidaError(SistemaFJError):
    """Se genera cuando una operación no puede realizarse."""