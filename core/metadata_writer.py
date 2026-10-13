import sys
import subprocess
import hashlib
import shutil
from pathlib import Path

APP_DISPLAY_NAME = "Nexora Rename"
METADATA_AUTHOR_DEFAULT = "Nexora"

def get_exiftool_path():
    """Detecta la ruta del binario exiftool según el SO."""
    if sys.platform == "win32":
        bundled = Path(__file__).resolve().parent.parent / "exiftool.exe"
        if bundled.exists():
            return str(bundled)
        return shutil.which("exiftool") or "exiftool"
    else:
        # Busca en el PATH del sistema (instalado vía apt)
        return shutil.which("exiftool") or "exiftool"

EXIFTOOL_PATH = get_exiftool_path()

def update_metadata(file_path: Path, new_name: str, author: str = METADATA_AUTHOR_DEFAULT):
    """Actualiza metadatos de forma segura en Linux y Windows."""
    title = Path(new_name).stem
    unique_id = hashlib.sha1(f"{title}_{file_path}".encode("utf-8")).hexdigest()

    command = [
        EXIFTOOL_PATH,
        f"-Title={title}", f"-Subject={title}", f"-Description={title}",
        f"-Artist={author}", f"-Creator={author}",
        f"-Software={APP_DISPLAY_NAME}", "-overwrite_original",
        str(file_path)
    ]

    startupinfo = None
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
        result = subprocess.run(command, capture_output=True, text=True, startupinfo=startupinfo, timeout=60)
        return result.returncode == 0
    except FileNotFoundError:
        print(f"\n[ERROR METADATA] exiftool no encontrado: {EXIFTOOL_PATH}")
        return False
    except Exception as e:
        print(f"\n[ERROR METADATA] {file_path}\n{e}")
        return False
