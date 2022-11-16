# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\p214s\OneDrive\Documents\GitHub\Team_X_ECE_1140\CTC_App\Iteration3\CTC.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1156, 651)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1141, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.Schedule = QtWidgets.QWidget()
        self.Schedule.setEnabled(True)
        self.Schedule.setObjectName("Schedule")
        self.singleDispatch = QtWidgets.QGroupBox(self.Schedule)
        self.singleDispatch.setGeometry(QtCore.QRect(20, 100, 361, 371))
        self.singleDispatch.setObjectName("singleDispatch")
        self.chooseStationCombo = QtWidgets.QComboBox(self.singleDispatch)
        self.chooseStationCombo.setGeometry(QtCore.QRect(150, 34, 201, 31))
        self.chooseStationCombo.setObjectName("chooseStationCombo")
        self.stationsTable = QtWidgets.QTableWidget(self.singleDispatch)
        self.stationsTable.setGeometry(QtCore.QRect(10, 120, 341, 192))
        self.stationsTable.setObjectName("stationsTable")
        self.stationsTable.setColumnCount(1)
        self.stationsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.stationsTable.setHorizontalHeaderItem(0, item)
        self.chooseStationLabel = QtWidgets.QLabel(self.singleDispatch)
        self.chooseStationLabel.setGeometry(QtCore.QRect(20, 40, 121, 17))
        self.chooseStationLabel.setObjectName("chooseStationLabel")
        self.addDestinationButton = QtWidgets.QPushButton(self.singleDispatch)
        self.addDestinationButton.setGeometry(QtCore.QRect(10, 80, 341, 25))
        self.addDestinationButton.setObjectName("addDestinationButton")
        self.dispatchButton = QtWidgets.QPushButton(self.singleDispatch)
        self.dispatchButton.setGeometry(QtCore.QRect(10, 330, 341, 25))
        self.dispatchButton.setObjectName("dispatchButton")
        self.autoDispatch = QtWidgets.QGroupBox(self.Schedule)
        self.autoDispatch.setGeometry(QtCore.QRect(20, 490, 361, 91))
        self.autoDispatch.setObjectName("autoDispatch")
        self.openFile = QtWidgets.QPushButton(self.autoDispatch)
        self.openFile.setGeometry(QtCore.QRect(10, 40, 341, 31))
        self.openFile.setObjectName("openFile")
        self.redLineButton = QtWidgets.QPushButton(self.Schedule)
        self.redLineButton.setGeometry(QtCore.QRect(20, 30, 171, 31))
        self.redLineButton.setObjectName("redLineButton")
        self.greenLineButton = QtWidgets.QPushButton(self.Schedule)
        self.greenLineButton.setGeometry(QtCore.QRect(210, 30, 171, 31))
        self.greenLineButton.setObjectName("greenLineButton")
        self.throughputLabel = QtWidgets.QLabel(self.Schedule)
        self.throughputLabel.setGeometry(QtCore.QRect(500, 50, 91, 41))
        self.throughputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.throughputLabel.setObjectName("throughputLabel")
        self.throughPutValue = QtWidgets.QLabel(self.Schedule)
        self.throughPutValue.setGeometry(QtCore.QRect(610, 50, 91, 41))
        self.throughPutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.throughPutValue.setObjectName("throughPutValue")
        self.currentLineValue = QtWidgets.QLabel(self.Schedule)
        self.currentLineValue.setGeometry(QtCore.QRect(610, 10, 101, 41))
        self.currentLineValue.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLineValue.setObjectName("currentLineValue")
        self.currentLineLabel = QtWidgets.QLabel(self.Schedule)
        self.currentLineLabel.setGeometry(QtCore.QRect(500, 10, 91, 41))
        self.currentLineLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLineLabel.setObjectName("currentLineLabel")
        self.trainTableStacked = QtWidgets.QStackedWidget(self.Schedule)
        self.trainTableStacked.setGeometry(QtCore.QRect(810, 10, 311, 571))
        self.trainTableStacked.setObjectName("trainTableStacked")
        self.redTrainTableStacked = QtWidgets.QWidget()
        self.redTrainTableStacked.setObjectName("redTrainTableStacked")
        self.redTrainTable = QtWidgets.QTableWidget(self.redTrainTableStacked)
        self.redTrainTable.setGeometry(QtCore.QRect(0, 0, 311, 561))
        self.redTrainTable.setAutoFillBackground(False)
        self.redTrainTable.setObjectName("redTrainTable")
        self.redTrainTable.setColumnCount(3)
        self.redTrainTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.redTrainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.redTrainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.redTrainTable.setHorizontalHeaderItem(2, item)
        self.redTrainTable.horizontalHeader().setCascadingSectionResizes(False)
        self.trainTableStacked.addWidget(self.redTrainTableStacked)
        self.greenTrainTableStacked = QtWidgets.QWidget()
        self.greenTrainTableStacked.setObjectName("greenTrainTableStacked")
        self.greenTrainTable = QtWidgets.QTableWidget(self.greenTrainTableStacked)
        self.greenTrainTable.setGeometry(QtCore.QRect(0, 0, 311, 561))
        self.greenTrainTable.setAutoFillBackground(False)
        self.greenTrainTable.setObjectName("greenTrainTable")
        self.greenTrainTable.setColumnCount(3)
        self.greenTrainTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.greenTrainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.greenTrainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.greenTrainTable.setHorizontalHeaderItem(2, item)
        self.greenTrainTable.horizontalHeader().setCascadingSectionResizes(False)
        self.trainTableStacked.addWidget(self.greenTrainTableStacked)
        self.editDispatchStacked = QtWidgets.QStackedWidget(self.Schedule)
        self.editDispatchStacked.setGeometry(QtCore.QRect(410, 90, 391, 521))
        self.editDispatchStacked.setObjectName("editDispatchStacked")
        self.redEditStacked = QtWidgets.QWidget()
        self.redEditStacked.setObjectName("redEditStacked")
        self.redEditDispatch = QtWidgets.QGroupBox(self.redEditStacked)
        self.redEditDispatch.setGeometry(QtCore.QRect(10, 20, 361, 481))
        self.redEditDispatch.setObjectName("redEditDispatch")
        self.redAddButton = QtWidgets.QPushButton(self.redEditDispatch)
        self.redAddButton.setGeometry(QtCore.QRect(10, 130, 341, 25))
        self.redAddButton.setObjectName("redAddButton")
        self.redAddStationLabel = QtWidgets.QLabel(self.redEditDispatch)
        self.redAddStationLabel.setGeometry(QtCore.QRect(20, 90, 121, 17))
        self.redAddStationLabel.setObjectName("redAddStationLabel")
        self.redAddStation = QtWidgets.QComboBox(self.redEditDispatch)
        self.redAddStation.setGeometry(QtCore.QRect(150, 84, 201, 31))
        self.redAddStation.setObjectName("redAddStation")
        self.redRemoveButton = QtWidgets.QPushButton(self.redEditDispatch)
        self.redRemoveButton.setGeometry(QtCore.QRect(10, 226, 341, 25))
        self.redRemoveButton.setObjectName("redRemoveButton")
        self.redRemoveStationLabel = QtWidgets.QLabel(self.redEditDispatch)
        self.redRemoveStationLabel.setGeometry(QtCore.QRect(20, 186, 121, 17))
        self.redRemoveStationLabel.setObjectName("redRemoveStationLabel")
        self.redRemoveStation = QtWidgets.QComboBox(self.redEditDispatch)
        self.redRemoveStation.setGeometry(QtCore.QRect(150, 180, 201, 31))
        self.redRemoveStation.setObjectName("redRemoveStation")
        self.redEditDispatchTable = QtWidgets.QTableWidget(self.redEditDispatch)
        self.redEditDispatchTable.setGeometry(QtCore.QRect(10, 270, 341, 161))
        self.redEditDispatchTable.setObjectName("redEditDispatchTable")
        self.redEditDispatchTable.setColumnCount(1)
        self.redEditDispatchTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.redEditDispatchTable.setHorizontalHeaderItem(0, item)
        self.redChooseTrainLabel = QtWidgets.QLabel(self.redEditDispatch)
        self.redChooseTrainLabel.setGeometry(QtCore.QRect(20, 36, 121, 17))
        self.redChooseTrainLabel.setObjectName("redChooseTrainLabel")
        self.redChooseTrain = QtWidgets.QComboBox(self.redEditDispatch)
        self.redChooseTrain.setGeometry(QtCore.QRect(150, 30, 201, 31))
        self.redChooseTrain.setObjectName("redChooseTrain")
        self.redUpdateButton = QtWidgets.QPushButton(self.redEditDispatch)
        self.redUpdateButton.setGeometry(QtCore.QRect(10, 440, 341, 25))
        self.redUpdateButton.setObjectName("redUpdateButton")
        self.editDispatchStacked.addWidget(self.redEditStacked)
        self.greenEditStacked = QtWidgets.QWidget()
        self.greenEditStacked.setObjectName("greenEditStacked")
        self.greenEditDispatch = QtWidgets.QGroupBox(self.greenEditStacked)
        self.greenEditDispatch.setGeometry(QtCore.QRect(10, 20, 361, 481))
        self.greenEditDispatch.setObjectName("greenEditDispatch")
        self.greenAddButton = QtWidgets.QPushButton(self.greenEditDispatch)
        self.greenAddButton.setGeometry(QtCore.QRect(10, 130, 341, 25))
        self.greenAddButton.setObjectName("greenAddButton")
        self.greenAddStationLabel = QtWidgets.QLabel(self.greenEditDispatch)
        self.greenAddStationLabel.setGeometry(QtCore.QRect(20, 90, 121, 17))
        self.greenAddStationLabel.setObjectName("greenAddStationLabel")
        self.greenAddStation = QtWidgets.QComboBox(self.greenEditDispatch)
        self.greenAddStation.setGeometry(QtCore.QRect(150, 84, 201, 31))
        self.greenAddStation.setObjectName("greenAddStation")
        self.greenRemoveButton = QtWidgets.QPushButton(self.greenEditDispatch)
        self.greenRemoveButton.setGeometry(QtCore.QRect(10, 226, 341, 25))
        self.greenRemoveButton.setObjectName("greenRemoveButton")
        self.greenRemoveStationLabel = QtWidgets.QLabel(self.greenEditDispatch)
        self.greenRemoveStationLabel.setGeometry(QtCore.QRect(20, 186, 121, 17))
        self.greenRemoveStationLabel.setObjectName("greenRemoveStationLabel")
        self.greenRemoveStation = QtWidgets.QComboBox(self.greenEditDispatch)
        self.greenRemoveStation.setGeometry(QtCore.QRect(150, 180, 201, 31))
        self.greenRemoveStation.setObjectName("greenRemoveStation")
        self.greenEditDispatchTable = QtWidgets.QTableWidget(self.greenEditDispatch)
        self.greenEditDispatchTable.setGeometry(QtCore.QRect(10, 270, 341, 161))
        self.greenEditDispatchTable.setObjectName("greenEditDispatchTable")
        self.greenEditDispatchTable.setColumnCount(1)
        self.greenEditDispatchTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenEditDispatchTable.setHorizontalHeaderItem(0, item)
        self.greenChooseTrainLabel = QtWidgets.QLabel(self.greenEditDispatch)
        self.greenChooseTrainLabel.setGeometry(QtCore.QRect(20, 36, 121, 17))
        self.greenChooseTrainLabel.setObjectName("greenChooseTrainLabel")
        self.greenChooseTrain = QtWidgets.QComboBox(self.greenEditDispatch)
        self.greenChooseTrain.setGeometry(QtCore.QRect(150, 30, 201, 31))
        self.greenChooseTrain.setObjectName("greenChooseTrain")
        self.greenUpdateButton = QtWidgets.QPushButton(self.greenEditDispatch)
        self.greenUpdateButton.setGeometry(QtCore.QRect(10, 440, 341, 25))
        self.greenUpdateButton.setObjectName("greenUpdateButton")
        self.editDispatchStacked.addWidget(self.greenEditStacked)
        self.tabWidget.addTab(self.Schedule, "")
        self.Maintenance = QtWidgets.QWidget()
        self.Maintenance.setObjectName("Maintenance")
        self.greenLineButton_2 = QtWidgets.QPushButton(self.Maintenance)
        self.greenLineButton_2.setGeometry(QtCore.QRect(210, 30, 171, 31))
        self.greenLineButton_2.setObjectName("greenLineButton_2")
        self.redLineButton_2 = QtWidgets.QPushButton(self.Maintenance)
        self.redLineButton_2.setGeometry(QtCore.QRect(20, 30, 171, 31))
        self.redLineButton_2.setObjectName("redLineButton_2")
        self.maintenanceStack = QtWidgets.QStackedWidget(self.Maintenance)
        self.maintenanceStack.setGeometry(QtCore.QRect(20, 90, 1101, 501))
        self.maintenanceStack.setObjectName("maintenanceStack")
        self.redInfo = QtWidgets.QWidget()
        self.redInfo.setObjectName("redInfo")
        self.greenClosedBlocksGroup_2 = QtWidgets.QGroupBox(self.redInfo)
        self.greenClosedBlocksGroup_2.setGeometry(QtCore.QRect(20, 180, 331, 321))
        self.greenClosedBlocksGroup_2.setObjectName("greenClosedBlocksGroup_2")
        self.greenClosedBlocksTable_2 = QtWidgets.QTableWidget(self.greenClosedBlocksGroup_2)
        self.greenClosedBlocksTable_2.setGeometry(QtCore.QRect(10, 30, 311, 281))
        self.greenClosedBlocksTable_2.setObjectName("greenClosedBlocksTable_2")
        self.greenClosedBlocksTable_2.setColumnCount(1)
        self.greenClosedBlocksTable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenClosedBlocksTable_2.setHorizontalHeaderItem(0, item)
        self.greenSwitchStateGroup_2 = QtWidgets.QGroupBox(self.redInfo)
        self.greenSwitchStateGroup_2.setGeometry(QtCore.QRect(390, 230, 361, 271))
        self.greenSwitchStateGroup_2.setObjectName("greenSwitchStateGroup_2")
        self.greenSwitchStateTable_2 = QtWidgets.QTableWidget(self.greenSwitchStateGroup_2)
        self.greenSwitchStateTable_2.setGeometry(QtCore.QRect(10, 30, 341, 231))
        self.greenSwitchStateTable_2.setObjectName("greenSwitchStateTable_2")
        self.greenSwitchStateTable_2.setColumnCount(2)
        self.greenSwitchStateTable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenSwitchStateTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenSwitchStateTable_2.setHorizontalHeaderItem(1, item)
        self.greenChangeSwitchGroup_2 = QtWidgets.QGroupBox(self.redInfo)
        self.greenChangeSwitchGroup_2.setGeometry(QtCore.QRect(390, 10, 361, 201))
        self.greenChangeSwitchGroup_2.setObjectName("greenChangeSwitchGroup_2")
        self.greenChooseOriginCombo_2 = QtWidgets.QComboBox(self.greenChangeSwitchGroup_2)
        self.greenChooseOriginCombo_2.setGeometry(QtCore.QRect(190, 44, 151, 31))
        self.greenChooseOriginCombo_2.setObjectName("greenChooseOriginCombo_2")
        self.greenSetState_2 = QtWidgets.QPushButton(self.greenChangeSwitchGroup_2)
        self.greenSetState_2.setGeometry(QtCore.QRect(20, 150, 321, 25))
        self.greenSetState_2.setObjectName("greenSetState_2")
        self.label_4 = QtWidgets.QLabel(self.greenChangeSwitchGroup_2)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 151, 17))
        self.label_4.setObjectName("label_4")
        self.greenChooseTargetCombo_2 = QtWidgets.QComboBox(self.greenChangeSwitchGroup_2)
        self.greenChooseTargetCombo_2.setGeometry(QtCore.QRect(190, 90, 151, 31))
        self.greenChooseTargetCombo_2.setObjectName("greenChooseTargetCombo_2")
        self.label_5 = QtWidgets.QLabel(self.greenChangeSwitchGroup_2)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 151, 17))
        self.label_5.setObjectName("label_5")
        self.greenCrossingGroup_2 = QtWidgets.QGroupBox(self.redInfo)
        self.greenCrossingGroup_2.setGeometry(QtCore.QRect(790, 10, 291, 491))
        self.greenCrossingGroup_2.setObjectName("greenCrossingGroup_2")
        self.greenCrossingTable_2 = QtWidgets.QTableWidget(self.greenCrossingGroup_2)
        self.greenCrossingTable_2.setGeometry(QtCore.QRect(10, 30, 271, 451))
        self.greenCrossingTable_2.setObjectName("greenCrossingTable_2")
        self.greenCrossingTable_2.setColumnCount(2)
        self.greenCrossingTable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenCrossingTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenCrossingTable_2.setHorizontalHeaderItem(1, item)
        self.greenMaintenanceGroup_2 = QtWidgets.QGroupBox(self.redInfo)
        self.greenMaintenanceGroup_2.setGeometry(QtCore.QRect(20, 10, 331, 151))
        self.greenMaintenanceGroup_2.setObjectName("greenMaintenanceGroup_2")
        self.chooseMaintenanceCombo_2 = QtWidgets.QComboBox(self.greenMaintenanceGroup_2)
        self.chooseMaintenanceCombo_2.setGeometry(QtCore.QRect(170, 40, 141, 31))
        self.chooseMaintenanceCombo_2.setObjectName("chooseMaintenanceCombo_2")
        self.putMaintenanceButton_2 = QtWidgets.QPushButton(self.greenMaintenanceGroup_2)
        self.putMaintenanceButton_2.setGeometry(QtCore.QRect(18, 100, 291, 25))
        self.putMaintenanceButton_2.setObjectName("putMaintenanceButton_2")
        self.label_6 = QtWidgets.QLabel(self.greenMaintenanceGroup_2)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 111, 17))
        self.label_6.setObjectName("label_6")
        self.maintenanceStack.addWidget(self.redInfo)
        self.greenInfo = QtWidgets.QWidget()
        self.greenInfo.setObjectName("greenInfo")
        self.greenClosedBlocksGroup = QtWidgets.QGroupBox(self.greenInfo)
        self.greenClosedBlocksGroup.setGeometry(QtCore.QRect(20, 180, 331, 321))
        self.greenClosedBlocksGroup.setObjectName("greenClosedBlocksGroup")
        self.greenClosedBlocksTable = QtWidgets.QTableWidget(self.greenClosedBlocksGroup)
        self.greenClosedBlocksTable.setGeometry(QtCore.QRect(10, 30, 311, 281))
        self.greenClosedBlocksTable.setObjectName("greenClosedBlocksTable")
        self.greenClosedBlocksTable.setColumnCount(1)
        self.greenClosedBlocksTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenClosedBlocksTable.setHorizontalHeaderItem(0, item)
        self.greenMaintenanceGroup = QtWidgets.QGroupBox(self.greenInfo)
        self.greenMaintenanceGroup.setGeometry(QtCore.QRect(20, 10, 331, 151))
        self.greenMaintenanceGroup.setObjectName("greenMaintenanceGroup")
        self.greenChooseMaintenanceCombo = QtWidgets.QComboBox(self.greenMaintenanceGroup)
        self.greenChooseMaintenanceCombo.setGeometry(QtCore.QRect(170, 40, 141, 31))
        self.greenChooseMaintenanceCombo.setObjectName("greenChooseMaintenanceCombo")
        self.greenMaintenanceButton = QtWidgets.QPushButton(self.greenMaintenanceGroup)
        self.greenMaintenanceButton.setGeometry(QtCore.QRect(18, 100, 291, 25))
        self.greenMaintenanceButton.setObjectName("greenMaintenanceButton")
        self.greenChooseBlockLabel = QtWidgets.QLabel(self.greenMaintenanceGroup)
        self.greenChooseBlockLabel.setGeometry(QtCore.QRect(20, 50, 111, 17))
        self.greenChooseBlockLabel.setObjectName("greenChooseBlockLabel")
        self.greenChangeSwitchGroup = QtWidgets.QGroupBox(self.greenInfo)
        self.greenChangeSwitchGroup.setGeometry(QtCore.QRect(390, 10, 361, 201))
        self.greenChangeSwitchGroup.setObjectName("greenChangeSwitchGroup")
        self.greenChooseOriginCombo = QtWidgets.QComboBox(self.greenChangeSwitchGroup)
        self.greenChooseOriginCombo.setGeometry(QtCore.QRect(190, 44, 151, 31))
        self.greenChooseOriginCombo.setObjectName("greenChooseOriginCombo")
        self.greenSetState = QtWidgets.QPushButton(self.greenChangeSwitchGroup)
        self.greenSetState.setGeometry(QtCore.QRect(20, 150, 321, 25))
        self.greenSetState.setObjectName("greenSetState")
        self.label_2 = QtWidgets.QLabel(self.greenChangeSwitchGroup)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 17))
        self.label_2.setObjectName("label_2")
        self.greenChooseTargetCombo = QtWidgets.QComboBox(self.greenChangeSwitchGroup)
        self.greenChooseTargetCombo.setGeometry(QtCore.QRect(190, 90, 151, 31))
        self.greenChooseTargetCombo.setObjectName("greenChooseTargetCombo")
        self.label_3 = QtWidgets.QLabel(self.greenChangeSwitchGroup)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 151, 17))
        self.label_3.setObjectName("label_3")
        self.greenCrossingGroup = QtWidgets.QGroupBox(self.greenInfo)
        self.greenCrossingGroup.setGeometry(QtCore.QRect(790, 10, 291, 491))
        self.greenCrossingGroup.setObjectName("greenCrossingGroup")
        self.greenCrossingTable = QtWidgets.QTableWidget(self.greenCrossingGroup)
        self.greenCrossingTable.setGeometry(QtCore.QRect(10, 30, 271, 451))
        self.greenCrossingTable.setObjectName("greenCrossingTable")
        self.greenCrossingTable.setColumnCount(2)
        self.greenCrossingTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenCrossingTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenCrossingTable.setHorizontalHeaderItem(1, item)
        self.greenSwitchStateGroup = QtWidgets.QGroupBox(self.greenInfo)
        self.greenSwitchStateGroup.setGeometry(QtCore.QRect(390, 230, 361, 271))
        self.greenSwitchStateGroup.setObjectName("greenSwitchStateGroup")
        self.greenSwitchStateTable = QtWidgets.QTableWidget(self.greenSwitchStateGroup)
        self.greenSwitchStateTable.setGeometry(QtCore.QRect(10, 30, 341, 231))
        self.greenSwitchStateTable.setObjectName("greenSwitchStateTable")
        self.greenSwitchStateTable.setColumnCount(2)
        self.greenSwitchStateTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenSwitchStateTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.greenSwitchStateTable.setHorizontalHeaderItem(1, item)
        self.maintenanceStack.addWidget(self.greenInfo)
        self.manualModeCheck = QtWidgets.QCheckBox(self.Maintenance)
        self.manualModeCheck.setGeometry(QtCore.QRect(530, 60, 121, 23))
        self.manualModeCheck.setObjectName("manualModeCheck")
        self.currentLineLabel_2 = QtWidgets.QLabel(self.Maintenance)
        self.currentLineLabel_2.setGeometry(QtCore.QRect(500, 10, 91, 41))
        self.currentLineLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLineLabel_2.setObjectName("currentLineLabel_2")
        self.currentLineValue_2 = QtWidgets.QLabel(self.Maintenance)
        self.currentLineValue_2.setGeometry(QtCore.QRect(610, 10, 101, 41))
        self.currentLineValue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLineValue_2.setObjectName("currentLineValue_2")
        self.tabWidget.addTab(self.Maintenance, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.trainTableStacked.setCurrentIndex(0)
        self.editDispatchStacked.setCurrentIndex(1)
        self.maintenanceStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.singleDispatch.setTitle(_translate("Form", "Single Dispatch"))
        item = self.stationsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Stations"))
        self.chooseStationLabel.setText(_translate("Form", "Choose Stations:"))
        self.addDestinationButton.setText(_translate("Form", "Add"))
        self.dispatchButton.setText(_translate("Form", "Dispatch"))
        self.autoDispatch.setTitle(_translate("Form", "Automatic Dispatch"))
        self.openFile.setText(_translate("Form", "Open File"))
        self.redLineButton.setText(_translate("Form", "Red Line"))
        self.greenLineButton.setText(_translate("Form", "Green Line"))
        self.throughputLabel.setText(_translate("Form", "Throughput:"))
        self.throughPutValue.setText(_translate("Form", "--"))
        self.currentLineValue.setText(_translate("Form", "--"))
        self.currentLineLabel.setText(_translate("Form", "Current Line:"))
        item = self.redTrainTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Train ID"))
        item = self.redTrainTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Block"))
        item = self.redTrainTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Next Stop"))
        item = self.greenTrainTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Train ID"))
        item = self.greenTrainTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Block"))
        item = self.greenTrainTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Next Stop"))
        self.redEditDispatch.setTitle(_translate("Form", "Edit Dispatch"))
        self.redAddButton.setText(_translate("Form", "Add"))
        self.redAddStationLabel.setText(_translate("Form", "Add Stations:"))
        self.redRemoveButton.setText(_translate("Form", "Remove"))
        self.redRemoveStationLabel.setText(_translate("Form", "Remove Stations:"))
        item = self.redEditDispatchTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Stations"))
        self.redChooseTrainLabel.setText(_translate("Form", "Choose Train:"))
        self.redUpdateButton.setText(_translate("Form", "Update"))
        self.greenEditDispatch.setTitle(_translate("Form", "Edit Dispatch"))
        self.greenAddButton.setText(_translate("Form", "Add"))
        self.greenAddStationLabel.setText(_translate("Form", "Add Stations:"))
        self.greenRemoveButton.setText(_translate("Form", "Remove"))
        self.greenRemoveStationLabel.setText(_translate("Form", "Remove Stations:"))
        item = self.greenEditDispatchTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Stations"))
        self.greenChooseTrainLabel.setText(_translate("Form", "Choose Train:"))
        self.greenUpdateButton.setText(_translate("Form", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Schedule), _translate("Form", "Tab 1"))
        self.greenLineButton_2.setText(_translate("Form", "Green Line"))
        self.redLineButton_2.setText(_translate("Form", "Red Line"))
        self.greenClosedBlocksGroup_2.setTitle(_translate("Form", "Closed Blocks"))
        item = self.greenClosedBlocksTable_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Block Number"))
        self.greenSwitchStateGroup_2.setTitle(_translate("Form", "Switch State"))
        item = self.greenSwitchStateTable_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Origin Block"))
        item = self.greenSwitchStateTable_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Target Block"))
        self.greenChangeSwitchGroup_2.setTitle(_translate("Form", "Switch Position"))
        self.greenSetState_2.setText(_translate("Form", "Set"))
        self.label_4.setText(_translate("Form", "Choose Origin Block:"))
        self.label_5.setText(_translate("Form", "Choose Target Block:"))
        self.greenCrossingGroup_2.setTitle(_translate("Form", "Crossing Status"))
        item = self.greenCrossingTable_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Block Number"))
        item = self.greenCrossingTable_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Status"))
        self.greenMaintenanceGroup_2.setTitle(_translate("Form", "Block Maintenance"))
        self.putMaintenanceButton_2.setText(_translate("Form", "Put In Maintenace"))
        self.label_6.setText(_translate("Form", "Choose Block:"))
        self.greenClosedBlocksGroup.setTitle(_translate("Form", "Closed Blocks"))
        item = self.greenClosedBlocksTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Block Number"))
        self.greenMaintenanceGroup.setTitle(_translate("Form", "Block Maintenance"))
        self.greenMaintenanceButton.setText(_translate("Form", "Put In Maintenace"))
        self.greenChooseBlockLabel.setText(_translate("Form", "Choose Block:"))
        self.greenChangeSwitchGroup.setTitle(_translate("Form", "Switch Position"))
        self.greenSetState.setText(_translate("Form", "Set"))
        self.label_2.setText(_translate("Form", "Choose Origin Block:"))
        self.label_3.setText(_translate("Form", "Choose Target Block:"))
        self.greenCrossingGroup.setTitle(_translate("Form", "Crossing Status"))
        item = self.greenCrossingTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Block Number"))
        item = self.greenCrossingTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Status"))
        self.greenSwitchStateGroup.setTitle(_translate("Form", "Switch State"))
        item = self.greenSwitchStateTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Origin Block"))
        item = self.greenSwitchStateTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Target Block"))
        self.manualModeCheck.setText(_translate("Form", "Manual Mode"))
        self.currentLineLabel_2.setText(_translate("Form", "Current Line:"))
        self.currentLineValue_2.setText(_translate("Form", "--"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Maintenance), _translate("Form", "Tab 2"))