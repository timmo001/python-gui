"""Python GUI GUI: Main window"""
from argparse import Namespace

from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtWidgets import QFrame, QVBoxLayout

from ..base import Base


class MainWindow(Base, QFrame):
    """Main Window"""

    def __init__(
        self,
        args: Namespace,
        icon: QIcon,
    ) -> None:
        """Initialize the window"""
        Base.__init__(self, args)
        QFrame.__init__(self)

        self.setWindowTitle("Python GUI")
        self.setWindowIcon(icon)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.browser)

    # pylint: disable=invalid-name
    def closeEvent(self, event: QCloseEvent) -> None:
        """Close the window instead of closing the app"""
        event.ignore()
        self.hide()
