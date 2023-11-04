from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QDialogButtonBox

from ui_prefdialog import Ui_PrefDialog
from clickprefs import ClickPrefs, DEFAULTS


class PrefDialog(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.ui = Ui_PrefDialog()
		self.ui.setupUi(self)
		self.setWindowTitle("Preferences")

		self.ui.buttonBox.accepted.connect(self.savePrefs)
		self.ui.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(self.restoreDefaults)

		# We need some prefs. If this fails, we have issues.
		self.prefs:ClickPrefs = parent.prefs

		# Populate the values in the widgets.
		self.ui.md1SpinBox.setValue(self.prefs.MDWeight(1))
		self.ui.md2SpinBox.setValue(self.prefs.MDWeight(2))
		self.ui.md3SpinBox.setValue(self.prefs.MDWeight(3))
		self.ui.multiClickSpinBox.setValue(self.prefs.multiClickWeight())
		self.ui.timerDigitsSpinBox.setValue(self.prefs.timerDigits())

		# If you want to do a >10min freestyle...tough.
		self.ui.totalTimeSpinBox.setMaximum(600)
		# If you want do do a <1sec freestyle...tough.
		self.ui.totalTimeSpinBox.setMinimum(1)
		# If you want to do a freestyle with a non-integer length in seconds...tough.
		self.ui.totalTimeSpinBox.setValue(self.prefs.totalTimeSetting() / 1000)

		# Restrict timer digits to sane values.
		self.ui.timerDigitsSpinBox.setRange(0, 2)

	
	@Slot()
	def savePrefs(self):
		"""
		Copy the dialog contents back and save them, once we're done making changes.
		"""
		self.prefs.setMDWeight(1, self.ui.md1SpinBox.value())
		self.prefs.setMDWeight(2, self.ui.md2SpinBox.value())
		self.prefs.setMDWeight(3, self.ui.md3SpinBox.value())
		self.prefs.setMultiClickWeight(self.ui.multiClickSpinBox.value())
		self.prefs.setTotalTimeSetting(self.ui.totalTimeSpinBox.value() * 1000)
		self.prefs.setTimerDigits(self.ui.timerDigitsSpinBox.value())

		# Save them to disk. Flash. Whatever.
		self.prefs.writePrefs()
	
	@Slot()
	def restoreDefaults(self):
		"""
		Repopulate the fields with default values, which the user can then save or discard.
		"""
		self.ui.md1SpinBox.setValue(DEFAULTS["md1Weight"])
		self.ui.md2SpinBox.setValue(DEFAULTS["md2Weight"])
		self.ui.md3SpinBox.setValue(DEFAULTS["md3Weight"])
		self.ui.multiClickSpinBox.setValue(DEFAULTS["multiClickWeight"])
		self.ui.totalTimeSpinBox.setValue(DEFAULTS["fsLength"] / 1000)
		self.ui.timerDigitsSpinBox.setValue(DEFAULTS["timerDigits"])

