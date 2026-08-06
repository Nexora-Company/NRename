from pathlib import Path

from core.metadata import (
    get_best_datetime,
    VIDEO_EXTENSIONS
)


def is_motion_photo(path: Path):
    """
    Detecta Motion Photos de Android/iPhone.
    """

    name = path.stem.lower()

    return any(keyword in name for keyword in [
        "mvimg",
        "motion_photo",
        "motionphoto",
        "live",
        "livephoto"
    ])


def sanitize_filename(filename: str):
    """
    Elimina caracteres inválidos para Windows.
    """

    invalid_chars = '<>:"/\\|?*'

    for char in invalid_chars:
        filename = filename.replace(char, "_")

    return filename.strip()


def get_prefix(path: Path):
    """
    Determina el prefijo del archivo.
    """

    if is_motion_photo(path):
        return "MVIMG"

    if path.suffix.lower() in VIDEO_EXTENSIONS:
        return "VID"

    return "IMG"


def generate_name(path: Path):
    """
    Genera un nombre único basado en fecha.
    """

    dt = get_best_datetime(path)

    timestamp = dt.strftime(
        "%Y%m%d_%H%M%S"
    )

    prefix = get_prefix(path)

    filename = (
        f"{prefix}_{timestamp}"
    )

    filename = sanitize_filename(
        filename
    )

    return (
        f"{filename}"
        f"{path.suffix.lower()}"
    )


def generate_custom_name(
        path: Path,
        base_name: str):
    """
    Permite nombres personalizados.
    Ejemplo:
    ViajeCartagena_20260625_150000.jpg
    """

    dt = get_best_datetime(path)

    timestamp = dt.strftime(
        "%Y%m%d_%H%M%S"
    )

    base_name = sanitize_filename(
        base_name
    )

    return (
        f"{base_name}_"
        f"{timestamp}"
        f"{path.suffix.lower()}"
    )