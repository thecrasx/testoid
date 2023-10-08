from typing import Optional
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MenuLayout(QGridLayout):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)


        self.__widgetSizeHint: QSize = QSize(100, 100)





    def setWidgetSizeHint(self, size: QSize):
        self.__widgetSizeHint = size





    def widgetEvent(self, arg__1: QEvent) -> None:
        super().widgetEvent(arg__1)

        print("aaaa")