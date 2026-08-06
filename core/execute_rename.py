import hashlib
from pathlib import Path

from core.history import add_history_entry
from core.metadata_writer import update_metadata


def sha256_file(path: Path):
    """
    Calcula el hash SHA256 del archivo por bloques de 1MB.
    """
    sha = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                sha.update(chunk)
        return sha.hexdigest()
    except Exception:
        return None


def generate_conflict_name(directory: Path, base_name: str, extension: str):
    """
    Genera nombres únicos secuenciales en caso de conflicto.
    """
    counter = 1
    while True:
        candidate = directory / f"{base_name}_{counter:03d}{extension}"
        if not candidate.exists():
            return candidate
        counter += 1


def execute_rename(files, progress_callback=None):
    """
    Ejecuta el renombrado masivo y actualización de metadatos.
    """
    stats = {
        "renamed": 0,
        "duplicates": 0,
        "conflicts": 0,
        "metadata_updated": 0,
        "errors": 0
    }

    known_hashes = {}
    total = len(files)

    for index, file in enumerate(files, start=1):
        try:
            source = Path(file["path"])

            if not source.exists():
                continue

            destination = source.parent / file["new"]

            # =================================
            # MISMO NOMBRE
            # =================================
            if source == destination:
                if update_metadata(source, source.name, author="Saarmyx"):
                    stats["metadata_updated"] += 1
                continue

            # =================================
            # HASH GLOBAL Y DUPLICADOS
            # =================================
            source_hash = sha256_file(source)

            if source_hash:
                if source_hash in known_hashes:
                    stats["duplicates"] += 1
                    continue
                known_hashes[source_hash] = source

            # =================================
            # CONFLICTOS
            # =================================
            if destination.exists():
                # Comparación optimizada sin re-calcular el hash del source
                if source.stat().st_size == destination.stat().st_size:
                    dest_hash = sha256_file(destination)
                    if source_hash and dest_hash and source_hash == dest_hash:
                        stats["duplicates"] += 1
                        continue

                destination = generate_conflict_name(
                    destination.parent,
                    destination.stem,
                    destination.suffix
                )
                stats["conflicts"] += 1

            # =================================
            # RENOMBRAR E HISTORIAL
            # =================================
            source.rename(destination)
            stats["renamed"] += 1

            add_history_entry(source, destination)

            # =================================
            # ACTUALIZAR METADATOS
            # =================================
            if update_metadata(destination, destination.name, author="Saarmyx"):
                stats["metadata_updated"] += 1

        except Exception as e:
            print(f"[RENAME ERROR] {source} -> {e}")
            stats["errors"] += 1

        # PROGRESO
        if progress_callback:
            progress = int((index / total) * 100)
            progress_callback(progress)

    return stats