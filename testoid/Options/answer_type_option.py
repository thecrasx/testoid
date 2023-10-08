from testoid.Options.OptionWidget.option_widget import OptionWidget





class AnswerTypeOption(OptionWidget):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.ui.optionLabel.setText("Type")
        self.updateLayoutSpacing()

        self.options.addOption("Multiple Choice")
        self.options.addOption("Multiple Response")

        self.options.setDefaultOption("Multiple Choice")
        self.options.setCurrentIndex(0)
        self.updateText()



        self.show()





    
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = AnswerTypeOption()

    sys.exit(app.exec())