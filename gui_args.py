# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gui_args(object):
    def setupUi(self, gui_args):
        gui_args.setObjectName("gui_args")
        gui_args.setWindowIcon(QtGui.QIcon('logo.jpg'))
        gui_args.resize(293, 415)
        self.verticalLayout = QtWidgets.QVBoxLayout(gui_args)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(gui_args)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(gui_args)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setCenterButtons(True)
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(gui_args)
        self.buttonBox.accepted.connect(gui_args.accept)
        self.buttonBox.rejected.connect(gui_args.reject)
        QtCore.QMetaObject.connectSlotsByName(gui_args)

    def retranslateUi(self, gui_args):
        _translate = QtCore.QCoreApplication.translate
        gui_args.setWindowTitle(_translate("gui_args", "Arguments"))
        self.label.setText(_translate("gui_args", "Arguments"))
