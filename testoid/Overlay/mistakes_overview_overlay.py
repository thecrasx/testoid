from PySide6.QtWidgets import QWidget
from testoid.Overlay.overlay import Overlay
from testoid.Overview.mistakes_overview import MistakesOverview




class MistakesOverviewOverlay(Overlay):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.mistakesOverview = MistakesOverview()
        self.setPadding(100, 30, 100, 30)
        self.addWidget(self.mistakesOverview)
        self.setOverlayOpacity(150)
        self.hide()