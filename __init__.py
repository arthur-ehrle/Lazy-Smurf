from host import *
from bdd import *
from fonctions import *
from graphical import *


def run_routine_from_data_with_callback(data,function):
    try:
        result = run_routine_from_data(data)  
    except:
        result = "connexion échouée"
    function(result)

if __name__ == "__main__": # GUI
    pyqtRemoveInputHook()
    app = QtWidgets.QApplication(sys.argv) # objet QApplication
    app.setStyleSheet(style_content) # appliquer le style contenu dans la variable style_content
    ex = Ui_MainWindow()  # créer une instance de Ui_Mainwindow  
    w = QtWidgets.QMainWindow() # instancier la classe QMainWindow 
    ex.setupUi(w) #appeler les objets de la méthode setupUi

    ex.request_action = run_routine_from_data_with_callback
    ex.start()

    w.show()
    
    sys.exit(app.exec_())