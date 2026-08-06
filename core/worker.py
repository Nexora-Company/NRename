from PySide6.QtCore import (
    QThread,
    Signal
)

from core.scanner import scan_folders


class ScanWorker(QThread):

    # Señales

    progress = Signal(int)
    finished_scan = Signal(list)
    error = Signal(str)

    def __init__(self, folders):
        super().__init__()

        self.folders = folders
        self._running = True

    def stop(self):
        """
        Permite detener el escaneo.
        """

        self._running = False

    def run(self):

        try:

            files = scan_folders(
                self.folders,
                self.progress.emit
            )

            if self._running:
                self.finished_scan.emit(
                    files
                )

        except Exception as e:

            self.error.emit(
                str(e)
            )