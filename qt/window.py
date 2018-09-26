import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 420)
        self.setWindowTitle('我的窗口')

        # 向窗口添加控件
        # 添加一个按钮
        button = QPushButton("取消", self)
        button.setGeometry(250, 380, 45, 35)

        # 设置“这是什么”
        # setToolTip()，设置控件的提示信息，可以使用副文本内容
        button.setToolTip('这是一个<u>取消</u>按钮，按下将<b>退出</b>')

        # 设置窗体屏幕居中
        # 获取屏幕的分辨率
        screen = QDesktopWidget().screenGeometry()
        #获取窗体大小
        wall = self.geometry()

        self.move((screen.width()-wall.width())/2,(screen.height()-wall.height())/2)

        self.show()

    #消息提示机制(关闭)
    def closeEvent(self,event):
        #获取消息提示框
        reply = QMessageBox().question(self,'message','你是否确定退出',QMessageBox.Yes,QMessageBox.No)
        #判断选择的按钮
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


#将.UI文件转换成.py文件工具安装
#sudo apt install pyqt4-dev-tools
#转换命令
#pyuic demo.ui -o demo.py:将demo.ui文件转换成demo.py