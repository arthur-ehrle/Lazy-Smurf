import os
import glob
import base64

from chiffrement import *

ip_base = "10.10.10.10"
login_base = déchiffrement("yjoyai","ziak")
mdp_base = déchiffrement("mstxjcnvqnfftobgdcnxiut","akimbo")
nom_base="equipements"
current = os.getcwd()
chemin_csv = "{}\\equipements.csv".format(current)
chemin_conf = "{}\\conf.txt".format(current)
os_dir = "os"
tableau_os = [os.path.basename(f) for f in glob.glob(os.path.join('os/', '*.yaml'))]
devices = '.\\devices.csv'
mode = "notConnected" # ou 'connected'