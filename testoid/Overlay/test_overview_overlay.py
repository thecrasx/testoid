from PySide6.QtWidgets import QWidget
from testoid.Overlay.overlay import Overlay
from testoid.Overview.test_overview import TestOverview




class TestOverviewOverlay(Overlay):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.testOverview = TestOverview()
        self.setPadding(75, 25, 75, 25)
        self.addWidget(self.testOverview)
        self.setOverlayOpacity(175)
        self.hide()