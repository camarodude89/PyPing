from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton,
QMainWindow, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, QCheckBox)
from PyQt5.QtGui import QIcon, QFont

class GUIInterface(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 440, 200)
        self.setWindowTitle('PyPingWOL')
        self.setWindowIcon(QIcon('web.png'))

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)

        #QToolTip.setFont(QFont('SansSerif', 10))

        #testBtn = QPushButton('Test', self)
        #testBtn.setToolTip('This tests the PC\'s network connection(s)')
        #testBtn.resize(testBtn.sizeHint())
        #testBtn.move(50, 50)

        #wOLBtn = QPushButton('Send WoL', self)
        #wOLBtn.setToolTip('Sends WoL packets to selected computers.')
        #wOLBtn.resize(wOLBtn.sizeHint())
        #wOLBtn.move(200, 50)


        self.setLayout(self.layout)

        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()
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
        self.tableWidget.setColumnWidth(0,20)
        self.tableWidget.move(0,0)
