# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, Slot
from PySide6.QtGui import QKeyEvent

from PySide6.QtCore import QTime, QTimer, Qt
from PySide6.QtWidgets import QLCDNumber, QPushButton, QLabel, QDialog
from dataclasses import dataclass

from prefdialog import PrefDialog
from ui_mainwindow import Ui_MainWindow

@dataclass
class ClickScore:
	plusClicks:         int = 0
	minusClicks:        int = 0
	majDeductLv1Clicks: int = 0
	majDeductLv2Clicks: int = 0
	majDeductLv3Clicks: int = 0


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.setWindowTitle("44clicker")

		# Set up the exit strategy.
		self.ui.actionQuit.triggered.connect(self.close)

		# Set up the undo signal.
		self.ui.actionUndoReset.triggered.connect(self.undoReset)

		# Set up a way to get to the pref dialog.
		self.ui.actionPrefs.triggered.connect(self.showPrefDialog)

		# Get the clicks ready.
		self.curClicks = ClickScore()
		self.lastClicks = ClickScore()
		self.displayClicks()

		# Initialize timers
		self.fsTimer = QTimer(self)
		self.dispRefreshTimer = QTimer(self)
		# self.prefs = prefs I guess

		self.fsTimer.setTimerType(Qt.TimerType.PreciseTimer)
		self.fsTimer.setSingleShot(True)
		# self.fsTimer.setInterval(prefs.totalTimeSetting())
		self.fsTimer.timeout.connect(self.timerFinished)
		# self.timeRemaining = prefs.totalTimeSetting()
		self.dispRefreshTimer.timeout.connect(self.timerRedraw)

		self.timerRedraw()


	# "slots:"
	
	@Slot()
	def timerFinished(self):
		return
	
	@Slot()
	def timerRedraw(self):
		return
	
	@Slot()
	def undoReset(self):
		# Perform a single-level undo operation in case we reset accidentally.
		self.curClicks.plusClicks = self.lastClicks.plusClicks
		self.curClicks.minusClicks = self.lastClicks.minusClicks
		self.curClicks.majDeductLv1Clicks = self.lastClicks.majDeductLv1Clicks
		self.curClicks.majDeductLv2Clicks = self.lastClicks.majDeductLv2Clicks
		self.curClicks.majDeductLv3Clicks = self.lastClicks.majDeductLv3Clicks

		self.displayClicks()
	
	@Slot()
	def showPrefDialog(self):
		d = PrefDialog()
		if d.exec() == QDialog.DialogCode.Accepted:
			self.timerRedraw()


	# "private:"

	def keyPressEvent(self, event: QKeyEvent):
		# Attempt to defeat autorepeat. May or may not work consistently
		# with PySide6, but it seems to work in my initial testing.
		if event.isAutoRepeat() == True:
			return

		# Do the appropriate thing for each key.
		key = event.key()
		if key == Qt.Key.Key_R:
			# Reset the score
			self.resetClicks()
		elif key == Qt.Key.Key_Slash:
			# One plus click
			self.plusClick()
		elif key == Qt.Key.Key_Period:
			# Three plus clicks
			self.plusClick(3) # todo: use prefs.multiClickWeight()
		elif key == Qt.Key.Key_Z:
			# One minus click
			self.minusClick()
		elif key == Qt.Key.Key_X:
			# Three minus clicks
			self.minusClick(-3) # todo: use prefs.multiclickWeight()
		elif key == Qt.Key.Key_A:
			# Major deduct level 1 (restart)
			self.majorDeductClick(1)
		elif key == Qt.Key.Key_S:
			# Major deduct level 2 (switch)
			self.majorDeductClick(2)
		elif key == Qt.Key.Key_D:
			# Major deduct level 3 (detach)
			self.majorDeductClick(3)
		elif key == Qt.Key.Key_Q:
			# Start/pause the timer
			self.timerStartPause()
		elif key == Qt.Key.Key_W:
			# Reset the timer
			self.timerReset()
	
	def keyReleaseEvent(self, event: QKeyEvent):
		# todo?
		return

	def plusClick(self, qty:int = 1):
		self.curClicks.plusClicks += qty
		self.displayClicks()
	
	def minusClick(self, qty:int = -1):
		self.curClicks.minusClicks += qty
		self.displayClicks()
	
	def majorDeductClick(self, level:int):
		if level == 1:
			self.curClicks.majDeductLv1Clicks += 1 # todo: use prefs.mdWeight()
		elif level == 2:
			self.curClicks.majDeductLv2Clicks += 3 # see above
		elif level == 3:
			self.curClicks.majDeductLv3Clicks += 5 # see above

		self.displayClicks()
	

	def displayClicks(self):
		clicks = self.curClicks
		self.ui.plusClicksLcd.display(clicks.plusClicks)
		self.ui.minusClicksLcd.display(clicks.minusClicks)
		self.ui.totalClicksLcd.display(clicks.plusClicks + clicks.minusClicks)
		self.ui.majDeductLv1Lcd.display(clicks.majDeductLv1Clicks)
		self.ui.majDeductLv2Lcd.display(clicks.majDeductLv2Clicks)
		self.ui.majDeductLv3Lcd.display(clicks.majDeductLv3Clicks)
		self.ui.majDeductTotalLcd.display( \
			clicks.majDeductLv1Clicks +
			clicks.majDeductLv2Clicks +
			clicks.majDeductLv3Clicks)
		# Note that the majDeduct LCDs have two digits and will fail if you
		# try to give them a three-digit number. If someone actually shows up
		# and gets more than 99 major deducts in 3 minutes, though...
		# I wouldn't even be mad. That would be legitimately impressive.

	
	def resetClicks(self):
		# Make it so we can undo.
		# Note that this doesn't check if anything was actually changed.
		# If they start up, immediately reset, click some, and then undo,
		# everything will "undo" back to zero, which is kind of weird.
		# Further note that I don't much care what happens if someone
		# really wants to do that.
		self.ui.actionUndoReset.setEnabled(True)

		# Back up first
		self.lastClicks.plusClicks = self.curClicks.plusClicks
		self.lastClicks.minusClicks = self.curClicks.minusClicks
		self.lastClicks.majDeductLv1Clicks = self.curClicks.majDeductLv1Clicks
		self.lastClicks.majDeductLv2Clicks = self.curClicks.majDeductLv2Clicks
		self.lastClicks.majDeductLv3Clicks = self.curClicks.majDeductLv3Clicks

		# Do the reset part
		self.curClicks.plusClicks = 0
		self.curClicks.minusClicks = 0
		self.curClicks.majDeductLv1Clicks = 0
		self.curClicks.majDeductLv2Clicks = 0
		self.curClicks.majDeductLv3Clicks = 0

		self.displayClicks()
	
	def timerStartPause(self, forceStop = False):
		return
	
	def timerReset(self):
		return
	


if __name__ == "__main__":
	app = QApplication()
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec())
