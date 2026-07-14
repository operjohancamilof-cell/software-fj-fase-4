import logging
from pathlib import Path


def configurar_logger() -> logging.Logger:
    """Configura el archivo de eventos y errores del sistema."""

    ruta_proyecto = Path(__file__).resolve().parent.parent
    carpeta_logs = ruta_proyecto / "logs"
    archivo_log = carpeta_logs / "sistema.log"

    carpeta_logs.mkdir(exist_ok=True)

    logger = logging.getLogger("software_fj")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        manejador_archivo = logging.FileHandler(
            archivo_log,
            encoding="utf-8"
        )

        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        manejador_archivo.setFormatter(formato)
        logger.addHandler(manejador_archivo)

    return logger