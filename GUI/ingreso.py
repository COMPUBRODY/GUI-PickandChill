from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from producto import Producto


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #DEFINICIONES DEL MARCO
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 30, 401, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #DEFINICIONES DE LA ETIQUETA CODIGO
        self.CodigoLabel = QtWidgets.QLabel(self.frame)
        self.CodigoLabel.setGeometry(QtCore.QRect(70, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CodigoLabel.setFont(font)
        self.CodigoLabel.setObjectName("CodigoLabel")
        #DEFINICIONES DE LA LINEA DE TEXTO DEL CODIGO
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        #DEFINICIONES DE LA RULETA DE CANTIDAD
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(80, 110, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(12)
        self.spinBox.setObjectName("Ruleta_Cantidad")
        #DEFINICIONES ETIQUETA CANTIDAD
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #DEFINICIONES DEL BOTON DE INGRESO
        self.BotonIngreso = QtWidgets.QPushButton(self.frame)
        self.BotonIngreso.setGeometry(QtCore.QRect(130, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        self.BotonIngreso.setFont(font)
        self.BotonIngreso.setObjectName("BotonIngreso")
        #DEFINICIONES DEL TITULO: INGRESO DE PRODUCTO
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 0, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionBASE = QtWidgets.QAction(MainWindow)
        self.actionBASE.setObjectName("actionBASE")
        self.menuFile.addAction(self.actionBASE)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CodigoLabel.setText(_translate("MainWindow", "Codigo"))
        self.label_2.setText(_translate("MainWindow", "Cantidad"))
        self.BotonIngreso.setText(_translate("MainWindow", "INGRESO"))
        self.label.setText(_translate("MainWindow", "INGRESO DE PRODUCTO"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionBASE.setText(_translate("MainWindow", "BASE"))
        #CODIGO ESCRITO
        self.BotonIngreso.clicked.connect(self.Ingreso_Boton)

        #FUNCION PARA MENSAJE CADA QUE SE PRESIONE EL BOTON
    def Ingreso_Boton(self):

        texto_codigo = self.lineEdit.text()
        cantidad_producto = self.spinBox.text()
        if not texto_codigo:
            print('no hay nada para ingresar')
            QMessageBox.warning(MainWindow, 'ALERTA!', 'Ingresa un Codigo de Producto')
        elif cantidad_producto=='0':
            print('no hay nada para ingresar')
            QMessageBox.warning(MainWindow, 'ALERTA!', 'Ingresa una Cantidad')
        else:
            prod = Producto(texto_codigo, cantidad_producto)
            prod.asignar_Codigo()
            if prod.nombre=='null':
                QMessageBox.warning(MainWindow, 'ALERTA!', 'El Producto no Existe!')
            else:
                prod.define_fechas()
                prod.asignar_lugar()
                QMessageBox.information(MainWindow, 'INFORMACION!', 'Se Ingreso Producto')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
