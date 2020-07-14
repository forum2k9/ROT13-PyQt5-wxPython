# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 28 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyWindow_1
###########################################################################

class MyWindow_1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 513,407 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.inText = wx.TextCtrl( self, wx.ID_ANY, u"Enter text...", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.inText.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.inText.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer1.Add( self.inText, 1, wx.ALL|wx.EXPAND, 5 )

		self.rot13_btn = wx.Button( self, wx.ID_ANY, u"Generate Rot13", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.rot13_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.outText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.outText.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.outText, 1, wx.ALL|wx.EXPAND, 5 )

		self.copy_btn = wx.Button( self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.copy_btn, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.rot13_btn.Bind( wx.EVT_BUTTON, self.generate_rot13_func )
		self.outText.Bind( wx.EVT_TEXT, self.copy_func )
		self.copy_btn.Bind( wx.EVT_BUTTON, self.copy_func )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def generate_rot13_func( self, event ):
		event.Skip()

	def copy_func( self, event ):
		event.Skip()



