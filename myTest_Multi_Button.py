import sys, json

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QListWidget, QVBoxLayout, QWidget, QToolBar, QMessageBox, QPushButton, QHBoxLayout

__module_name__ = "Qt6 JSON System Information"
__module_version__ = "1.0"
__module_about__ = "Learning Python, Qt6 and JSON, HTML, CSS <br> which includes Dictionaries, Lists Functions, File reading and layout controls"

with open("fulllist.json") as file:
    sys_info = json.load(file)
margin = "\n=-=-=-=-=-=-=-=-=\n"
print(f"Number of Elements: {len(sys_info)} {type(sys_info)} {margin}")

def remove(item):
    return item.split("#", 3)[-1]

def getSys(self, s, button):
    sys = sys_info[s]
    self.List1.clear()
    #self.List1.setText(f"{sys}")
    for key,value in sys.items():
        new_title = f"{remove(key)}"
        button.setText(new_title)
        newkey = sys.get(key)
        #print(f"{newkey}")
        for i in range(len(newkey)):
            dialog(self, newkey[i])

def dialog(self, item):
    for key,value in item.items():
        msg = f"{remove(key)} => {value}"
        self.List1.addItem(msg)

def show_about(self):
    msg = QMessageBox()
    msg.setWindowTitle("About")
    msg.setText(f"<p align='center'>Module Name: {__module_name__} Version: {__module_version__}<br>{__module_about__}</p>")
    retval = msg.exec()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(__module_name__)
        self.resize(640,480)

        widget = QWidget()
        self.setCentralWidget(widget)

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        about_action = QAction("About", self)
        about_action.triggered.connect(show_about)
        toolbar.addAction(about_action)

        self.List1 = QListWidget(self)
        self.List1.setFixedSize(300, 400)
        self.List1.setStyleSheet("QListWidget { color: black; background-color: white; }")
        layoutL = QVBoxLayout()

        for i in range(0, 12):
            button = QPushButton(f'Button {i}')
            button.setFixedSize(150, 40)
            button.clicked.connect(self.make_click_handler(i))
            layoutL.addWidget(button)

        layoutR = QVBoxLayout()
        layoutR.addWidget(self.List1)

        SysMain = QHBoxLayout()
        SysMain.addLayout(layoutL)
        SysMain.addLayout(layoutR)

        widget.setLayout(SysMain)

    def make_click_handler(self, number):
        def click_handler():
            button = self.sender()
            getSys(self, number, button)
        return click_handler

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

