# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, Slot
from PySide6.QtGui import QKeyEvent

from PySide6.QtCore import QTime, QTimer, Qt
from PySide6.QtWidgets import QLCDNumber, QPushButton, QLabel
from dataclasses import dataclass

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
		# self.ui = self.load_ui()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.setWindowTitle("44clicker")


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

		self.curClicks = ClickScore()
		self.lastClicks = ClickScore()

		self.displayClicks()

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
		return
	
	@Slot()
	def showPrefDialog(self):
		return


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
		return
	
	def displayClicks(self):
		self.ui.plusClicksLcd.display(self.curClicks.plusClicks)
		self.ui.minusClicksLcd.display(self.curClicks.minusClicks)
		self.ui.totalClicksLcd.display(self.curClicks.plusClicks + 
			self.curClicks.minusClicks)
	
	def resetClicks(self):
		return
	
	def timerStartPause(self, forceStop = False):
		return
	
	def timerReset(self):
		return
	


if __name__ == "__main__":
	app = QApplication()
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec())
