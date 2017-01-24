from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton,
QMainWindow, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout,
QHBoxLayout, QCheckBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore

class GUIInterface(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 338, 200)
        self.setWindowTitle('PyPingWOL')
        self.setWindowIcon(QIcon('web.png'))

        self.createTable()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.tableWidget)

        QToolTip.setFont(QFont('SansSerif', 10))

        self.testBtn = QPushButton('Test', self)
        self.testBtn.setToolTip('This tests the PC\'s network connection(s)')
        self.testBtn.resize(self.testBtn.sizeHint())

        self.wOLBtn = QPushButton('Send WoL', self)
        self.wOLBtn.setToolTip('Sends WoL packets to selected computers.')
        self.wOLBtn.resize(self.wOLBtn.sizeHint())

        self.hBLayout = QHBoxLayout()
        self.hBLayout.addWidget(self.testBtn)
        self.hBLayout.addWidget(self.wOLBtn)

        self.mainLayout.addLayout(self.hBLayout)

        self.setLayout(self.mainLayout)

        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setRowCount(2)
        self.tableWidget.verticalHeaderVisible = False
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels([' ', 'Desc', 'PC Name',
        'Status'])

        checkBox = QCheckBox()
        checkBox.setChecked(True)

        self.tableWidget.setCellWidget(0,0, checkBox)
        self.tableWidget.setItem(0,1, QTableWidgetItem("Wet Side TV"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("MAR-BPHHR22-D"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Ok"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Bowles Breakroom TV"))
        self.tableWidget.setItem(1,2, QTableWidgetItem("MSM-2Q8X821"))
        self.tableWidget.setItem(1,3, QTableWidgetItem("Unreachable"))
        self.tableWidget.setColumnWidth(0,14)
        self.tableWidget.move(0,0)
