import yaml
from host import *


def dict_replace_value(d, old, new):
    x = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = dict_replace_value(v, old, new)
        elif isinstance(v, list):
            v = list_replace_value(v, old, new)
        elif isinstance(v, str):
            v = v.replace(old, new)
        x[k] = v
    return x

def list_replace_value(l, old, new):
    x = []
    for e in l:
        if isinstance(e, list):
            e = list_replace_value(e, old, new)
        elif isinstance(e, dict):
            e = dict_replace_value(e, old, new)
        elif isinstance(e, str):
            e = e.replace(old, new)
        x.append(e)
    return x

def get_os_config(os):
    with open(r'os/{}.yaml'.format(os)) as f: 
        return yaml.full_load(f)

def get_actions(os_config_dict):
    return list(os_config_dict.keys())

def get_routines(action, os_config):
    return list(os_config[action].keys())

def get_args_routine(routine):
    arguments = routine["arguments"]
    if isinstance(arguments, dict):
        return arguments
    else:
        return {}

def run_routine_from_data(data):

    ip = data["ip"]
    username = data["username"]
    password = data["password"]
    os = data["os"]
    routine = data["routine"]
    action_type = data["action_type"]
    routine_args = data["routine_args"]
    
    host = Host(ip,username,password,os)
    routine_manager = RoutineManager(host, routine, action_type, routine_args)

    return_command = routine_manager.exec_routine()
    return return_command


class RoutineManager:
    # Constructeur
    def __init__(self, host, routine, action_type, routine_args):
        self.host = host
        self.routine = routine
        self.action_type = action_type
        self.routine_args = routine_args
        #self.init_arguments()

    def exec_routine(self):
        for function_name, content in self.routine.items():  
            if function_name == "commands":
                self.commands(self.routine["commands"])
            else:
                exec_function = getattr(self, function_name)                        # On stocke dans la variable 'exec_function', la méthode de classe récupérée dans 'function_name'
                exec_function(content)                                              # On execute la méthode de classe 'function_name'

        self.ssh.disconnect()                                                       # Deconnection ssh
        return self.return_command

    def commands(self, content):
        self.ssh = self.host.connexion()
        retour = ""
        if(self.action_type == 'show'):
            for i in content:
                retour += f"{self.ssh.send_command(i)}\n"

        elif(self.action_type == 'conf'):
            retour += f"{self.ssh.send_config_set(content)}"
        self.return_command = retour

    def arguments(self, content):
        if self.routine_args == {}:
            print("Pas besoin d'args")
        else:
            print("Besoins d'args")
            for arg_name, arg_value in self.routine_args.items():
                arg_tag = self.routine["arguments"][arg_name]
                self.routine = dict_replace_value(self.routine, arg_tag, arg_value)
