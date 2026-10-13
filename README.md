# Nexora Rename

Herramienta de escritorio de Nexora para organizar y renombrar de forma masiva fotos y vídeos por fecha real de captura.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![PySide6](https://img.shields.io/badge/Qt-PySide6-16161A)
![Platforms](https://img.shields.io/badge/Platforms-Windows%20%7C%20Linux-lightgrey)

## Propósito e integración

Responsabilidad única (SRP): escanear carpetas, proponer nombres `IMG_/VID_` basados en EXIF/metadatos multimedia y ejecutar el renombrado con detección de duplicados (SHA256), inyección de metadatos y deshacer seguro.

Se integra en el ecosistema Nexora como utilidad de escritorio autónoma. Identidad visual: tokens oficiales de Nexora (modo oscuro `#0D0D0F` / `#131317`, rojo de marca `#A50021`).

## Estructura del proyecto

```text
NexoraRename/
├── main.py
├── core/
│   ├── scanner.py
│   ├── renamer.py
│   ├── metadata.py
│   ├── metadata_writer.py
│   ├── execute_rename.py
│   ├── history.py
│   ├── worker.py
│   └── rename_worker.py
├── ui/
│   ├── main_window.py
│   ├── preview_table.py
│   ├── styles.py
│   └── tokens.py
└── resources/
    └── IconRename.png
```

## Funcionalidades principales

- Renombrado por fecha real: EXIF en imágenes, metadatos multimedia en vídeo, fecha de modificación como respaldo.
- Previsualización antes de renombrar con tabla de carpeta, nombre actual y nuevo nombre.
- Detección de duplicados por SHA256 y resolución de conflictos con sufijo secuencial `_001`.
- Inyección de metadatos (título, autoría `Nexora`) vía ExifTool.
- Historial local con deshacer (`~/.nexora-rename/history.json`).
- Drag & drop de carpetas y menú contextual (abrir archivo/carpeta, copiar ruta).
- Formatos: imágenes `.jpg` `.jpeg` `.png` `.webp` `.heic` `.bmp` `.tiff`; vídeos `.mp4` `.mov` `.mkv` `.avi` `.webm` `.3gp` `.m4v`.

## Inicio rápido

Requisito externo: ExifTool disponible en `PATH` (Windows: `exiftool.exe` junto al proyecto o en `PATH`; Linux: `sudo apt install libimage-exiftool-perl`).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Flujo de uso: agregar carpeta o arrastrarla a la ventana, pulsar Analizar, revisar la previsualización, pulsar Renombrar, usar Deshacer cambios solo si se necesita revertir la última operación.

## Desarrollo local y pruebas

```bash
pip install -r requirements.txt
python -m compileall core ui main.py
python main.py
pyinstaller --noconfirm --windowed --name NexoraRename main.py
bash build_deb.sh
```

Sin suite de pruebas automatizadas actualmente. Verificación mínima exigida antes de cada cambio: compilación con `compileall` y arranque manual con Analizar y Renombrar sobre una carpeta de prueba.

## Estándar de contribución

Commits atómicos con rutas explícitas y Conventional Commits (`feat`, `fix`, `style`, `refactor`, `chore`, `test`). Prohibido `git add .`.

```bash
git add core/scanner.py ui/main_window.py
git commit -m "feat(core): ejemplo de cambio atómico"
```

## Soporte

Reportar problemas y propuestas en la pestaña Issues del repositorio.
