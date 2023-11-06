from PySide6.QtCore import QObject, QSettings
from dataclasses import dataclass


@dataclass
class ClickPrefsDefaults:
	"""
	Sane defaults for ClickPrefs.
	"""
	md1Weight:        int = 1
	md2Weight:        int = 3
	md3Weight:        int = 5
	multiClickWeight: int = 3
	fsLength:         int = 120000
	dispRefresh:      int = 47
	timerDigits:      int = 2
	timerVisible:     bool = True


class ClickPrefs(QObject):
	def __init__(self, parent = None):
		super().__init__(parent)

		qs = QSettings("Elephark", "44clicker")
		
		self.md1Weight = qs.value("md1Weight", ClickPrefsDefaults.md1Weight)
		self.md2Weight = qs.value("md2Weight", ClickPrefsDefaults.md2Weight)
		self.md3Weight = qs.value("md3Weight", ClickPrefsDefaults.md3Weight)
		self.multiClickWeight = qs.value("multiClickWeight", ClickPrefsDefaults.multiClickWeight)
		self.fsLength = qs.value("fsLength", ClickPrefsDefaults.fsLength)
		self.dispRefresh = qs.value("dispRefresh", ClickPrefsDefaults.dispRefresh)
		self.timerDigits = qs.value("timerDigits", ClickPrefsDefaults.timerDigits)
		self.timerVisible = qs.value("timerVisible", ClickPrefsDefaults.timerVisible)

	
	def writePrefs(self):
		"""
		Save settings to disk.
		"""
		qs = QSettings("Elephark", "44clicker")

		qs.setValue("md1Weight", self.md1Weight)
		qs.setValue("md2Weight", self.md2Weight)
		qs.setValue("md3Weight", self.md3Weight)
		qs.setValue("multiClickWeight", self.multiClickWeight)
		qs.setValue("fsLength", self.fsLength)
		qs.setValue("dispRefresh", self.dispRefresh)
		qs.setValue("timerDigits", self.timerDigits)
		qs.setValue("timerVisible", self.timerVisible)

	
	def MDWeight(self, level:int):
		if level == 1:
			return self.md1Weight
		elif level == 2:
			return self.md2Weight
		elif level == 3:
			return self.md3Weight
		else:
			return 0
	

	def setMDWeight(self, level:int, weight:int):
		if level == 1:
			self.md1Weight = weight
			return True
		elif level == 2:
			self.md2Weight = weight
			return True
		elif level == 3:
			self.md3Weight = weight
			return True
		else:
			return False
