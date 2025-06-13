from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import*
from PyQt5.QtWebEngineWidgets import*

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #next is our navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        #create a back button
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)
        #create a forward button
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)
        #create reload
        reload_button = QAction('reload',self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)
        #create home button
        home_button = QAction('Home',self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

    #right now define our navigatehome
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        self.browser.urlChanged.connect(self.update_url)

    def update_url(self,q):
        self.url_bar.setText(q.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName("My own Browser")
window = MainWindow()
app.exec_()