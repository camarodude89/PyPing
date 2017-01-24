import sys
from ping import Ping
from PyQt5.QtWidgets import QApplication
from gui_interface import GUIInterface

def main():
    hostname = input("Enter a hostname or IP address to ping: ")
    pingStatus = Ping.ping(hostname)
    print(pingStatus)
    input("Press any key")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    gi = GUIInterface()
    sys.exit(app.exec_())
