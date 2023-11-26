from PyQt5.QtCore import QObject
import matplotlib.pyplot as plt
import os

class Modelo:
    def __init__(self):
        self.__us ="medicoAnalitico"
        self.__cont="bio12345"
        self.__dic={}
    def setlogin(self,l):
        self.__us=l
    def setPassword(self,p):
        self.__cont=p  
    def verificar(self,l,p):
        self.datos()
        r=(self.__us== l) and (self.__cont == p)
        return [r,self.__dic]
    def datos(self):
        lista_archivos = os.listdir("images")
        for archivo in lista_archivos:
            datos = os.listdir("images/"+ archivo)
            self.__dic[archivo]=datos
    def pista(self):
        return self.__dic
  