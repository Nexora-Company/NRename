# Nexora Rename

Una herramienta de escritorio en Python diseñada para automatizar y gestionar el renombrado masivo de archivos multimedia de forma eficiente, equipada con una interfaz gráfica de usuario (UI) bajo el sistema de diseño oficial de **Nexora**.

---

## 🚀 Características

- **Análisis y Escaneo Asíncrono:** Procesa imágenes (`.jpg`, `.png`, `.webp`, `.heic`, etc.) y vídeos (`.mp4`, `.mov`, `.mkv`, etc.) sin congelar la interfaz gracias a un sistema de hilos (`QThread`).

- **Inyección y Actualización de Metadatos:** Integra **ExifTool** para escribir etiquetas de título, autoría ("Saarmyx"), software e identificadores únicos de manera transparente.

- **Detección Inteligente de Duplicados:** Algoritmo de verificación por bloques Hash SHA256 (1MB) que evita sobrescribir archivos o procesar duplicados exactos.

- **Sistema de Deshacer (Undo):** Registro persistente en `history.json` para revertir operaciones de renombrado de forma segura.

- **Interfaz Nexora Design System:** Estética industrial monocromática (`#0A0A0A`) con acentos en rojo marca (`#E11D2E`), tabla interactiva de previsualización y soporte para _Drag & Drop_.

---

## 📦 Requisitos e Instalación

1. **Python 3.x** instalado.
2. Clona este repositorio:

   ```bash
   git clone [https://github.com/tu-usuario/NEXORARENAME.git](https://github.com/tu-usuario/NEXORARENAME.git)
   cd NEXORARENAME
   ```

3. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt

```

4. **ExifTool:** Asegúrate de tener el ejecutable `exiftool.exe` ubicado en la raíz del proyecto.

---

## 🛠️ Uso

Para iniciar la aplicación, ejecuta el archivo principal desde la consola:

```bash
python main.py

```

---

## 📂 Estructura del Proyecto

```text
NEXORARENAME/
├── core/
│   ├── execute_rename.py    # Lógica de renombrado, hashing y conflictos
│   ├── history.json_writer  # Gestión de historial y restauración (undo)
│   ├── metadata_writer.py  # Integración con ExifTool y ocultación de consola CMD
│   ├── metadata.py         # Extracción de fechas EXIF / MediaInfo
│   ├── rename_worker.py    # QThread para ejecución de renombrado
│   ├── renamer.py          # Generador de nombres basados en marcas de tiempo
│   ├── scanner.py          # Recopilador e inspector de carpetas
│   └── worker.py           # QThread para escaneo asíncrono
├── ui/
│   ├── main_window.py      # Ventana principal y gestión de eventos
│   ├── preview_table.py    # Tabla personalizada con menú contextual
│   └── styles.py           # Estilos QSS (Nexora Design Tokens)
├── exiftool.exe            # Binario para inyección de metadatos
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Lista de dependencias del proyecto
└── .gitignore              # Exclusiones de Git

```
