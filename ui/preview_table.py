import os
import subprocess

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QAction, QDesktopServices
from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMenu,
    QMessageBox
)

from PySide6.QtCore import QUrl


class PreviewTable(QTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_table()

    # ==================================================
    # CONFIGURACIÓN
    # ==================================================

    def setup_table(self):

        self.setColumnCount(3)

        self.setHorizontalHeaderLabels([
            "Carpeta",
            "Nombre Actual",
            "Nuevo Nombre"
        ])

        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.setSortingEnabled(True)

        self.setAlternatingRowColors(True)

        self.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.setContextMenuPolicy(
            Qt.CustomContextMenu
        )

        self.customContextMenuRequested.connect(
            self.show_context_menu
        )

    # ==================================================
    # CARGAR DATOS
    # ==================================================

    def load_files(self, files):

        self.setSortingEnabled(False)

        self.setRowCount(len(files))

        for row, file in enumerate(files):

            self.setItem(
                row,
                0,
                QTableWidgetItem(
                    file["folder"]
                )
            )

            self.setItem(
                row,
                1,
                QTableWidgetItem(
                    file["original"]
                )
            )

            self.setItem(
                row,
                2,
                QTableWidgetItem(
                    file["new"]
                )
            )

        self.setSortingEnabled(True)

    # ==================================================
    # MENÚ CONTEXTUAL
    # ==================================================

    def show_context_menu(self, pos: QPoint):

        row = self.currentRow()

        if row < 0:
            return

        menu = QMenu(self)

        open_file_action = QAction(
            "Abrir archivo",
            self
        )

        open_folder_action = QAction(
            "Abrir carpeta",
            self
        )

        copy_path_action = QAction(
            "Copiar ruta",
            self
        )

        menu.addAction(open_file_action)
        menu.addAction(open_folder_action)
        menu.addSeparator()
        menu.addAction(copy_path_action)

        open_file_action.triggered.connect(
            self.open_file
        )

        open_folder_action.triggered.connect(
            self.open_folder
        )

        copy_path_action.triggered.connect(
            self.copy_path
        )

        menu.exec(
            self.viewport().mapToGlobal(pos)
        )

    # ==================================================
    # UTILIDADES
    # ==================================================

    def get_selected_path(self):

        row = self.currentRow()

        if row < 0:
            return None

        folder = self.item(row, 0).text()
        original = self.item(row, 1).text()

        return os.path.join(
            folder,
            original
        )

    def open_file(self):

        path = self.get_selected_path()

        if not path:
            return

        try:

            QDesktopServices.openUrl(
                QUrl.fromLocalFile(path)
            )

        except Exception as e:

            QMessageBox.warning(
                self,
                "Error",
                str(e)
            )

    def open_folder(self):

        path = self.get_selected_path()

        if not path:
            return

        try:

            if os.name == "nt":

                subprocess.run([
                    "explorer",
                    "/select,",
                    os.path.normpath(path)
                ])

            else:

                QDesktopServices.openUrl(
                    QUrl.fromLocalFile(
                        os.path.dirname(path)
                    )
                )

        except Exception as e:

            QMessageBox.warning(
                self,
                "Error",
                str(e)
            )

    def copy_path(self):

        path = self.get_selected_path()

        if not path:
            return

        clipboard = self.window().clipboard()

        if clipboard:
            clipboard.setText(path)