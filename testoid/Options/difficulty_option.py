from testoid.Options.OptionWidget.option_widget import OptionWidget





class DifficultyOption(OptionWidget):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.ui.optionLabel.setText("Difficulty")
        self.updateLayoutSpacing(140)

        self.options.addOption("Easy")
        self.options.addOption("Medium")
        self.options.addOption("Hard")

        self.options.setDefaultOption("Medium")
        self.options.setCurrent("Medium")
        self.updateText()



        self.show()





    
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    window = DifficultyOption()

    sys.exit(app.exec())