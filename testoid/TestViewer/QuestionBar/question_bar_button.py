from PySide6.QtWidgets import QWidget, QPushButton, QSizePolicy
from PySide6.QtCore import QObject, Signal
from testoid.Tools.stylesheet import load as ssLoad


class _StyleSheet:
    NORMAL = ssLoad("question-bar-button-normal")
    SELECTED = ssLoad("question-bar-button-selected")



class _CustomSignal(QObject):
    selected = Signal(object)


class QuestionBarButton(QPushButton):
    def __init__(self, parent: QWidget, ID: int = 0):
        super().__init__(parent)
        self.__ID = ID

        self.__customSignal = _CustomSignal()
        self.selected = self.__customSignal.selected

        self.__selected: bool = False
        self.clicked.connect(self.__onButtonClick)

        self.setFixedWidth(50)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setStyleSheet(_StyleSheet.NORMAL)
        self.show()


    @property
    def ID(self) -> int:
        return self.__ID


    def isSelected(self) -> bool:
        return self.__selected
    

    def setSelected(self, selected: bool):
        if selected:
            self.setStyleSheet(_StyleSheet.SELECTED)
            self.selected.emit(self)
        else:
            self.setStyleSheet(_StyleSheet.NORMAL)

        self.__selected = selected

    
    def __onButtonClick(self):
        if not self.__selected:
            self.setSelected(True)
