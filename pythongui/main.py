"""Python GUI GUI: Main class"""
from argparse import Namespace
import asyncio
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from .base import Base
from .system_tray import SystemTray
from .window.main import MainWindow


class Main(Base):
    """Main class"""

    def __init__(
        self,
        args: Namespace,
    ) -> None:
        """Initialize the main class"""
        super().__init__(args)

        self.application = QApplication([])
        self.icon = QIcon("public/icon.png")
        self.application.setStyleSheet(
            """
            QWidget {
                color: #FFFFFF;
                background-color: #212121;
            }

            QMenu {
                background-color: #292929;
            }

            QMenu::item {
                background-color: transparent;
            }

            QMenu::item:selected {
                background-color: #757575;
            }
            """
        )

        self.main_window = MainWindow(
            self.args,
            self.icon,
        )
        self.main_window.resize(1280, 720)
        self.main_window.showNormal()
        self.main_window.hide()

        self.system_tray_icon = SystemTray(
            self.args,
            self.icon,
            self.application,
            self.callback_exit_application,
            self.callback_show_window,
        )
        self.system_tray_icon.show()

        sys.exit(self.application.exec())

    def callback_exit_application(self) -> None:
        """Exit the application"""
        self.logger.info("Exiting application..")
        self.application.quit()

    def callback_show_window(
        self,
        path: str,
        maximized: bool,
        width: int = 1280,
        height: int = 720,
    ) -> None:
        """Show the main window"""
        self.logger.info("Showing window: %s", path)

        self.main_window.hide()
        self.main_window.setup(path)
        self.main_window.resize(width, height)
        screen_geometry = self.application.primaryScreen().availableSize()
        self.main_window.move(
            (screen_geometry.width() - self.main_window.width()) / 2,
            (screen_geometry.height() - self.main_window.height()) / 2,
        )
        if maximized:
            self.main_window.showMaximized()
        else:
            self.main_window.showNormal()
