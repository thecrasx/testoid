from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from testoid.Options.OptionWidget.option_widget_ui import Ui_OptionWidget
from testoid.Tools.stylesheet import load as ssLoad

class _CustomSignal(QObject):
    changed = Signal()

class _Options:
    def __init__(self) -> None:
        self.__defaultOption = None
        self.__defaultOptionIndex = -1
        self.__currentIndex = 0
        self.__optionsLen = 0

        self.__current = None
        self.__options = []

    @property





    def current(self):
        return self.__current
    
    @property





    def defaultOption(self):
        return self.__defaultOption





    def setDefaultOption(self, option: str):
        index = 0
        for _option in self.__options:
            if _option == option:
                self.__defaultOption = option
                self.__defaultOptionIndex = index
                break

            index += 1





    def setDefaultAsCurrent(self):
        if self.__defaultOptionIndex != -1:
            self.__current = self.__defaultOption
            self.__currentIndex = self.__defaultOptionIndex





    def all(self):
        return self.__options.copy()





    def next(self) -> str | None:
        if self.__currentIndex + 1 < self.__optionsLen:
            self.__currentIndex += 1

            self.__current = self.__options[self.__currentIndex]

            return self.__current
        
        return None





    def prev(self) -> str | None:
        if self.__currentIndex - 1 >= 0 and self.__optionsLen != 0:
            self.__currentIndex -= 1

            self.__current = self.__options[self.__currentIndex]

            return self.__current
        
        return None





    def setCurrent(self, option: str) -> bool:
        i = 0
        changed = False

        for _option in self.__options:
            if _option == option:
                self.__currentIndex = i
                self.__current = option
                changed = True
                break
            i += 1

        return changed





    def setCurrentIndex(self, index: int):
        if index > -1 and index < self.__optionsLen:
            self.__currentIndex = index
            self.__current = self.__options[index]





    def addOption(self, option: str):
        self.__current = option
        self.__options.append(option)
        self.__optionsLen += 1





    def removeOption(self, option: str):
        self.__options.remove(option)
        self.__optionsLen -= 1




class OptionWidget(QWidget):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)

        self.ui = Ui_OptionWidget()
        self.ui.setupUi(self)

        self.__customSignal = _CustomSignal()
        self.changed = self.__customSignal.changed

        self.options = _Options()

        self.ui.prevBtn.setStyleSheet(ssLoad("option-left"))
        self.ui.nextBtn.setStyleSheet(ssLoad("option-right"))

        self.ui.prevBtn.clicked.connect(self.prev)
        self.ui.nextBtn.clicked.connect(self.next)


        self.show()

    @property





    def current(self):
        return self.options.current
    
    @property





    def defaultOption(self):
        return self.options.defaultOption





    def resetCurrentToDefault(self):
        self.options.setDefaultAsCurrent()
        self.updateText()
        self.changed.emit()





    def setOption(self, option: str):
        if self.options.setCurrent(option):
            self.ui.currentOptionLabel.setText(self.options.current)
            self.changed.emit()





    def updateText(self):
        if self.options.current:
            self.ui.currentOptionLabel.setText(self.options.current)





    def updateLayoutSpacing(self, default_ = 150):
        space = default_ - len(self.ui.optionLabel.text())

        if space > 0:
            self.ui.optionWidgetLayout.setSpacing(space)





    def next(self):
        if self.options.next():
            self.ui.currentOptionLabel.setText(self.options.current)
            self.changed.emit()





    def prev(self):
        if self.options.prev():
            self.ui.currentOptionLabel.setText(self.options.current)
            self.changed.emit()

        