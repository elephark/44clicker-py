from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QDialogButtonBox

from ui_prefdialog import Ui_PrefDialog


class PrefDialog(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.ui = Ui_PrefDialog()
		self.ui.setupUi(self)
		self.setWindowTitle("Preferences")

		self.ui.buttonBox.accepted.connect(self.savePrefs)
		self.ui.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults).clicked.connect(self.restoreDefaults)

	
	@Slot()
	def savePrefs(self):
		print("savePrefs()")
	
	@Slot()
	def restoreDefaults(self):
		print("restoreDefaults()")

