from PyQt5.QtWidgets import QDialog, QMessageBox 
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os
import pydicom
import matplotlib.pyplot as plt


class Vista(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ingresar.ui', self)
        self.__control=""
        self.__lista={}
        self.setup()
    def verl(self):
        return self.__lista
    def setup(self):
        self.ing.clicked.connect(self.ingresar)
    def ingresar(self):
        us= self.us.text()
        cont=self.cont.text()
        r=self.__control.login(us,cont)
        if r[0] == False:
            print("s")
            msg = QMessageBox()
            msg.setText("No es el usuario o contraseña")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            self.__lista=r[1]
            ventanap=Vp(self)
            self.hide()
            ventanap.show()
        pass
    def addControler(self,c):
        self.__control=c
class Vp(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi('ventanaP.ui', self)
        self.__controlador=""
        self.__ventanaP=ppal
        self.__lip={}
        self.__llave=""
        self.setup()
    def setup(self):
        self.archivo.currentIndexChanged.connect(self.cargar)
        self.imgP.valueChanged.connect(self.pasar)
        self.__lip=self.__ventanaP.verl()
        for i in self.__lip:
            self.archivo.addItem(i)
    def cargar(self):
        self.__llave=""
        self.__llave=self.archivo.currentText()
        d=self.__lip[self.__llave]
        self.imgP.setMinimum(0)
        self.imgP.setMaximum(len(d))
        self.imgP.setValue(0)
        pass
    def pasar(self):
        x=self.__lip[self.__llave][self.imgP.value()]
        ds = pydicom.dcmread("images/"+ self.__llave+"/"+x)
        self.info.setPlainText("|Peso: " + str(ds[0x0010,0x1030].value)+"|"+ " |ID:"+str(ds[0x0010,0x0020].value)+"| |Intensidad del campo magnético(T): "+str(ds[0x0018,0x0087].value)+"| |Sexo: "+str(ds[0x0010,0x0040].value)+"| |Examen: "+str(ds[0x0018,0x0015].value)+"|")
        pixel_data = ds.pixel_array
        plt.imshow(pixel_data, cmap = plt.cm.bone)
        plt.axis('off')
        plt.savefig("temp_image.png")
        pixmap = QPixmap("temp_image.png")
        self.img.setPixmap(pixmap)
        os.remove('temp_image.png')
        pass