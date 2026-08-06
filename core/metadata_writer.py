import sys
import subprocess
import hashlib
import shutil
from pathlib import Path

def get_exiftool_path():
    """Detecta la ruta del binario exiftool según el SO."""
    if sys.platform == "win32":
        return str(Path(__file__).resolve().parent.parent / "exiftool.exe")
    else:
        # Busca en el PATH del sistema (instalado vía apt)
        return shutil.which("exiftool") or "exiftool"

EXIFTOOL_PATH = get_exiftool_path()

def update_metadata(file_path: Path, new_name: str, author: str = "Saarmyx"):
    """Actualiza metadatos de forma segura en Linux y Windows."""
    title = Path(new_name).stem
    unique_id = hashlib.sha1(f"{title}_{file_path}".encode("utf-8")).hexdigest()

    command = [
        EXIFTOOL_PATH,
        f"-Title={title}", f"-Subject={title}", f"-Description={title}",
        f"-Artist={author}", f"-Creator={author}",
        "-Software=NexoraRename", "-overwrite_original",
        str(file_path)
    ]

    startupinfo = None
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
        result = subprocess.run(command, capture_output=True, text=True, startupinfo=startupinfo)
        return result.returncode == 0
    except Exception as e:
        print(f"\n[ERROR METADATA] {file_path}\n{e}")
        return False