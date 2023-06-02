from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class mainWindow():
    def __init__(self):

        # CREATING THE GUI
        self.window = QWidget()
        # SETTING THE TITLE
        self.window.setWindowTitle("Bloom")
        self.window.setWindowIcon(QIcon("icon.png"))

        # CREATING THE LAYOUT
        self.layout = QVBoxLayout()
        # THE LAYOUT FOR THE BUTTONS AT THE TOP
        self.horizontal = QHBoxLayout()

        # CREATING THE URL BAR AND SETTING IT'S SIZE
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        # CREATING THE SEARCH BUTTON AND SETTING IT'S SIZE
        self.search_btn = QPushButton("Search")
        self.search_btn.setMinimumHeight(30)

        # CREATING THE BACK AND FORWARD BUTTONS AND SETTING THEIR SIZE
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forwards_btn = QPushButton(">")
        self.forwards_btn.setMinimumHeight(30)

        # ADDING THE ELEMENTS TO THE HORIZONTAL LAYOUT
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forwards_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.search_btn)

        # CREATING THE BROWSER ITSELF
        self.browser = QWebEngineView()

        # IMPLEMENTING THE FUNCTIONALITY OF THE BUTTONS
        self.back_btn.clicked.connect(self.browser.back)
        self.forwards_btn.clicked.connect(self.browser.forward)
        self.search_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))

        # ADDING THE HORIZONTAL LAYOUT AND THE BROWSER ITSELF
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        # SETTING THE BROWSER' STARTING PAGE
        self.browser.setUrl(QUrl("https://www.ecosia.org/"))

        # SETTING THE LAYOUT
        self.window.setLayout(self.layout)
        self.window.show()

    # MAKING SURE THE SEARCH BAR WORKS CORRECTLY
    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

# INITIALIZING THE APP
app = QApplication([])
window = mainWindow()
app.exec_()