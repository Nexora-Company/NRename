# Nexora Rename

Una herramienta en Python diseñada para automatizar y gestionar el renombrado de archivos de forma masiva y eficiente, equipada con una interfaz gráfica de usuario (UI).

## 🚀 Características

- **Escaneo automático:** Detecta estructuras de archivos duplicados dentro del sistema.
- **Interfaz Gráfica:** Gestión visual y tabla de previsualización antes de aplicar cambios.
- **Sistema de Logs:** Registro detallado de todas las operaciones realizadas.

## 📦 Requisitos e Instalación

1. Asegúrate de tener Python 3.x instalado.
2. Clona este repositorio:
   ```bash
   git clone https://github.com
   cd NEXORARENAME
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Uso

Para iniciar la aplicación, ejecuta el archivo principal desde la consola:

```bash
python main.py
```

## 📂 Estructura del Proyecto

- `core/`: Lógica interna, escáner de archivos y subprocesos de renombrado.
- `ui/`: Ventana principal, estilos y tablas de la interfaz gráfica.
- `logs/`: Registros de ejecución (generados automáticamente).
