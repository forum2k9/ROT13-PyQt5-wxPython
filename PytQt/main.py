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

		# ----- Connect Widgets Start (Connect Events in wxPython) ----
		# self.NAME-OF-WIDGET.clicked.connect(self.FUNCTION-TO-EXECUTE)
		self.rot13_Button.clicked.connect(self.generate_rot13_func)
		self.in_textEdit.textChanged.connect(self.generate_rot13_func)

		self.copy_Button.clicked.connect(self.copy_func)
		# ----- Connect Widgets End ----

		self.show()
		

	def generate_rot13_func(self):
		# print('generate_rot13_func CLICKED')

		raw_text = self.in_textEdit.toPlainText()

		# Using Python String method: maketrans() that returns a mapping table for translation usable for translate() method.
		rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
		rot13_result = raw_text.translate(rot13trans)

		self.out_textEdit.setPlainText(rot13_result)




	def copy_func(self, event):
		# print('copy_func...')

		# Copy to clipboard...
		self.out_textEdit.selectAll()
		self.out_textEdit.copy()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())




