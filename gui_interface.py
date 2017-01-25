from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton,
QMainWindow, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout,
QHBoxLayout, QCheckBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from ping import Ping

class GUIInterface(QWidget):

    remoteMachines = [["Wet Side TV", "MAR-BPHHR22-D"],
        ["Bowles Breakroom TV", "MSM-2Q8X821"]]

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 338, 200)
        self.setWindowTitle('PyPing')
        self.setWindowIcon(QIcon('web.png'))

        self.createTable()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.tW)

        QToolTip.setFont(QFont('SansSerif', 10))

        self.testBtn = QPushButton('Test', self)
        self.testBtn.setToolTip('This tests the PC\'s network connection(s)')
        self.testBtn.resize(self.testBtn.sizeHint())
        self.testBtn.clicked.connect(self.checkStatus)

        self.hBLayout = QHBoxLayout()
        self.hBLayout.addWidget(self.testBtn)

        self.mainLayout.addLayout(self.hBLayout)

        self.setLayout(self.mainLayout)

        self.show()

    def createTable(self):

        self.tW = QTableWidget()
        self.tW.verticalHeader().setVisible(False)
        self.tW.setRowCount(len(self.remoteMachines))
        self.tW.verticalHeaderVisible = False
        self.tW.setColumnCount(4)
        self.tW.setHorizontalHeaderLabels([' ', 'Desc', 'PC Name',
        'Status'])

        self.checkBoxList = []

        for row in range(len(self.remoteMachines)):

            col = 0
            self.checkBoxList.append(QCheckBox())
            self.checkBoxList[row].setChecked(True)

            self.tW.setCellWidget(row,col, self.checkBoxList[row])
            self.tW.setItem(row,col+1,
                QTableWidgetItem(self.remoteMachines[row][col]))
            self.tW.setItem(row,col+2,
                QTableWidgetItem(self.remoteMachines[row][col+1]))
            self.tW.setItem(row,col+3,
                QTableWidgetItem("Untested"))

        self.tW.setColumnWidth(0,14)

    def checkStatus(self):

        for row, box in enumerate(self.checkBoxList):

            if box.isChecked():

                result = Ping.ping(self.remoteMachines[row][1])
                self.tW.item(row,3).setText(result)
