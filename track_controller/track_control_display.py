import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt

qt_creator_file = "TestUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType("Track-Controller/"+qt_creator_file)
TestingPLCWind = "TestingPLC.ui"
Ui_TestingWindow, QtBaseClass = uic.loadUiType("Track-Controller/"+TestingPLCWind)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.testWind = test_window()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.TestPLCButton.clicked.connect(self.OpenTest)
        self.UploadPLCButton.clicked.connect(self.openFileNameDialog)

    def OpenTest(self):
        if self.testWind.isVisible():
            self.testWind.hide()

        else:
            self.testWind.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.CurrentlyRunningLabel.setText("Currently Running: "+ fileName)
            self.PLCTextBrowser.setText("Test");
            #TODO: Save File Path As VAriable
            #TODO: Send File To Be Parsed as PLC
            #TODO: Put PLC info on text Browser 
    

class test_window (QtWidgets.QMainWindow, Ui_TestingWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.UploadNewPLCButton.clicked.connect(self.openFileNameDialog)


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.CurrentPLCLabel.setText("Currently Running: "+ fileName)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()