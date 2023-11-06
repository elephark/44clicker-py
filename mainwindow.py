# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, Slot
from PySide6.QtGui import QKeyEvent, QPalette, QColor

from PySide6.QtCore import QTime, QTimer, Qt
from PySide6.QtWidgets import QLCDNumber, QPushButton, QLabel, QDialog
from dataclasses import dataclass

from prefdialog import PrefDialog
from clickprefs import ClickPrefs
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

		# We need some preferences.
		self.prefs = ClickPrefs()

		# We need a UI.
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

		# Initialize timers. For fsTimer we strive for millisecond accuracy.
		self.fsTimer = QTimer()
		self.fsTimer.setTimerType(Qt.TimerType.PreciseTimer)
		self.fsTimer.setSingleShot(True)
		self.fsTimer.setInterval(self.prefs.totalTimeSetting())
		self.fsTimer.timeout.connect(self.timerFinished)
		self.timeRemaining = self.prefs.totalTimeSetting()

		# We're less concerned about dispRefreshTimer's accuracy.
		# It doesn't really matter.
		self.dispRefreshTimer = QTimer()
		self.dispRefreshTimer.timeout.connect(self.timerRedraw)

		self.timerRedraw()


	# "slots:"
	
	@Slot()
	def timerFinished(self):
		self.timerStartPause(True)
	
	@Slot()
	def timerRedraw(self):
		# Cache the remaining time.
		if self.fsTimer.isActive() == True:
			self.timeRemaining = self.fsTimer.remainingTime()

		# Center the digits, in the way a QLCDNumber understands.
		# self.ui.timeElapsedLcd.setDigitCount()
		# loool

		# Figure out how much time is left.
		timeElapsed = self.prefs.totalTimeSetting() - self.timeRemaining
		# Make things add up on screen.
		if self.prefs.timerDigits() == 1:
			timeElapsed += 99
		elif self.prefs.timerDigits() == 2:
			timeElapsed += 9

		# PARANOiA.mp3
		if timeElapsed < 0:
			timeElapsed = 0

		# Divide time remaining down to minutes, seconds, smaller units...
		# and push it out to the screen.
		mm:int = self.timeRemaining / (60 * 1000)
		# Seconds.
		ss:int = (((self.timeRemaining % (60 * 1000)) + 
			(0 if (self.prefs.timerDigits() != 0) else 999)) / 1000)
		# Oh, we also don't want 2:00 to display as 1:60 when the timer is running.
		# There might be a more elegant way to handle this.
		if ss == 60:
			ss = 0
			mm += 1
		
		cc:int = (self.timeRemaining % 1000) / 10
		if self.prefs.timerDigits() == 1:
			cc /= 10

		dispText = ""

		if self.prefs.timerDigits() == 2:
			dispText = "{0:0>2d}:{1:0>2d}.{2:0>2d}".format(int(mm), int(ss), int(cc))
		elif self.prefs.timerDigits() == 1:
			dispText = "{0:0>2d}:{1:0>2d}.{2:0>1d}".format(int(mm), int(ss), int(cc))
		else: # timerDigits == 0 or > 2
			dispText = "{0:0>2d}:{1:0>2d}".format(int(mm), int(ss))
		self.ui.timeRemainingLcd.display(dispText)

		# Do it again for time elapsed.
		mm = timeElapsed / (60 * 1000)
		ss = (timeElapsed % (60 * 1000)) / 1000
		cc = (timeElapsed % 1000) / 10
		if self.prefs.timerDigits() == 1:
			cc /= 10
		
		if self.prefs.timerDigits() == 2:
			dispText = "{0:0>2d}:{1:0>2d}.{2:0>2d}".format(int(mm), int(ss), int(cc))
		elif self.prefs.timerDigits() == 1:
			dispText = "{0:0>2d}:{1:0>2d}.{2:0>1d}".format(int(mm), int(ss), int(cc))
		else: # timerDigits == 0 or > 2
			dispText = "{0:0>2d}:{1:0>2d}".format(int(mm), int(ss))
		self.ui.timeElapsedLcd.display(dispText)


		# Turn the timers red when the time runs out.
		pal = QPalette()
		if self.timeRemaining == 0:
			pal.setColor(QPalette.ColorRole.Window, QColor(222, 22, 22))
			pal.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
		self.ui.timeRemainingLcd.setAutoFillBackground(True)
		self.ui.timeElapsedLcd.setAutoFillBackground(True)
		self.ui.timeRemainingLcd.setPalette(pal)
		self.ui.timeElapsedLcd.setPalette(pal)
		



	
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
		d = PrefDialog(self)
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
			self.plusClick(self.prefs.multiClickWeight())
		elif key == Qt.Key.Key_Z:
			# One minus click
			self.minusClick()
		elif key == Qt.Key.Key_X:
			# Three minus clicks
			self.minusClick(-1 * self.prefs.multiClickWeight())
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
			self.curClicks.majDeductLv1Clicks += self.prefs.MDWeight(1)
		elif level == 2:
			self.curClicks.majDeductLv2Clicks += self.prefs.MDWeight(2)
		elif level == 3:
			self.curClicks.majDeductLv3Clicks += self.prefs.MDWeight(3)

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
		# If the timer is already running, pause it.
		if self.fsTimer.isActive() == True or forceStop == True:
			# Cache the remaining time and stop the fs timer.
			self.timeRemaining = self.fsTimer.remainingTime()
			self.fsTimer.stop()

			# Hold bounds.
			if self.timeRemaining < 0:
				self.timeRemaining = 0

			# Stop the refresh timer.
			self.dispRefreshTimer.stop()

			# One last redraw of the timer values.
			self.timerRedraw()
			return False
		# If the timer isn't running, start it.
		else:
			# Automatically restart if the timer has expired.
			if self.timeRemaining == 0:
				self.timeRemaining = self.prefs.totalTimeSetting()
			
			# Load the countdown timer with the total remaining time and kick it off.
			self.fsTimer.start(self.timeRemaining)

			# Kick off the refresh timer, which will cause a redraw very soon.
			self.dispRefreshTimer.start(self.prefs.timerDisplayRefresh())

			return True
	
	def timerReset(self):
		# Stop everything.
		self.fsTimer.stop()
		self.dispRefreshTimer.stop()

		# Reload things afresh.
		self.timeRemaining = self.prefs.totalTimeSetting()

		# Redraw timer values.
		self.timerRedraw()
	


if __name__ == "__main__":
	app = QApplication()
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec())
