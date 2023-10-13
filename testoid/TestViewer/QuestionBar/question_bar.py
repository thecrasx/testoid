from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6.QtGui
from PySide6.QtWidgets import *

from testoid.TestViewer.QuestionBar.question_bar_ui import Ui_QuestionBar
from testoid.TestViewer.QuestionBar.question_bar_button import QuestionBarButton

class _CustomSignal(QObject):
    clicked = Signal(int)



class QuestionBar(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.ui = Ui_QuestionBar()
        self.ui.setupUi(self)


        self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.scrollArea.verticalScrollBar().setDisabled(True)
        self.ui.scrollArea.horizontalScrollBar().setInvertedControls(False)
        self.ui.scrollArea.wheelEvent = self.__scrollAreaWheelEvent


        self.__customSignal = _CustomSignal()
        self.clicked = self.__customSignal.clicked

        self.__buttons: list[QuestionBarButton] = []
        self.__currentButton: QuestionBarButton = None
        self.__buttonCount: int = 0
        self.__emitSelected: bool = True
        self.__marks: list[int] = []

        # Hide button for testing designs
        self.ui.testBtn.hide()


        self.show()





    def __scrollAreaWheelEvent(self, event: QWheelEvent) -> None:
        pixel_delta = event.pixelDelta()
        angle_delta = event.angleDelta()

        scroll_event = QWheelEvent(
            event.position(),
            event.globalPosition(),
            QPoint(pixel_delta.y(), pixel_delta.x()),
            QPoint(angle_delta.y(), angle_delta.x()), 
            event.buttons(), 
            event.modifiers(),event.phase(),
            event.inverted(), event.source(),
        )

        QCoreApplication.sendEvent(self.ui.scrollArea.horizontalScrollBar(), scroll_event)





    def __onButtonSelect(self, button: QuestionBarButton):
        if self.__currentButton is not None:
            self.__currentButton.setSelected(False)

        self.__currentButton = button
        
        if self.__emitSelected:
            self.clicked.emit(button.ID)
        else:
            self.__emitSelected = True
        



    
    def addButton(self):
        button = QuestionBarButton(self.ui.buttonsFrame, self.__buttonCount + 1)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.buttonsFrameLayout.addWidget(button)

        button.setText(str(self.__buttonCount + 1))
        button.selected.connect(self.__onButtonSelect)

        self.__buttons.append(button)
        self.__buttonCount += 1




    def setBarSize(self, size: int):
        if size == self.__buttonCount:
            return

        elif size > self.__buttonCount:
            for i in range(self.__buttonCount, size):
                self.addButton()

        else:
            if size < 0:
                size == 0

            for i in range(size, self.__buttonCount):
                self.__buttons[i].selected.disconnect(self.__onButtonSelect)
                self.__buttons[i].close()

            if size == 0:
                self.__buttons = []
                self.__buttonCount = 0
            else:
                self.__buttons = self.__buttons[:size]
                self.__buttonCount = size


    def resetBar(self):
        self.setBarSize(0)

    
    def setSelected(self, button: int, emit: bool = True):
        if button < 1 and button > self.__buttonCount:
            return
        
        self.__buttons[button - 1].setSelected(True)

        self.__emitSelected = emit





    def markQuestion(self, question_id: int = None):
        if question_id is not None and question_id >= 0 and question_id <= self.__buttonCount:
            button = self.__buttons[question_id - 1]
        else:
            button = self.__currentButton

        button.mark()
        self.__marks.append(button.ID)





    
    def unmarkQuestion(self, question_id: int = None):
        if question_id is not None and question_id >= 0 and question_id <= self.__buttonCount:
            button = self.__buttons[question_id - 1]
        else:
            button = self.__currentButton

        button.unmark()
        self.__marks.remove(button.ID)





    def isQuestionMarked(self, question_id: int = None) -> bool:
        if question_id is not None and question_id >= 0 and question_id <= self.__buttonCount:
            return self.__buttons[question_id - 1].isMarked()
        else:
            return self.__currentButton.isMarked()

        


        
        











if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    window = QuestionBar()

    sys.exit(app.exec())