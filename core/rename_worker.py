from PySide6.QtCore import (
    QThread,
    Signal
)

from core.execute_rename import (
    execute_rename
)


class RenameWorker(QThread):

    # Señales

    progress = Signal(int)
    finished_rename = Signal(dict)
    error = Signal(str)

    def __init__(self, files):
        super().__init__()

        self.files = files
        self._running = True

    def stop(self):
        """
        Permite detener el proceso.
        """

        self._running = False

    def run(self):

        try:

            stats = execute_rename(
                self.files,
                self.progress.emit
            )

            if self._running:
                self.finished_rename.emit(
                    stats
                )

        except Exception as e:

            self.error.emit(
                str(e)
            )