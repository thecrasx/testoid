from testoid.MainWindow.main_window import MainWindow
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())