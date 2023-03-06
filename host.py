import netmiko

class Host:
    # Constructeur
    def __init__(self,ip,username,password,os):
        self.ip = ip
        self.username = username
        self.password = password
        self.os = os

    def connexion(self):
        ssh = netmiko.ConnectHandler(ip=self.ip,device_type=self.os,username=self.username,password=self.password)
        ssh.clear_buffer()
        return ssh