from pathlib import Path
from datetime import datetime

from PIL import Image, ExifTags

try:
    from pymediainfo import MediaInfo
except ImportError:
    MediaInfo = None


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".heic",
    ".bmp",
    ".tiff"
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".mkv",
    ".avi",
    ".webm",
    ".3gp",
    ".m4v"
}

EXIF_DATETIME_TAGS = {
    "DateTimeOriginal",
    "DateTimeDigitized",
    "DateTime"
}


def get_exif_datetime(path: Path):
    """
    Obtiene la fecha EXIF de una imagen.
    """

    try:
        with Image.open(path) as img:

            exif = img.getexif()

            if not exif:
                return None

            for tag_id, value in exif.items():

                tag_name = ExifTags.TAGS.get(
                    tag_id,
                    tag_id
                )

                if tag_name in EXIF_DATETIME_TAGS:

                    try:
                        return datetime.strptime(
                            str(value),
                            "%Y:%m:%d %H:%M:%S"
                        )
                    except Exception:
                        continue

    except Exception:
        pass

    return None


def get_video_datetime(path: Path):
    """
    Obtiene la fecha real de creación de vídeos.
    """

    if MediaInfo is None:
        return None

    try:

        media_info = MediaInfo.parse(
            str(path)
        )

        for track in media_info.tracks:

            if track.track_type != "General":
                continue

            candidates = [
                getattr(track, "recorded_date", None),
                getattr(track, "tagged_date", None),
                getattr(track, "file_last_modification_date", None)
            ]

            for date_value in candidates:

                if not date_value:
                    continue

                try:

                    date_value = (
                        date_value
                        .replace("UTC ", "")
                        .replace("Z", "")
                    )

                    return datetime.fromisoformat(
                        date_value
                    )

                except Exception:
                    continue

    except Exception:
        pass

    return None


def get_filesystem_datetime(path: Path):
    """
    Usa la fecha de modificación del sistema.
    """

    try:
        return datetime.fromtimestamp(
            path.stat().st_mtime
        )
    except Exception:
        return datetime.now()


def get_best_datetime(path: Path):
    """
    Obtiene la mejor fecha disponible.
    Prioridad:

    1. EXIF
    2. Metadata vídeo
    3. Fecha modificación
    """

    ext = path.suffix.lower()

    if ext in IMAGE_EXTENSIONS:

        dt = get_exif_datetime(path)

        if dt:
            return dt

    elif ext in VIDEO_EXTENSIONS:

        dt = get_video_datetime(path)

        if dt:
            return dt

    return get_filesystem_datetime(path)