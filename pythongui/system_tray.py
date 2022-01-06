"""Python GUI GUI: System Tray"""
from argparse import Namespace
from collections.abc import Callable
from typing import Optional
from webbrowser import open_new_tab

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMenu, QSystemTrayIcon, QWidget

from .base import Base


class SystemTray(Base, QSystemTrayIcon):
    """System Tray"""

    def __init__(
        self,
        args: Namespace,
        icon: QIcon,
        parent: QWidget,
        callback_exit_application: Callable,
        callback_show_window: Callable[[str, bool, Optional[int], Optional[int]], None],
    ) -> None:
        """Initialize the system tray"""
        Base.__init__(self, args)
        QSystemTrayIcon.__init__(self, icon, parent)

        self.callback_show_window = callback_show_window

        menu = QMenu()

        menu.addSeparator()

        action_exit: QAction = menu.addAction("Exit")
        action_exit.triggered.connect(callback_exit_application)

        self.setContextMenu(menu)
