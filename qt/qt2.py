from PyQt4 import QtGui
import sys


class Myqt(QtGui.QWidget):
    def __init__(self):
        super(Myqt, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('测试界面')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    myQt = Myqt()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
