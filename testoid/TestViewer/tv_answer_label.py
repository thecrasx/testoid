

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class _Signal(QObject):
    clicked = Signal(object)

class TVAnswerLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__selected = False

        font = QFont()
        font.setFamilies([u"FreeSans"])
        font.setPointSize(11)

        self.setFont(font)
        self.setWordWrap(True)
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.__signal = _Signal()
        self.clicked = self.__signal.clicked


    def mouseReleaseEvent(self, ev):
        if self.isSelected():         
            self.setSelected(False)
        
        else:        
            self.setSelected(True)


        self.clicked.emit(self)
    

    def isSelected(self) -> bool:
        return self.__selected


    def setSelected(self, isSelected):
        if isSelected:
            self.__selected = True

            self.setStyleSheet(u"QLabel {\n"
                                "   padding: 20px 10px 20px 10px;\n"
                                "	background: #715A83;\n"
                                "	color: rgba(255, 255, 255, 200);\n"
                                "   border-radius: 10px;\n"
                                "}")
            
        else:
            self.__selected = False

            self.setStyleSheet(u"QLabel {\n"
                                "   padding: 20px 10px 20px 10px;\n"
                                "	background: #9369B4;\n"
                                "	color: rgba(255, 255, 255, 200);\n"
                                "   border-radius: 10px;\n"
                                "}")
            
            
        

