# from typing import Optional
from PySide6.QtCore import QObject, QSettings

DEFAULTS = {
	"md1Weight"       : 1,
	"md2Weight"       : 3,
	"md3Weight"       : 5,
	"multiClickWeight": 3,
	"fsLength"        : 120000,
	"dispRefresh"     : 47,
	"timerDigits"     : 2,
	"timerVisible"    : True,
}

class ClickPrefs(QObject):
	def __init__(self, parent = None):
		super().__init__(parent)
		qs = QSettings("Elephark", "44clicker")

		self.settings = {
			# "md1Weight"       : DEFAULTS["md1Weight"],
			# "md2Weight"       : DEFAULTS["md2Weight"],
			# "md3Weight"       : DEFAULTS["md3Weight"],
			# "multiClickWeight": DEFAULTS["multiClickWeight"],
			# "fsLength"        : DEFAULTS["fsLength"],
			# "dispRefresh"     : DEFAULTS["dispRefresh"],
			# "timerDigits"     : DEFAULTS["timerDigits"],
			# "timerVisible"    : DEFAULTS["timerVisible"],
		}

		self.settings["md1Weight"] = qs.value("md1weight", DEFAULTS["md1Weight"])
		self.settings["md2Weight"] = qs.value("md2weight", DEFAULTS["md2Weight"])
		self.settings["md3Weight"] = qs.value("md3weight", DEFAULTS["md3Weight"])
		self.settings["multiClickWeight"] = qs.value("multiClickWeight", DEFAULTS["multiClickWeight"])
		self.settings["fsLength"] = qs.value("fsLength", DEFAULTS["fsLength"])
		self.settings["dispRefresh"] = qs.value("dispRefresh", DEFAULTS["dispRefresh"])
		self.settings["timerDigits"] = qs.value("timerDigits", DEFAULTS["timerDigits"])
		self.settings["timerVisible"] = qs.value("timerVisible", DEFAULTS["timerVisible"])

	

	def multiClickWeight(self):
		return self.settings["multiClickWeight"]
	
	def totalTimeSetting(self):
		return self.settings["fsLength"]
	
	def timerDisplayRefresh(self):
		return self.settings["dispRefresh"]
	
	def timerDigits(self):
		return self.settings["timerDigits"]
	

	def setMultiClickWeight(self, weight:int):
		self.settings["multiClickWeight"] = weight

	def setTotalTimeSetting(self, totalTime:int):
		self.settings["fsLength"] = totalTime

	def setTimerDisplayRefresh(self, timeout:int):
		self.settings["dispRefresh"] = timeout
	
	def setTimerDigits(self, digits:int):
		self.settings["timerDigits"] = digits

	
	def writePrefs(self):
		qs = QSettings("Elephark", "44clicker")

		qs.setValue("md1Weight", self.settings["md1Weight"])
		qs.setValue("md2Weight", self.settings["md2Weight"])
		qs.setValue("md3Weight", self.settings["md3Weight"])
		qs.setValue("multiClickWeight", self.settings["multiClickWeight"])
		qs.setValue("fsLength", self.settings["fsLength"])
		qs.setValue("dispRefresh", self.settings["dispRefresh"])
		qs.setValue("timerDigits", self.settings["timerDigits"])
		qs.setValue("timerVisible", self.settings["timerVisible"])

	
	def MDWeight(self, level:int):
		if level == 1:
			return self.settings["md1Weight"]
		elif level == 2:
			return self.settings["md2Weight"]
		elif level == 3:
			return self.settings["md3Weight"]
		else:
			return 0
	
	def setMDWeight(self, level:int, weight:int):
		if level == 1:
			self.settings["md1Weight"] = weight
			return True
		elif level == 2:
			self.settings["md2Weight"] = weight
			return True
		elif level == 3:
			self.settings["md3Weight"] = weight
			return True
		else:
			return False
