import sys
from PyQt5.QtWidgets import QApplication
from gui import ChessApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ChessApp()
    ventana.show()
    sys.exit(app.exec_())
