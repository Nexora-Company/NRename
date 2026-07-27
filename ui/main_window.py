from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QLabel,
    QFileDialog,
    QMessageBox,
    QProgressBar
)

from core.worker import ScanWorker
from core.rename_worker import RenameWorker
from core.history import (
    undo_last_operation,
    has_history
)

from ui.styles import DARK_STYLE
from ui.preview_table import PreviewTable


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.folders = []
        self.files = []

        self.scan_worker = None
        self.rename_worker = None

        self.setup_ui()

    # ==================================================
    # UI
    # ==================================================

    def setup_ui(self):
        self.setWindowTitle("NexoraRen v1.0")
        self.resize(1300, 800)
        self.setAcceptDrops(True)
        self.setStyleSheet(DARK_STYLE)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        # BOTONES SUPERIORES
        top_layout = QHBoxLayout()

        self.add_folder_btn = QPushButton("Agregar carpeta")
        self.remove_folder_btn = QPushButton("Eliminar carpeta")
        self.scan_btn = QPushButton("Analizar")
        self.rename_btn = QPushButton("Renombrar")
        self.undo_btn = QPushButton("Deshacer")

        top_layout.addWidget(self.add_folder_btn)
        top_layout.addWidget(self.remove_folder_btn)
        top_layout.addStretch()
        top_layout.addWidget(self.scan_btn)
        top_layout.addWidget(self.rename_btn)
        top_layout.addWidget(self.undo_btn)

        layout.addLayout(top_layout)

        # LISTA DE CARPETAS
        self.folder_list = QListWidget()
        self.folder_list.setMaximumHeight(140)
        layout.addWidget(self.folder_list)

        # TABLA DE PREVISUALIZACIÓN
        self.table = PreviewTable()
        layout.addWidget(self.table)

        # PROGRESO Y ESTADÍSTICAS
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.stats_label = QLabel("Listo")
        layout.addWidget(self.stats_label)

        # CONEXIONES
        self.add_folder_btn.clicked.connect(self.add_folder)
        self.remove_folder_btn.clicked.connect(self.remove_folder)
        self.scan_btn.clicked.connect(self.start_scan)
        self.rename_btn.clicked.connect(self.start_rename)
        self.undo_btn.clicked.connect(self.undo_changes)

        self.rename_btn.setEnabled(False)

    # ==================================================
    # CARPETAS
    # ==================================================

    def add_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta")
        if not folder:
            return

        if folder in self.folders:
            QMessageBox.information(
                self,
                "Información",
                "La carpeta ya fue agregada."
            )
            return

        self.folders.append(folder)
        self.folder_list.addItem(folder)

    def remove_folder(self):
        row = self.folder_list.currentRow()
        if row < 0:
            return

        self.folders.pop(row)
        self.folder_list.takeItem(row)

    # ==================================================
    # ESCANEO
    # ==================================================

    def start_scan(self):
        if not self.folders:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Seleccione al menos una carpeta."
            )
            return

        self.table.setRowCount(0)
        self.progress_bar.setValue(0)
        self.scan_btn.setEnabled(False)
        self.stats_label.setText("Analizando...")

        self.scan_worker = ScanWorker(self.folders)
        self.scan_worker.progress.connect(self.update_progress)
        self.scan_worker.finished_scan.connect(self.load_preview)
        self.scan_worker.error.connect(self.show_error)
        self.scan_worker.start()

    # ==================================================
    # PREVIEW
    # ==================================================

    def load_preview(self, files):
        self.files = files
        self.table.load_files(files)

        self.scan_btn.setEnabled(True)
        self.rename_btn.setEnabled(len(files) > 0)
        self.stats_label.setText(f"Archivos encontrados: {len(files)}")

    # ==================================================
    # RENOMBRADO
    # ==================================================

    def start_rename(self):
        if not self.files:
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            f"¿Renombrar {len(self.files)} archivos?"
        )

        if confirm != QMessageBox.Yes:
            return

        self.progress_bar.setValue(0)
        self.rename_btn.setEnabled(False)

        self.rename_worker = RenameWorker(self.files)
        self.rename_worker.progress.connect(self.update_progress)
        self.rename_worker.finished_rename.connect(self.finish_rename)
        self.rename_worker.error.connect(self.show_error)
        self.rename_worker.start()

    def finish_rename(self, stats):
        self.stats_label.setText(
            f"Renombrados: {stats['renamed']} | "
            f"Duplicados: {stats['duplicates']} | "
            f"Conflictos: {stats['conflicts']} | "
            f"Metadatos: {stats['metadata_updated']} | "
            f"Errores: {stats['errors']}"
        )

        self.rename_btn.setEnabled(False)
        QMessageBox.information(
            self,
            "Finalizado",
            "Proceso completado correctamente."
        )

    # ==================================================
    # DESHACER
    # ==================================================

    def undo_changes(self):
        if not has_history():
            QMessageBox.information(
                self,
                "Información",
                "No existe historial."
            )
            return

        confirm = QMessageBox.question(
            self,
            "Deshacer",
            "¿Desea restaurar todos los cambios?"
        )

        if confirm != QMessageBox.Yes:
            return

        stats = undo_last_operation()

        QMessageBox.information(
            self,
            "Restauración finalizada",
            f"Restaurados: {stats['restored']}\nErrores: {stats['errors']}"
        )

    # ==================================================
    # UTILIDADES
    # ==================================================

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def show_error(self, error):
        QMessageBox.critical(self, "Error", error)
        self.scan_btn.setEnabled(True)
        self.rename_btn.setEnabled(True)

    # ==================================================
    # DRAG & DROP
    # ==================================================

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            folder = url.toLocalFile()
            if folder and folder not in self.folders:
                self.folders.append(folder)
                self.folder_list.addItem(folder)