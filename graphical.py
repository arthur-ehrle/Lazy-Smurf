# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tsp.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


#####################################################################################
#************************* IMPORTS **************************************************
#####################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.Qt import QAbstractItemView, QLineEdit

import os
import sys
import psycopg2
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from fonctions import *
from variables import *

from style import style_content
from ajout_materiel import *
from gui_args import *



#####################################################################################
#************************* FORME ****************************************************
#####################################################################################
class Ui_MainWindow(object):  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('logo.jpg'))
        MainWindow.resize(634, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.init_from_gui("show"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.list_evenements_2 = QtWidgets.QListWidget(self.centralwidget)
        self.list_evenements_2.setObjectName("list_evenements_2")
        self.list_evenements_2.itemDoubleClicked.connect(self.reponse)
        self.gridLayout.addWidget(self.list_evenements_2, 2, 1, 8, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.list_equipements = QtWidgets.QTableWidget(self.centralwidget)
        self.list_equipements.setObjectName("list_equipements")
        self.list_equipements.clicked.connect(self.materiel_actuel)
        self.list_equipements.doubleClicked.connect(self.start_putty)
        self.list_equipements.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.list_equipements.setSelectionMode(QtWidgets.QTableView.SingleSelection) # multi selection
        #self.list_equipements.setSelectionMode(QtWidgets.QTableView.MultiSelection) # multi selection
        self.list_equipements.setColumnCount(3)
        self.list_equipements.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.list_equipements.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_equipements.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_equipements.setHorizontalHeaderItem(2, item)
        header = self.list_equipements.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.gridLayout.addWidget(self.list_equipements, 8, 0, 1, 1)
        self.list_evenements = QtWidgets.QListWidget(self.centralwidget)
        self.list_evenements.setObjectName("list_evenements")
        
        self.gridLayout.addWidget(self.list_evenements, 9, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.init_from_gui("conf"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.modif_mat_simple)
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.list_evenements.clear())
        self.pushButton_5.clicked.connect(self.start)
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        # self.text_input_1 = QtWidgets.QLineEdit(self.centralwidget)
        # self.text_input_1.setObjectName("text_input_1")
        # self.text_input_1.setPlaceholderText("Votre réponse")
        # self.gridLayout.addWidget(self.text_input_1, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAjout_materiels = QtWidgets.QMenu(self.menuMenu)
        self.menuAjout_materiels.setObjectName("menuAjout_materiels")
        self.menuSupprimer_materiels = QtWidgets.QMenu(self.menuMenu)
        self.menuSupprimer_materiels.setObjectName("menuSupprimer_materiels")

        self.menulist_evenements_2s = QtWidgets.QMenu(self.menubar)
        self.menulist_evenements_2s.setObjectName("menulist_evenements_2s")

        self.actionGraph = QtWidgets.QAction(MainWindow)
        self.actionGraph.setObjectName("actionGraph")
        self.menulist_evenements_2s.addAction(self.actionGraph)
        self.actionGraph.triggered.connect(self.graph_bdd)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExecution = QtWidgets.QAction(MainWindow)
        self.actionExecution.setObjectName("actionExecution")
        self.actionExecution.triggered.connect(self.ajout_mat_massif)
        self.actionAjout = QtWidgets.QAction(MainWindow)
        self.actionAjout.setObjectName("actionAjout")
        self.actionAjout.triggered.connect(self.ajout_mat_simple)
        self.actionSupprimer_materiel = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_materiel.setObjectName("actionSupprimer_materiel")
        self.actionSupprimer_materiel.triggered.connect(self.supprimer_materiel)
        self.actionReadme_2 = QtWidgets.QAction(MainWindow)
        self.actionReadme_2.setObjectName("actionReadme_2")
        self.actionReadme_2.triggered.connect(self.readme)
        self.menuAjout_materiels.addAction(self.actionExecution)
        self.menuAjout_materiels.addSeparator()
        self.menuAjout_materiels.addAction(self.actionAjout)
        self.menuAjout_materiels.addSeparator()
        self.menuAjout_materiels.addAction(self.actionReadme_2)
        self.menuSupprimer_materiels.addAction(self.actionSupprimer_materiel)
        self.menuMenu.addAction(self.menuAjout_materiels.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menuSupprimer_materiels.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menulist_evenements_2s.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ajout_materiel = QtWidgets.QDialog() #instance ajout matériel
        self.instance_ajout = Ui_ajout_materiel() #instance ajout matériel
        self.instance_ajout.setupUi(self.ajout_materiel) #execution de setupui pour les widgets de l'instance ajout matériel

        #self.lister_infos("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Manager Tool"))
        self.pushButton.setText(_translate("MainWindow", "Voir  Configuration"))
        self.label.setText(_translate("MainWindow", "Network Manager Tool"))
        item = self.list_equipements.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.list_equipements.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "OS"))
        item = self.list_equipements.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP"))
        self.pushButton_2.setText(_translate("MainWindow", "Configurer"))
        self.pushButton_3.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_5.setText(_translate("MainWindow", "Clear events"))
        self.menuMenu.setTitle(_translate("MainWindow", "Gestion materiels"))
        self.menuAjout_materiels.setTitle(_translate("MainWindow", "Ajout materiels"))
        self.menuSupprimer_materiels.setTitle(_translate("MainWindow", "Supprimer materiels"))
        self.menulist_evenements_2s.setTitle(_translate("MainWindow", "Fonctions supplementaires"))
        self.actionExecution.setText(_translate("MainWindow", "Ajouter materiel CSV"))
        self.actionAjout.setText(_translate("MainWindow", "Ajouter materiel"))
        self.actionSupprimer_materiel.setText(_translate("MainWindow", "Supprimer materiel"))
        self.actionReadme_2.setText(_translate("MainWindow", "Readme"))
        self.actionGraph.setText(_translate("MainWindow", "Graph équipements"))

#####################################################################################
#************************* FONCTIONS ************************************************
#####################################################################################

    def start(self):
        try:    
            self.lister_infos("")
        except:
            pass

    def start_putty(self):
        os.system('putty.exe -ssh {}@{} -pw {}'.format(self.username,self.ip,self.password))
        
    def graph_bdd(self):
        sizes=[]
        nom = []
        if mode == 'connected':
            i = 0
            connexion = None
            reponse = ""
            connexion = psycopg2.connect(host=ip_base, database=nom_base, user=login_base, password=mdp_base)
            curseur = connexion.cursor()        
            for sys_exploit in tableau_os:
                sys_exploit=os.path.splitext(sys_exploit)[0]
                curseur.execute("SELECT COUNT(*) FROM materiels WHERE os='{}';".format(sys_exploit)) 
                row = curseur.fetchone()
                val_os = str(row[0])
                if int(val_os) > 0:
                    sizes.append(val_os)
                    nom.append(sys_exploit)
            curseur.close()
        if mode == 'notConnected':
            for sys_exploit in tableau_os:
                df = pd.read_csv(devices,sep=';')
                sys_exploit=os.path.splitext(sys_exploit)[0]
                df = df[df["OS"]==sys_exploit]
                val_os = len(df.index)
                print("EXPLOIT",sys_exploit)
                print("EXPLOIT",val_os)

                if int(val_os) > 0:
                    sizes.append(val_os)
                    nom.append(sys_exploit)
        
        plt.pie(sizes, labels=nom, 
        autopct='%1.1f%%',  startangle=90)
        plt.axis('equal')
        plt.savefig('inventaire_bdd.png') #sauvegarder le graphe
        plt.show() #Afficher le graphe

    def lister_infos(self,nom_equipement):
        self.list_equipements.clear()
        if mode == 'connected':
            try:
                i = 0
                connexion = None
                reponse = ""
                connexion = psycopg2.connect(host=ip_base, database=nom_base, user=login_base, password=mdp_base)
                curseur= connexion.cursor()
                if nom_equipement == "":
                    curseur.execute("SELECT * FROM materiels ")
                else :
                    curseur.execute("SELECT * FROM materiels where nom = '{}'".format(nom_equipement))
                row = curseur.fetchone()
                while row is not None:   
                    # initialisation des variables
                    ip = str(row[1])
                    username = str(row[3])
                    password = str(row[4])
                    os = str(row[2])
                    nom = str(row[5])

                    if nom_equipement == "":
                        # ajout des variables dans la table 
                        self.list_equipements.insertRow(i)
                        self.list_equipements.setItem(i,0, QTableWidgetItem(str(row[5])))
                        self.list_equipements.setItem(i,1, QTableWidgetItem(str(row[2])))
                        self.list_equipements.setItem(i,2, QTableWidgetItem(str(row[1])))

                    # passage à la ligne suivante
                    i=i+1
                    row = curseur.fetchone()
                curseur.close()
            except:
                self.list_evenements.addItem("Erreur de connexion à la base de donnée ")
        if mode == 'notConnected':
            try:
                # lecture du csv
                donnees = pd.read_csv(devices,sep=';')

                if nom_equipement != "":
                    donnees = donnees[donnees["NOM"]==nom_equipement]

                # création des différentes listes
                ip = donnees.IP.to_list()
                username = donnees.LOGIN.to_list()
                password = donnees.MDP.to_list()
                os = donnees.OS.to_list()
                nom = donnees.NOM.to_list()

                # ajout des données dans la table graphique
                if nom_equipement == "":
                    for i in range (len(donnees)):
                        self.list_equipements.insertRow(i)
                        self.list_equipements.setItem(i,2, QTableWidgetItem(ip[i]))
                        self.list_equipements.setItem(i,1, QTableWidgetItem(os[i]))
                        self.list_equipements.setItem(i,0, QTableWidgetItem(nom[i]))
            except:
                self.list_evenements.addItem("Erreur de connexion de lecture du CSV ")

    def requetes_bdd(self, requete):
        connexion = None
        reponse = ""
        connexion = psycopg2.connect(host=ip_base, database=nom_base, user=login_base, password=mdp_base)
        curseur= connexion.cursor()          
        curseur.execute(requete)
        connexion.commit()
        curseur.close()
        connexion.close()
        return 

    def supprimer_materiel(self):
        try:
            self.requetes_bdd(("DELETE FROM materiels WHERE id = '{}'".format(self.id)))   
            self.lister_infos("")
        except:
            self.list_evenements.addItem("Veuillez saisir un équipement d'abord")

    def ajout_mat_massif(self):
        connexion = None
        reponse = ""
        connexion = psycopg2.connect(host=ip_base, database=nom_base, user=login_base, password=mdp_base)
        curseur= connexion.cursor()          
        sqlstr = "COPY materiels(ip,os,login,password,nom) FROM STDIN DELIMITER ';' CSV HEADER NULL AS '' "
        with open(chemin_csv, encoding='latin-1') as f:
            curseur.copy_expert(sqlstr, f)  
        connexion.commit()
        curseur.close()
        connexion.close()
        self.lister_infos("")
     
    def ajout_mat_simple(self):
        self.ajout_materiel.setWindowTitle("Ajout d\'un materiel")
        self.instance_ajout.label.setText("Ajout d\'un materiel")
        if self.ajout_materiel.exec():
            ip = self.instance_ajout.input_ip.text()
            login =self.instance_ajout.input_login.text()
            password =self.instance_ajout.input_passwd.text()
            name = self.instance_ajout.input_nom.text()
            index=self.instance_ajout.input_os.currentIndex()
            os=self.instance_ajout.input_os.itemText(index)
            self.requetes_bdd(("INSERT INTO materiels (ip,os,login,password,nom) VALUES ('{}','{}','{}','{}','{}')".format(ip,os,login,password,name)))
            self.lister_infos("")

    def modif_mat_simple(self):
        try:
            self.ajout_materiel.setWindowTitle("Modification d'un materiel")
            self.instance_ajout.label.setText("Modification d'un materiel")
            self.instance_ajout.input_ip.setText(self.ip)
            self.instance_ajout.input_login.setText(self.username)
            self.instance_ajout.input_passwd.setText(self.password)
            self.instance_ajout.input_nom.setText(self.nom)
            i=0
            for valeur_os in tableau_os:
                valeur_os=os.path.splitext(valeur_os)[0]
                if valeur_os == self.os:
                    self.instance_ajout.input_os.setCurrentIndex(i)
                else:
                    i=i+1
            if self.ajout_materiel.exec():
                ip = self.instance_ajout.input_ip.text()
                login =self.instance_ajout.input_login.text()
                password =self.instance_ajout.input_passwd.text()
                name = self.instance_ajout.input_nom.text()
                index=self.instance_ajout.input_os.currentIndex()
                os_mat=self.instance_ajout.input_os.itemText(index)
                self.requetes_bdd(("UPDATE materiels SET ip='{}', os='{}', login='{}', password='{}', nom='{}' WHERE id = {}".format(ip,os_mat,login,password,name,self.id)))
                self.lister_infos("")
        except:
            self.list_evenements.addItem("Veuillez saisir un équipement d'abord")
            
    def materiel_actuel(self):
        try:
            self.list_evenements_2.clear()
            ligne_actuelle = self.list_equipements.currentRow()
            item = self.list_equipements.item(ligne_actuelle,0)
            ligne_actuelle = item.text()
            if mode == "connected":
                connexion = None
                reponse = ""
                connexion = psycopg2.connect(host=ip_base, database=nom_base, user=login_base, password=mdp_base)
                curseur= connexion.cursor()          
                curseur.execute("SELECT * FROM materiels where nom = '{}'".format(ligne_actuelle))
                row = curseur.fetchone()
                while row is not None:   
                    # initialisation des variables
                    self.ip = str(row[1])
                    self.username = str(row[3])
                    self.password = str(row[4])
                    self.os = str(row[2])
                    self.nom = str(row[5])
                    self.id = str(row[0])
                    row = curseur.fetchone()  
                curseur.close()
            if mode == 'notConnected':
        
                # lecture du csv
                donnees = pd.read_csv(devices,sep=';')             
                donnees = donnees[donnees["NOM"]==ligne_actuelle]

                # création des différentes listes
                self.ip = "".join(donnees.IP.to_list())
                self.username = "".join(donnees.LOGIN.to_list())
                self.password = "".join(donnees.MDP.to_list())
                self.os = "".join(donnees.OS.to_list())
                self.nom = "".join(donnees.NOM.to_list())

            
        except:
            pass

    def readme(self):   
        self.list_evenements.addItem("""Il est possible d'ajouter plusieurs équipements en même temps dans la BDD.
        Il faut les entrer dans le fichier CSV mis à disposition en respectant les normes d'écriture puis cliquer sur l'onglet mis à disposition.
        """)

    def reponse(self): 
        rep =  self.list_evenements_2.currentItem()
        rep = rep.text()    
        self.init_from_gui2(rep)

    def init_from_gui(self, action_type):
       
        self.action_type = action_type
        self.list_evenements_2.clear()
        self.os_config = get_os_config(self.os)
        routines = get_routines(action_type, self.os_config)
        for choix in routines:
            self.list_evenements_2.addItem(choix)
      

    def init_from_gui2(self, choice_routine):
        input_args = QtWidgets.QDialog() 
        instance_args = Ui_gui_args() 
        instance_args.setupUi(input_args)

        self.routine = self.os_config[self.action_type][choice_routine]

        arguments = get_args_routine(self.routine)

        self.routine_args = {}
        tab_arg_name = list(arguments.keys())
        tab_arg_val=[]

        if len(tab_arg_name) > 0:
            for i in range(len(tab_arg_name)): # première boucle pour remplir le tableau
                name_label = f"{tab_arg_name[i]} :"
                nom_input = tab_arg_name[i]
                instance_widget = self.creer_widgets(name_label,nom_input, instance_args,input_args)
                tab_arg_val.append(instance_widget)

            if input_args.exec():  # quand je vais appuyer sur valider
                for j in range(len(tab_arg_name)): # Deuxième boucle pour parcourir le tableau une fois que les champs sont remplis
                    self.routine_args[tab_arg_name[j]] = tab_arg_val[j].text()
                self.end_init_gui2()
                
        else:
            print("Pas besoin d'args")
            self.end_init_gui2()
        return

    def end_init_gui2(self):
        data  = {
        "ip":self.ip,
        "username": self.username,
        "password":self.password,
        "os":self.os,
        "routine":self.routine,
        "action_type":self.action_type,
        "routine_args":self.routine_args
        }
        self.request_action(data, self.display_action_result)
        return

    def creer_widgets(self,nom_label,nom_input,instance_args,input_args):
        #widget label
        instance_args.nom_label = QtWidgets.QLabel(input_args)
        instance_args.nom_label.setAlignment(QtCore.Qt.AlignCenter)
        instance_args.nom_label.setObjectName(nom_label)
        instance_args.nom_label.setText(nom_label)
        instance_args.verticalLayout.addWidget(instance_args.nom_label)

        #widget input
        instance_args.nom_input = QtWidgets.QLineEdit(input_args)
        instance_args.nom_input.setObjectName(nom_input)
        instance_args.nom_input.setPlaceholderText(nom_input)
        instance_args.verticalLayout.addWidget(instance_args.nom_input)
        return instance_args.nom_input
    
    def request_action(self, data, function):
        print(data)
    
    def display_action_result(self, result):
        print(result)
        
        for lines in result.splitlines():
            if lines != "!":
                self.list_evenements.addItem(lines)
            else:
                pass