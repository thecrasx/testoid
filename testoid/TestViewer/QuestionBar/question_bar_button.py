from PySide6.QtWidgets import QWidget, QPushButton, QSizePolicy
from PySide6.QtCore import QObject, Signal
from testoid.Tools.stylesheet import load as ssLoad


class _StyleSheet:
    NORMAL = ssLoad("question-bar-button-normal")
    SELECTED = ssLoad("question-bar-button-selected")
    MARK_NORMAL = ssLoad("question-bar-button-mark-normal")
    MARK_SELECTED = ssLoad("question-bar-button-mark-selected")
    DISABLED = ssLoad("question-bar-button-disabled")



class _CustomSignal(QObject):
    selected = Signal(object)


class QuestionBarButton(QPushButton):
    def __init__(self, parent: QWidget, ID: int = 0):
        super().__init__(parent)
        self.__ID = ID

        self.__customSignal = _CustomSignal()
        self.selected = self.__customSignal.selected

        self.__selected: bool = False
        self.__marked: bool = False
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
        self.__selected = selected
        self.__changeStyleSheet(self.__selected, self.__marked)

        if selected:
            self.selected.emit(self)

    
    def setDisabled(self):
        super().setDisabled(True)
        self.setStyleSheet(_StyleSheet.DISABLED)

    
    def setEnabled(self):
        super().setEnabled(True)
        self.setStyleSheet(_StyleSheet.NORMAL)


    def mark(self):
        self.__marked = True
        self.__changeStyleSheet(self.__selected, self.__marked)


    def unmark(self):
        self.__marked = False
        self.__changeStyleSheet(self.__selected, self.__marked)

    
    def isMarked(self) -> bool:
        return self.__marked


    
    def __onButtonClick(self):
        if not self.__selected:
            self.setSelected(True)


    def __changeStyleSheet(self, selected, marked):
        if marked:
            if selected:
                self.setStyleSheet(_StyleSheet.MARK_SELECTED)
            else:
                self.setStyleSheet(_StyleSheet.MARK_NORMAL)
        else:
            if selected:
                self.setStyleSheet(_StyleSheet.SELECTED)
            else:
                self.setStyleSheet(_StyleSheet.NORMAL)
