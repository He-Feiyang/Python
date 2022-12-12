"""
---------------------------------------------------------------
 File Name: test0
 Author:    hefeiyang
 Date:      07/12/2022
 IDE:       PyCharm
---------------------------------------------------------------
 """
# https://maicss.gitbook.io/pyqt-chinese-tutoral/pyqt5/hello_world#li-5-xiao-xi-he-zi

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

from MainWindow import Ui_MainWindow

class Example(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):

        #按键
        QToolTip.setFont( QFont('SansSerif', 10) ) #设置提示框字体
        btn = QPushButton('Quit', self) 
        btn.clicked.connect(QCoreApplication.instance().quit) # instance()创建了一个QCoreApplication的实例，btn和quit函数绑定在一起
        btn.setToolTip('This is a <b>QPushButton</b> widget') # setToolTip()可以使用富文本，加粗
        btn.resize(btn.sizeHint()) # sizeHint()提供默认的按钮大小
        btn.move(200, 60) # 设置button在窗口的位置

        # 主窗口
        self.setGeometry(300,300,300,100) # 主窗口位置、大小
        self.setWindowTitle('hfyTest') #主窗口名字
        self.setWindowIcon(QIcon('title.png')) #主窗口图片
        
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Warning', 'Are you sure to quit?', 
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No) # yes和no表示消息框的俩按钮，最后一个参数是默认高亮的是哪个按钮

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def center(self):
        qr = self.frameGeometry()
        



if __name__ == '__main__':
    # application 对象
    app = QApplication(sys.argv)

    window = Example()

    sys.exit(app.exec_())
