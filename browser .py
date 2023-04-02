import sys
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QToolBar
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QPushButton
from PySide2.QtWebEngineWidgets import QWebEngineView

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sadman Web Browser")
        self.setGeometry(400, 200, 1200, 800)

        self.webView = QWebEngineView(self)
        self.webView.load(QUrl("http://google.com"))
        self.setCentralWidget(self.webView)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.urlBar = QLineEdit()
        self.urlBar.setFixedHeight(36)
        self.urlBar.returnPressed.connect(self.navigate)
        toolbar.addWidget(self.urlBar)

        backButton = QPushButton("◄", self)
        backButton.setStyleSheet("font-size: 24px; font-weight: bold;")
        backButton.clicked.connect(self.webView.back)
        toolbar.addWidget(backButton)

        forwardButton = QPushButton("►", self)
        forwardButton.setStyleSheet("font-size: 24px; font-weight: bold;")
        forwardButton.clicked.connect(self.webView.forward)
        toolbar.addWidget(forwardButton)

        refreshButton = QPushButton("⟳", self)
        refreshButton.setStyleSheet("font-size: 24px; font-weight: bold;")
        refreshButton.clicked.connect(self.webView.reload)
        toolbar.addWidget(refreshButton)

        stopButton = QPushButton("X", self)
        stopButton.setStyleSheet("font-size: 24px; font-weight: bold;")
        stopButton.clicked.connect(self.webView.stop)
        toolbar.addWidget(stopButton)

    def navigate(self):
        url = self.urlBar.text()

        if not url.startswith("http"):
            url = "http://" + url

        self.webView.load(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
