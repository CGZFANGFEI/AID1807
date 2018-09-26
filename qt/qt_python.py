# 导入pyqt
from PyQt4 import QtGui
import sys


def main():
    app = QtGui.QApplication(sys.argv)  # 创建qt图形应用
    w = QtGui.QWidget()  # 创建图形窗口
    w.resize(800, 600)  # 设置窗口大小
    w.move(350, 350)  # 设置窗口的起始位置
    w.setWindowTitle('测试界面')  # 设置标题名称
    w.show()  # 显示窗口

    sys.exit(app.exec_())  # 关闭图形界面


if __name__ == '__main__':
    main()
