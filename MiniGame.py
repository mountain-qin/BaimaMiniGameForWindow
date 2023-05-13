#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import wx


import Translater
if not Translater.init(): _=lambda x:x


app_name="MiniGame"
app_label=_("Baima Mini game")
version_name="1.0"


class MiniGame(wx.Frame):
	def __init__(self,parent=None, id=-1, title=app_label, *args, **kw):
		super().__init__(parent, id, title,*args, **kw)

		self.main_dir_path=os.path.dirname(os.path.abspath(sys.argv[0]))

		self.index=-1
		self.games=[{"name": _("Baima Puzzle"), "path": "Puzzle\\Puzzle.exe"}]

		# if len(self.games)==1:
			# os.startfile(os.path.realpath(self.games[0]["path"]))
			# sys.exit()

		panel=wx.Panel(self,-1)
		l=[""]
		self.lb=wx.ListBox(panel,-1,choices=l, style=wx.LB_SINGLE)
		self.lb.SetSize((300, 200))
		self.show_message(_("Please press the up or down arrow to select a game, and press Enter to confirm"))
		self.lb.SetSelection(0)
		self.lb.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
		self.Show(True)
		return None

	def on_char_hook(self, event:wx.KeyEvent):
		key_code=event.GetKeyCode()
		if key_code==wx.WXK_UP:
			self.index-=1
			if self.index<0: self.index=0
			self.show_message(self.games[self.index]["name"])

		elif key_code==wx.WXK_DOWN:
			self.index+=1
			if self.index>len(self.games)-1: self.index=len(self.games)-1
			self.show_message(self.games[self.index]["name"])

		elif key_code==wx.WXK_RETURN:
			if self.index<0:return
			game_path=os.path.join(self.main_dir_path, self.games[self.index]["path"])
			if os.path.exists(game_path): os.startfile(game_path)
			sys.exit()

		event.Skip()

	def show_message(self, message):
		# 让屏幕阅读器可以朗读。
		self.lb.SetString(0, message)
		return None

try:
	app=wx.App(False)
	MiniGame()
	app.MainLoop()
except:
		pass