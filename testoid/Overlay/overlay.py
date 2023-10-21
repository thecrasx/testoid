from PySide6.QtWidgets import QVBoxLayout, QWidget, QFrame
from PySide6.QtCore import QSize, Signal


class Overlay(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setOverlayOpacity(0)
        self.move(0, 0)

        self.__layout = QVBoxLayout(self)
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSpacing(0)
        self.setLayout(self.__layout)

        self.__titleBarHeight = 0

        self.__frame = QFrame(self)
        self.__layout.addWidget(self.__frame)
        self.__frameLayout = QVBoxLayout(self.__frame)
        self.__frame.setLayout(self.__frameLayout)


    def setParentResizeSignal(self, resizeSignal: Signal):
        resizeSignal.connect(self.updateSize)

    def setTitleBarOffset(self, titleBar):
        self.__titleBarHeight = titleBar.height() - 2
        self.move(0, self.__titleBarHeight)

    def updateSize(self):
        self.resize(self.parentWidget().size() - QSize(0, self.__titleBarHeight))
    
    def addWidget(self, widget: QWidget):
        widget.setParent(self.__frame)
        self.__frameLayout.addWidget(widget)


    def setOverlayOpacity(self, opacity):
        self.setStyleSheet(f"background: rgba(0, 0, 0, {opacity});")

    
    def setPadding(self, left: int, top: int, right: int, bottom: int):
        self.__frameLayout.setContentsMargins(left, top, right, bottom)
    
    def setEqualPadding(self, padding: int):
        self.__frameLayout.setContentsMargins(padding, padding, padding, padding)