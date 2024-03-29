# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Personal_Project\Osu-Collection-Formatter\GUI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 882)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.song_list = QtWidgets.QListWidget(self.centralwidget)
        self.song_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.song_list.setObjectName("song_list")
        self.gridLayout.addWidget(self.song_list, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 3, 1)
        self.debug = QtWidgets.QTextBrowser(self.centralwidget)
        self.debug.setObjectName("debug")
        self.gridLayout_2.addWidget(self.debug, 1, 0, 2, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.songNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.songNameLabel.setObjectName("songNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.songNameLabel)
        self.songNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.songNameLineEdit.setEnabled(False)
        self.songNameLineEdit.setObjectName("songNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.songNameLineEdit)
        self.songNameRomanisedLabel = QtWidgets.QLabel(self.centralwidget)
        self.songNameRomanisedLabel.setObjectName("songNameRomanisedLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.songNameRomanisedLabel)
        self.songNameRomanisedLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.songNameRomanisedLineEdit.setEnabled(False)
        self.songNameRomanisedLineEdit.setObjectName("songNameRomanisedLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.songNameRomanisedLineEdit)
        self.artistLabel = QtWidgets.QLabel(self.centralwidget)
        self.artistLabel.setObjectName("artistLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.artistLabel)
        self.artistLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.artistLineEdit.setEnabled(False)
        self.artistLineEdit.setObjectName("artistLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.artistLineEdit)
        self.artistRomanisedLabel = QtWidgets.QLabel(self.centralwidget)
        self.artistRomanisedLabel.setObjectName("artistRomanisedLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.artistRomanisedLabel)
        self.artistRomanisedLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.artistRomanisedLineEdit.setEnabled(False)
        self.artistRomanisedLineEdit.setObjectName("artistRomanisedLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.artistRomanisedLineEdit)
        self.difficultynameLabel = QtWidgets.QLabel(self.centralwidget)
        self.difficultynameLabel.setObjectName("difficultynameLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.difficultynameLabel)
        self.difficultynameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.difficultynameLineEdit.setEnabled(False)
        self.difficultynameLineEdit.setObjectName("difficultynameLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.difficultynameLineEdit)
        self.levelLabel = QtWidgets.QLabel(self.centralwidget)
        self.levelLabel.setObjectName("levelLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.levelLabel)
        self.levelLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.levelLineEdit.setEnabled(False)
        self.levelLineEdit.setObjectName("levelLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.levelLineEdit)
        self.mapperLabel = QtWidgets.QLabel(self.centralwidget)
        self.mapperLabel.setObjectName("mapperLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.mapperLabel)
        self.mapperLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mapperLineEdit.setEnabled(False)
        self.mapperLineEdit.setObjectName("mapperLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.mapperLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.select_chart = QtWidgets.QPushButton(self.centralwidget)
        self.select_chart.setObjectName("select_chart")
        self.verticalLayout.addWidget(self.select_chart)
        self.selectFolder = QtWidgets.QPushButton(self.centralwidget)
        self.selectFolder.setObjectName("selectFolder")
        self.verticalLayout.addWidget(self.selectFolder)
        self.delete_chart = QtWidgets.QPushButton(self.centralwidget)
        self.delete_chart.setObjectName("delete_chart")
        self.verticalLayout.addWidget(self.delete_chart)
        self.clearLog = QtWidgets.QPushButton(self.centralwidget)
        self.clearLog.setObjectName("clearLog")
        self.verticalLayout.addWidget(self.clearLog)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.optionsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.optionsGroupBox.setObjectName("optionsGroupBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.optionsGroupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 521, 101))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.packNameLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.packNameLabel.setObjectName("packNameLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.packNameLabel)
        self.packNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.packNameLineEdit.setObjectName("packNameLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.packNameLineEdit)
        self.packAuthorLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.packAuthorLabel.setObjectName("packAuthorLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.packAuthorLabel)
        self.packAuthorLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.packAuthorLineEdit.setObjectName("packAuthorLineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.packAuthorLineEdit)
        self.namingRuleLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.namingRuleLabel.setObjectName("namingRuleLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.namingRuleLabel)
        self.namingRuleComboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.namingRuleComboBox.setObjectName("namingRuleComboBox")
        self.namingRuleComboBox.addItem("")
        self.namingRuleComboBox.addItem("")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.namingRuleComboBox)
        self.packArtistLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.packArtistLabel.setObjectName("packArtistLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.packArtistLabel)
        self.packArtistLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.packArtistLineEdit.setInputMask("")
        self.packArtistLineEdit.setObjectName("packArtistLineEdit")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.packArtistLineEdit)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.optionsGroupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 130, 521, 33))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.useOriginalLanguageInVersionNameCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.useOriginalLanguageInVersionNameCheckBox.setObjectName("useOriginalLanguageInVersionNameCheckBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.useOriginalLanguageInVersionNameCheckBox)
        self.useOriginalLanguageInVersionNameLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.useOriginalLanguageInVersionNameLabel.setObjectName("useOriginalLanguageInVersionNameLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.useOriginalLanguageInVersionNameLabel)
        self.generateButton = QtWidgets.QPushButton(self.optionsGroupBox)
        self.generateButton.setEnabled(False)
        self.generateButton.setGeometry(QtCore.QRect(10, 280, 101, 23))
        self.generateButton.setObjectName("generateButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.optionsGroupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 170, 401, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.previewLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.previewLabel.setObjectName("previewLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.previewLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.lineEdit)
        self.gridLayout_3.addWidget(self.optionsGroupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 2, 1, 1)
        self.progressField = QtWidgets.QTextBrowser(self.centralwidget)
        self.progressField.setObjectName("progressField")
        self.gridLayout_2.addWidget(self.progressField, 2, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 8)
        self.gridLayout_2.setColumnStretch(2, 8)
        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 4)
        self.gridLayout_2.setRowStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.select_chart.clicked.connect(MainWindow.browse_beatmaps)
        self.song_list.itemClicked['QListWidgetItem*'].connect(MainWindow.display_info)
        self.delete_chart.clicked.connect(MainWindow.remove_chart)
        self.clearLog.clicked.connect(self.debug.clear)
        self.packNameLineEdit.textEdited['QString'].connect(MainWindow.toggle_generate)
        self.packAuthorLineEdit.textEdited['QString'].connect(MainWindow.toggle_generate)
        self.generateButton.clicked.connect(MainWindow.format_pack)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Osu! Collection Formatter v2.0 (Powered by WS)"))
        self.songNameLabel.setText(_translate("MainWindow", "Song Name"))
        self.songNameRomanisedLabel.setText(_translate("MainWindow", "Song Name(Romanised)"))
        self.artistLabel.setText(_translate("MainWindow", "Artist"))
        self.artistRomanisedLabel.setText(_translate("MainWindow", "Artist(Romanised)"))
        self.difficultynameLabel.setText(_translate("MainWindow", "Difficulty Name"))
        self.levelLabel.setText(_translate("MainWindow", "Level"))
        self.mapperLabel.setText(_translate("MainWindow", "Mapper"))
        self.select_chart.setText(_translate("MainWindow", "Select Chart(s)"))
        self.selectFolder.setText(_translate("MainWindow", "Select Folder(s)"))
        self.delete_chart.setText(_translate("MainWindow", "Delete Chart(s)"))
        self.clearLog.setText(_translate("MainWindow", "Clear Logs"))
        self.optionsGroupBox.setTitle(_translate("MainWindow", "Options"))
        self.packNameLabel.setText(_translate("MainWindow", "Pack Name"))
        self.packAuthorLabel.setText(_translate("MainWindow", "Pack Author"))
        self.namingRuleLabel.setText(_translate("MainWindow", "Naming Rule"))
        self.namingRuleComboBox.setItemText(0, _translate("MainWindow", "Level"))
        self.namingRuleComboBox.setItemText(1, _translate("MainWindow", "Difficulty Name"))
        self.packArtistLabel.setText(_translate("MainWindow", "Pack Artist"))
        self.packArtistLineEdit.setPlaceholderText(_translate("MainWindow", "Default: Various Artists"))
        self.useOriginalLanguageInVersionNameLabel.setText(_translate("MainWindow", "Use Original Language in Version Name"))
        self.generateButton.setText(_translate("MainWindow", "Generate Pack"))
        self.previewLabel.setText(_translate("MainWindow", "Naming Preview"))
