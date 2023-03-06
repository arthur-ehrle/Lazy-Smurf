# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajout_materiel.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from variables import tableau_os
import os

class Ui_ajout_materiel(object):
    def setupUi(self, ajout_materiel):
        ajout_materiel.setObjectName("ajout_materiel")
        ajout_materiel.resize(428, 201)
        ajout_materiel.setWindowIcon(QtGui.QIcon('logo.jpg'))
        self.formLayout = QtWidgets.QFormLayout(ajout_materiel)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ajout_materiel)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtWidgets.QLabel(ajout_materiel)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.input_nom = QtWidgets.QLineEdit(ajout_materiel)
        self.input_nom.setObjectName("input_nom")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_nom)
        self.label_3 = QtWidgets.QLabel(ajout_materiel)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.input_ip = QtWidgets.QLineEdit(ajout_materiel)
        self.input_ip.setObjectName("input_ip")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_ip)
        self.label_4 = QtWidgets.QLabel(ajout_materiel)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.input_login = QtWidgets.QLineEdit(ajout_materiel)
        self.input_login.setObjectName("input_login")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_login)
        self.label_5 = QtWidgets.QLabel(ajout_materiel)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.input_passwd = QtWidgets.QLineEdit(ajout_materiel)
        self.input_passwd.setObjectName("input_passwd")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input_passwd)
        self.label_6 = QtWidgets.QLabel(ajout_materiel)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.input_os = QtWidgets.QComboBox(ajout_materiel)
        self.input_os.setObjectName("input_os")
        for os_actuel in tableau_os:
            self.input_os.addItem(os.path.splitext(os_actuel)[0])
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input_os)
        self.validation = QtWidgets.QDialogButtonBox(ajout_materiel)
        self.validation.setOrientation(QtCore.Qt.Horizontal)
        self.validation.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.validation.setCenterButtons(True)
        self.validation.setObjectName("validation")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.validation)

        self.retranslateUi(ajout_materiel)
        self.validation.rejected.connect(ajout_materiel.reject)
        self.validation.accepted.connect(ajout_materiel.accept)
        QtCore.QMetaObject.connectSlotsByName(ajout_materiel)

    def retranslateUi(self, ajout_materiel):
        _translate = QtCore.QCoreApplication.translate
        ajout_materiel.setWindowTitle(_translate("ajout_materiel", "Ajout d\'un materiel"))
        self.label.setText(_translate("ajout_materiel", "Ajout d\'un materiel"))
        self.label_2.setText(_translate("ajout_materiel", "Nom"))
        self.label_3.setText(_translate("ajout_materiel", "IP"))
        self.label_4.setText(_translate("ajout_materiel", "Login"))
        self.label_5.setText(_translate("ajout_materiel", "Password"))
        self.label_6.setText(_translate("ajout_materiel", "OS"))
    


