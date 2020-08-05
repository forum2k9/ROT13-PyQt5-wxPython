import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic


class MyWindow(QMainWindow):
	"""docstring for MyWindow"""
	def __init__(self):
		super(MyWindow, self).__init__()
		uic.loadUi('rot13_gui.ui', self)

		# ----- Connect Widgets Start ----
		# self.NAME-OF-WIDGET.clicked.connect(self.FUNCTION-TO-EXECUTE)
		self.rot13_Button.clicked.connect(self.generate_rot13_func)
		self.in_textEdit.textChanged.connect(self.generate_rot13_func)

		# ----- Connect Widgets End ----

		self.show()
		

	def generate_rot13_func(self):
		print('generate_rot13_func CLICKED')



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())





