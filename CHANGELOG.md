# Changelog

## [1.1.0] — 2026-10-13

### Cambiado

- Identidad visual alineada a tokens oficiales de Nexora (`ui/tokens.py`): fondos `#0D0D0F`/`#131317`/`#191A1E`/`#1F2024`, borde `#26272C`, rojo `#A50021`/`#8E001C`/`#FF8497`. Se eliminan hex no oficiales.
- Marca normalizada a `Nexora Rename` en título de ventana, metadatos `Software` y empaquetado. Autoría de metadatos pasa de valor personal a `Nexora`.
- Historial movido a `~/.nexora-rename/history.json` (con migración única desde el archivo heredado) para no versionar datos personales.
- `requirements.txt` con versiones mínimas y Python 3.11+.
- `build_deb.sh` robusto (`set -euo pipefail`), versión parametrizada y copia del icono al paquete.
- `README.md` reescrito a estándar técnico Nexora y `.gitignore` de producción para Python/Qt.

### Seguridad y repo

- Se desindexan del repositorio `history.json` (rutas personales), `__pycache__`, `*.code-workspace` y vendor `exiftool.exe`/`exiftool_files/`. ExifTool pasa a dependencia externa documentada.
- `update_metadata` con `timeout`, manejo de binario ausente y sin cambios de comportamiento salvo valores de marca.
