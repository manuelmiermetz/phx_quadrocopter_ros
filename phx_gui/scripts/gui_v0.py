# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_v0.ui'
#
# Created: Fri May 29 20:51:03 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1302, 623)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1276, 571))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gui_output = QtGui.QVBoxLayout()
        self.gui_output.setObjectName(_fromUtf8("gui_output"))
        self.verticalLayout_plots = QtGui.QVBoxLayout()
        self.verticalLayout_plots.setObjectName(_fromUtf8("verticalLayout_plots"))
        self.gui_output.addLayout(self.verticalLayout_plots)
        self.gridLayout_sliders = QtGui.QGridLayout()
        self.gridLayout_sliders.setObjectName(_fromUtf8("gridLayout_sliders"))
        self.label_17 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_sliders.addWidget(self.label_17, 2, 1, 1, 1)
        self.horizontalSlider_time_point = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_time_point.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_time_point.setObjectName(_fromUtf8("horizontalSlider_time_point"))
        self.gridLayout_sliders.addWidget(self.horizontalSlider_time_point, 3, 0, 1, 1)
        self.horizontalSlider_delta_time = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_delta_time.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_delta_time.setObjectName(_fromUtf8("horizontalSlider_delta_time"))
        self.gridLayout_sliders.addWidget(self.horizontalSlider_delta_time, 2, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_sliders.addWidget(self.label_18, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox_topic_selection = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_topic_selection.setObjectName(_fromUtf8("comboBox_topic_selection"))
        self.horizontalLayout_2.addWidget(self.comboBox_topic_selection)
        self.comboBox_sub_topic_selection = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_sub_topic_selection.setObjectName(_fromUtf8("comboBox_sub_topic_selection"))
        self.horizontalLayout_2.addWidget(self.comboBox_sub_topic_selection)
        self.button_add_remove_plot = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.button_add_remove_plot.setObjectName(_fromUtf8("button_add_remove_plot"))
        self.horizontalLayout_2.addWidget(self.button_add_remove_plot)
        self.gridLayout_sliders.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gui_output.addLayout(self.gridLayout_sliders)
        self.horizontalLayout.addLayout(self.gui_output)
        self.gui_input = QtGui.QVBoxLayout()
        self.gui_input.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gui_input.setObjectName(_fromUtf8("gui_input"))
        self.gridLayout_rc = QtGui.QGridLayout()
        self.gridLayout_rc.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_rc.setObjectName(_fromUtf8("gridLayout_rc"))
        self.verticalSlider_rc_button1 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_rc_button1.setMinimum(1000)
        self.verticalSlider_rc_button1.setMaximum(2000)
        self.verticalSlider_rc_button1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_rc_button1.setObjectName(_fromUtf8("verticalSlider_rc_button1"))
        self.gridLayout_rc.addWidget(self.verticalSlider_rc_button1, 0, 5, 1, 1)
        self.verticalSlider_rc_axis1 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_rc_axis1.setMinimum(1000)
        self.verticalSlider_rc_axis1.setMaximum(2000)
        self.verticalSlider_rc_axis1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_rc_axis1.setObjectName(_fromUtf8("verticalSlider_rc_axis1"))
        self.gridLayout_rc.addWidget(self.verticalSlider_rc_axis1, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_rc.addWidget(self.label_3, 2, 2, 1, 1)
        self.verticalSlider_rc_button0 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_rc_button0.setMinimum(1000)
        self.verticalSlider_rc_button0.setMaximum(2000)
        self.verticalSlider_rc_button0.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_rc_button0.setObjectName(_fromUtf8("verticalSlider_rc_button0"))
        self.gridLayout_rc.addWidget(self.verticalSlider_rc_button0, 0, 4, 1, 1)
        self.verticalSlider_rc_button2 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_rc_button2.setMinimum(1000)
        self.verticalSlider_rc_button2.setMaximum(2000)
        self.verticalSlider_rc_button2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_rc_button2.setObjectName(_fromUtf8("verticalSlider_rc_button2"))
        self.gridLayout_rc.addWidget(self.verticalSlider_rc_button2, 0, 6, 1, 1)
        self.verticalSlider_rc_axis2 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_rc_axis2.setMinimum(1000)
        self.verticalSlider_rc_axis2.setMaximum(2000)
        self.verticalSlider_rc_axis2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_rc_axis2.setObjectName(_fromUtf8("verticalSlider_rc_axis2"))
        self.gridLayout_rc.addWidget(self.verticalSlider_rc_axis2, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_rc.addWidget(self.label_7, 2, 6, 1, 1)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_rc.addWidget(self.label_6, 2, 5, 1, 1)
        self.verticalSlider_rc_axis0 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_rc_axis0.setMinimum(1000)
        self.verticalSlider_rc_axis0.setMaximum(2000)
        self.verticalSlider_rc_axis0.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_rc_axis0.setObjectName(_fromUtf8("verticalSlider_rc_axis0"))
        self.gridLayout_rc.addWidget(self.verticalSlider_rc_axis0, 0, 0, 1, 1)
        self.verticalSlider_rc_axis3 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_rc_axis3.setMinimum(1000)
        self.verticalSlider_rc_axis3.setMaximum(2000)
        self.verticalSlider_rc_axis3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_rc_axis3.setObjectName(_fromUtf8("verticalSlider_rc_axis3"))
        self.gridLayout_rc.addWidget(self.verticalSlider_rc_axis3, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_rc.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_rc.addWidget(self.label_5, 2, 4, 1, 1)
        self.verticalSlider_rc_button3 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_rc_button3.setMinimum(1000)
        self.verticalSlider_rc_button3.setMaximum(2000)
        self.verticalSlider_rc_button3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_rc_button3.setObjectName(_fromUtf8("verticalSlider_rc_button3"))
        self.gridLayout_rc.addWidget(self.verticalSlider_rc_button3, 0, 7, 1, 1)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_rc.addWidget(self.label, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_rc.addWidget(self.label_4, 2, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_rc.addWidget(self.label_8, 2, 7, 1, 1)
        self.lcdNumber_rc_axis0 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_rc_axis0.setEnabled(False)
        self.lcdNumber_rc_axis0.setNumDigits(4)
        self.lcdNumber_rc_axis0.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rc_axis0.setProperty("value", 1000.0)
        self.lcdNumber_rc_axis0.setObjectName(_fromUtf8("lcdNumber_rc_axis0"))
        self.gridLayout_rc.addWidget(self.lcdNumber_rc_axis0, 1, 0, 1, 1)
        self.lcdNumber_rc_axis1 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_rc_axis1.setNumDigits(4)
        self.lcdNumber_rc_axis1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rc_axis1.setProperty("intValue", 1000)
        self.lcdNumber_rc_axis1.setObjectName(_fromUtf8("lcdNumber_rc_axis1"))
        self.gridLayout_rc.addWidget(self.lcdNumber_rc_axis1, 1, 1, 1, 1)
        self.lcdNumber_rc_axis2 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_rc_axis2.setNumDigits(4)
        self.lcdNumber_rc_axis2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rc_axis2.setProperty("intValue", 1000)
        self.lcdNumber_rc_axis2.setObjectName(_fromUtf8("lcdNumber_rc_axis2"))
        self.gridLayout_rc.addWidget(self.lcdNumber_rc_axis2, 1, 2, 1, 1)
        self.lcdNumber_rc_axis3 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_rc_axis3.setNumDigits(4)
        self.lcdNumber_rc_axis3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rc_axis3.setProperty("intValue", 1000)
        self.lcdNumber_rc_axis3.setObjectName(_fromUtf8("lcdNumber_rc_axis3"))
        self.gridLayout_rc.addWidget(self.lcdNumber_rc_axis3, 1, 3, 1, 1)
        self.lcdNumber_rc_button0 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_rc_button0.setNumDigits(4)
        self.lcdNumber_rc_button0.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rc_button0.setProperty("intValue", 1000)
        self.lcdNumber_rc_button0.setObjectName(_fromUtf8("lcdNumber_rc_button0"))
        self.gridLayout_rc.addWidget(self.lcdNumber_rc_button0, 1, 4, 1, 1)
        self.lcdNumber_rc_button1 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_rc_button1.setNumDigits(4)
        self.lcdNumber_rc_button1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rc_button1.setProperty("intValue", 1000)
        self.lcdNumber_rc_button1.setObjectName(_fromUtf8("lcdNumber_rc_button1"))
        self.gridLayout_rc.addWidget(self.lcdNumber_rc_button1, 1, 5, 1, 1)
        self.lcdNumber_rc_button2 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_rc_button2.setNumDigits(4)
        self.lcdNumber_rc_button2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rc_button2.setProperty("intValue", 1000)
        self.lcdNumber_rc_button2.setObjectName(_fromUtf8("lcdNumber_rc_button2"))
        self.gridLayout_rc.addWidget(self.lcdNumber_rc_button2, 1, 6, 1, 1)
        self.lcdNumber_rc_button3 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_rc_button3.setNumDigits(4)
        self.lcdNumber_rc_button3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rc_button3.setProperty("intValue", 1000)
        self.lcdNumber_rc_button3.setObjectName(_fromUtf8("lcdNumber_rc_button3"))
        self.gridLayout_rc.addWidget(self.lcdNumber_rc_button3, 1, 7, 1, 1)
        self.gui_input.addLayout(self.gridLayout_rc)
        self.gridLayout_parameters = QtGui.QGridLayout()
        self.gridLayout_parameters.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_parameters.setObjectName(_fromUtf8("gridLayout_parameters"))
        self.label_11 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_parameters.addWidget(self.label_11, 2, 2, 1, 1)
        self.lcdNumber_parameter2 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_parameter2.setObjectName(_fromUtf8("lcdNumber_parameter2"))
        self.gridLayout_parameters.addWidget(self.lcdNumber_parameter2, 2, 1, 1, 1)
        self.lcdNumber_parameter6 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_parameter6.setObjectName(_fromUtf8("lcdNumber_parameter6"))
        self.gridLayout_parameters.addWidget(self.lcdNumber_parameter6, 6, 1, 1, 1)
        self.lcdNumber_parameter1 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_parameter1.setObjectName(_fromUtf8("lcdNumber_parameter1"))
        self.gridLayout_parameters.addWidget(self.lcdNumber_parameter1, 1, 1, 1, 1)
        self.horizontalSlider_parameter5 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_parameter5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_parameter5.setObjectName(_fromUtf8("horizontalSlider_parameter5"))
        self.gridLayout_parameters.addWidget(self.horizontalSlider_parameter5, 5, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_parameters.addWidget(self.label_9, 0, 2, 1, 1)
        self.lcdNumber_parameter3 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_parameter3.setObjectName(_fromUtf8("lcdNumber_parameter3"))
        self.gridLayout_parameters.addWidget(self.lcdNumber_parameter3, 3, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_parameters.addWidget(self.label_12, 3, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_parameters.addWidget(self.label_13, 4, 2, 1, 1)
        self.horizontalSlider_parameter6 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_parameter6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_parameter6.setObjectName(_fromUtf8("horizontalSlider_parameter6"))
        self.gridLayout_parameters.addWidget(self.horizontalSlider_parameter6, 6, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_parameters.addWidget(self.label_16, 7, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_parameters.addWidget(self.label_15, 6, 2, 1, 1)
        self.horizontalSlider_parameter7 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_parameter7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_parameter7.setObjectName(_fromUtf8("horizontalSlider_parameter7"))
        self.gridLayout_parameters.addWidget(self.horizontalSlider_parameter7, 7, 0, 1, 1)
        self.horizontalSlider_parameter4 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_parameter4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_parameter4.setObjectName(_fromUtf8("horizontalSlider_parameter4"))
        self.gridLayout_parameters.addWidget(self.horizontalSlider_parameter4, 4, 0, 1, 1)
        self.horizontalSlider_parameter3 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_parameter3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_parameter3.setObjectName(_fromUtf8("horizontalSlider_parameter3"))
        self.gridLayout_parameters.addWidget(self.horizontalSlider_parameter3, 3, 0, 1, 1)
        self.horizontalSlider_parameter1 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_parameter1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_parameter1.setObjectName(_fromUtf8("horizontalSlider_parameter1"))
        self.gridLayout_parameters.addWidget(self.horizontalSlider_parameter1, 1, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_parameters.addWidget(self.label_14, 5, 2, 1, 1)
        self.horizontalSlider_parameter2 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_parameter2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_parameter2.setObjectName(_fromUtf8("horizontalSlider_parameter2"))
        self.gridLayout_parameters.addWidget(self.horizontalSlider_parameter2, 2, 0, 1, 1)
        self.horizontalSlider_parameter0 = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_parameter0.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.horizontalSlider_parameter0.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_parameter0.setObjectName(_fromUtf8("horizontalSlider_parameter0"))
        self.gridLayout_parameters.addWidget(self.horizontalSlider_parameter0, 0, 0, 1, 1)
        self.lcdNumber_parameter5 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_parameter5.setObjectName(_fromUtf8("lcdNumber_parameter5"))
        self.gridLayout_parameters.addWidget(self.lcdNumber_parameter5, 5, 1, 1, 1)
        self.lcdNumber_parameter4 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_parameter4.setObjectName(_fromUtf8("lcdNumber_parameter4"))
        self.gridLayout_parameters.addWidget(self.lcdNumber_parameter4, 4, 1, 1, 1)
        self.lcdNumber_parameter7 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_parameter7.setObjectName(_fromUtf8("lcdNumber_parameter7"))
        self.gridLayout_parameters.addWidget(self.lcdNumber_parameter7, 7, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_parameters.addWidget(self.label_10, 1, 2, 1, 1)
        self.lcdNumber_parameter0 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_parameter0.setObjectName(_fromUtf8("lcdNumber_parameter0"))
        self.gridLayout_parameters.addWidget(self.lcdNumber_parameter0, 0, 1, 1, 1)
        self.gui_input.addLayout(self.gridLayout_parameters)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.button_send = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.button_send.setMaximumSize(QtCore.QSize(200, 50))
        self.button_send.setObjectName(_fromUtf8("button_send"))
        self.horizontalLayout_3.addWidget(self.button_send)
        self.checkBox = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.gui_input.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.gui_input)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "phoenixGUI", None))
        self.label_17.setText(_translate("MainWindow", "dt", None))
        self.label_18.setText(_translate("MainWindow", "time", None))
        self.button_add_remove_plot.setText(_translate("MainWindow", "add/remove", None))
        self.label_3.setText(_translate("MainWindow", "axis2", None))
        self.label_7.setText(_translate("MainWindow", "button2", None))
        self.label_6.setText(_translate("MainWindow", "button1", None))
        self.label_2.setText(_translate("MainWindow", "axis0", None))
        self.label_5.setText(_translate("MainWindow", "button0", None))
        self.label.setText(_translate("MainWindow", "axis1", None))
        self.label_4.setText(_translate("MainWindow", "axis3", None))
        self.label_8.setText(_translate("MainWindow", "button3", None))
        self.label_11.setText(_translate("MainWindow", "parameter2", None))
        self.label_9.setText(_translate("MainWindow", "parameter0", None))
        self.label_12.setText(_translate("MainWindow", "parameter3", None))
        self.label_13.setText(_translate("MainWindow", "parameter4", None))
        self.label_16.setText(_translate("MainWindow", "parameter7", None))
        self.label_15.setText(_translate("MainWindow", "parameter6", None))
        self.label_14.setText(_translate("MainWindow", "parameter5", None))
        self.label_10.setText(_translate("MainWindow", "parameter1", None))
        self.button_send.setText(_translate("MainWindow", "send", None))
        self.checkBox.setText(_translate("MainWindow", "automatic send", None))

