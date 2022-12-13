# QMainWindow提供了主窗口的功能，能创建简单的状态栏、工具栏、菜单栏
# https://maicss.gitbook.io/pyqt-chinese-tutoral/pyqt5/cai-dan-he-gong-ju-lan

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        exitAct = QAction(QIcon('title.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar().showMessage('Ready') # 状态栏

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,500,300) # 设置主窗口位置、大小
        self.setWindowTitle('HFYTest') # 主窗口名字
        self.setWindowIcon(QIcon('title.png')) # 主窗口图片
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())