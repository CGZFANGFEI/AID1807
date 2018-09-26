from PyQt4 import QtGui, QtCore


class Window(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('事件演示')

        # 设置布局
        vbox = QtGui.QVBoxLayout()
        # 向布局中添加组件
        # 添加一个LCD显示模块
        lcd = QtGui.QLCDNumber(self)
        lcd.setToolTip('显示数据')
        # 添加一个水平滑杆
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setToolTip('控制数据的变化')
        # 编写事件
        # 移动滑竿，变化的值在lcd上显示
        # 事件来源：滑竿sld
        # 事件对象：值发生变化　valuechanged
        # 事件目标：在lcd上显示值 display
        sld.valueChanged.connect(lcd.display)

        button = QtGui.QPushButton('关闭', self)
        button.setToolTip('关闭窗口')
        button.clicked.connect(self.close)

        # 将组件添加到布局
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        vbox.addWidget(button)
        # 最后的设置整体布局
        self.setLayout(vbox)

        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(
            self, '事件演示', '是否确定退出', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    # 添加键盘事件

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.close()


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
