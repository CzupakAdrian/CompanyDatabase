from PyQt5 import QtWidgets

from orm_controllers.DbConnection import DbConnectionAlbertSarajevo
from ui.main_win import MainWindow
import sys

app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
ui = MainWindow(DbConnectionAlbertSarajevo())
ui.setupUi(main_window)
main_window.show()
sys.exit(app.exec_())
