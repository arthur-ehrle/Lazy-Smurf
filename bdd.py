import psycopg2
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from variables import *

class Bdd():
    def __init__(self):
        self.test = 10

    def connexion(self):
        connexion = None
        reponse = ""
        self.connexion = psycopg2.connect(host=ip_base, database=nom_base, user=login_base, password=mdp_base)
        self.curseur= self.connexion.cursor()
    
    def end_connexion(self):
        self.curseur.close()

    def lister_infos(self, nom):
        if nom == "*":
            self.curseur.execute("SELECT * FROM materiels ")
        else :
            self.curseur.execute("SELECT * FROM materiels where nom = '{}'".format(nom))
        row = self.curseur.fetchone()
        while row is not None:       
            print(str(row)) 
            ip = str(row[1])
            username = str(row[3])
            password = str(row[4])
            os = str(row[2])
            row = self.curseur.fetchone()
        return ip, username, password, os

    def graph_bdd(self):
            i = 0
            sizes=[]
            nom = []
            for sys_exploit in tableau_os:
                sys_exploit=os.path.splitext(sys_exploit)[0]
                self.curseur.execute("SELECT COUNT(*) FROM materiels WHERE os='{}';".format(sys_exploit)) #Récupérer le nbr d'équipements cisco
                row = self.curseur.fetchone()
                val_os = str(row[0])
                if int(val_os) > 0:
                    sizes.append(val_os)
                    nom.append(sys_exploit)
            plt.pie(sizes, labels=nom, 
            autopct='%1.1f%%',  startangle=90)
            plt.axis('equal')
            plt.savefig('inventaire_bdd.png') #sauvegarder le graphe
            plt.show() #Afficher le graphe

    def requetes_bdd(self, requete):
            self.curseur.execute(requete)
            self.connexion.commit()
    
    def ajout_mat_massif(self):
        sqlstr = "COPY materiels(ip,os,login,password,nom) FROM STDIN DELIMITER ';' CSV HEADER NULL AS '' "
        with open(chemin_csv) as f:
            self.curseur.copy_expert(sqlstr, f)  
        self.connexion.commit()
        self.lister_infos("")