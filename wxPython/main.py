import wx
from gui import MyWindow_1

from random import choice


class MyWindow_2(MyWindow_1):
	def __init__(self, parent):
		MyWindow_1.__init__ (self, parent)
		
	def generate_rot13_func(self, event):
		# print('generate_rot13_func...')
		raw_text = self.inText.GetValue()
		self.outText.SetValue(raw_text)





	def copy_func(self, event):
		print('copy_func...')

		self.outText.Copy()





app = wx.App(0)
MyWindow_2(None).Show()
app.MainLoop()



# app = wx.App(False)
# frame = MyWindow_2(None)
# frame.Show()
# app.MainLoop()



