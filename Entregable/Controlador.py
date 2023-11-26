from PyQt5.QtWidgets import QApplication
from Modelo import Modelo
from Vista import Vista, Vp
import sys

class Controlador:
    def __init__(self, modelo, vista):
        self.__modelo = modelo
        self.__vista = vista
    def login(self,l,p):
        return self.__modelo.verificar(l,p)
    def pista1(self):
        return self.__modelo.pista()

def main():
    app = QApplication(sys.argv)
    modelo = Modelo()
    vista = Vista()
    mi_controlador=Controlador(modelo,vista)
    vista.addControler(mi_controlador)
    vista.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()