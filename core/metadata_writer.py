import sys
import subprocess
import hashlib
from pathlib import Path

# Ruta limpia al ejecutable de ExifTool en la raíz del proyecto
EXIFTOOL_PATH = str(
    Path(__file__).resolve().parent.parent / "exiftool.exe"
)


def update_metadata(
        file_path: Path,
        new_name: str,
        author: str = "Saarmyx"):
    """
    Actualiza los metadatos del archivo usando ExifTool.
    """

    title = Path(new_name).stem

    # ID único basado en nombre + ruta
    unique_id = hashlib.sha1(
        f"{title}_{file_path}".encode("utf-8")
    ).hexdigest()

    command = [
        EXIFTOOL_PATH,

        # TÍTULOS
        f"-Title={title}",
        f"-Subject={title}",
        f"-Description={title}",
        f"-ImageDescription={title}",
        f"-Comment={title}",
        f"-Caption-Abstract={title}",
        f"-Headline={title}",
        f"-ObjectName={title}",

        # WINDOWS EXPLORER
        f"-XPTitle={title}",
        f"-XPSubject={title}",
        f"-XPComment={title}",
        f"-XPKeywords={title}",

        # XMP
        f"-XMP-dc:Title={title}",
        f"-XMP-dc:Description={title}",
        f"-XMP-dc:Subject={title}",
        f"-XMP-dc:Identifier={unique_id}",

        # IDS INTERNOS
        f"-DocumentName={title}",
        f"-ImageUniqueID={title}",
        f"-OriginalDocumentID={unique_id}",
        f"-DocumentID={unique_id}",
        f"-InstanceID={unique_id}",
        f"-XMP-xmpMM:DocumentID={unique_id}",
        f"-XMP-xmpMM:InstanceID={unique_id}",

        # AUTORÍA
        f"-Artist={author}",
        f"-Author={author}",
        f"-Creator={author}",
        f"-OwnerName={author}",
        f"-Copyright={author}",

        # SOFTWARE
        "-Software=NexoraRename",
        "-CreatorTool=NexoraRename",

        # GUARDAR
        "-overwrite_original",

        str(file_path)
    ]

    # Ocultar ventana emergente de CMD en Windows
    startupinfo = None
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            startupinfo=startupinfo
        )

        stderr = result.stderr

        # Errores menores o advertencias que se ignoran
        ignored_errors = [
            "Not a valid HEIC",
            "Not a valid JPG",
            "looks more like",
            "Unknown trailer",
            "SampleTable",
            "minor",
            "Warning"
        ]

        if result.returncode != 0:
            if any(err in stderr for err in ignored_errors):
                return True

            print(f"\n[METADATA ERROR] {file_path}\n{stderr}")
            return False

        return True

    except FileNotFoundError:
        print("\n[EXIFTOOL ERROR] No se encontró exiftool.exe en la raíz.")
        return False

    except Exception as e:
        print(f"\n[ERROR METADATA] {file_path}\n{e}")
        return False