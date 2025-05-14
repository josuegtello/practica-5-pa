from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLineEdit,QFileDialog,QLayoutItem,QWidget,QScrollArea,QLabel,QPlainTextEdit
from PySide6.QtGui import QCursor,QIcon, QPixmap
from window_ui import *
import sys
import os
import json

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
    #Removemos la barra de titulo del sistema
        self.setWindowFlag(Qt.FramelessWindowHint)
        self._drag_pos = None
    #Signals Generales de la ventana
        self.closeWindowBtn.clicked.connect(self.closeWindow)
        self.minimizeWindowBtn.clicked.connect(self.minimizeWindow)
        self.maximizeWindowBtn.clicked.connect(self.maximizeWindow)
        #Obtenemos todos los botones
        self.buttons=self.findChildren(QPushButton)
        #Hacemos que todos los botones el cursor tome la forma de mano
        for btn in self.buttons:
            btn.setCursor(QCursor(Qt.PointingHandCursor))
    #Signals de Left Menu
        #minimizar o ampliar el menu
        self.openMenuBtn.clicked.connect(self.openMenu)
        #Filtramos los botones del left menu
        #Botones de Cambio de Pagina
        leftMenuBtns=self.querySelectorAll(self.buttons,"page-index")
        #Asignamos el mismo evento a los botones
        for btn in leftMenuBtns:
            btn.clicked.connect(self.changePage)
    
#Metodos de Window
    #Botones de Window
    def minimizeWindow(self):
        self.showMinimized()
    def maximizeWindow(self):
        btn=self.sender()
        state=btn.property("state")
        if state == "maximized": #Disminuimos el tamaño de la pantalla
            btn.setProperty("state","normal")
            btn.setIcon(QIcon("./media/icons/fullscreen_exit.svg"))
            self.showMaximized()
        elif state == "normal": #Aumentamos el tamaño de la pantalla
            btn.setProperty("state","maximized")
            btn.setIcon(QIcon("./media/icons/fullscreen.svg"))
            self.showNormal()
    def closeWindow(self):
        self.close() 
    #Renombramos los metodos para poder arrastrar la ventana Window de nuestra aplicacion
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if self._drag_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()
    def mouseReleaseEvent(self, event):
        self._drag_pos = None  
#Metodos del left Menu
    def openMenu(self):
        target=self.sender()
        state=target.property("state")
        buttonsMenu=self.querySelectorAll(self.buttons,"btn-menu")
        value=""
        if state == "opened":
            self.leftMenu.setMaximumWidth(55)
            #self.homeBtn.setMinimumSize(0,0)
            value="closed"
        elif state == "closed":
            self.leftMenu.setMaximumWidth(250)
            #self.homeBtn.setMinimumSize(150,0)
            value="opened"
        target.setProperty("state",value)
        #Actualizamos una propiedad de los botones
        for btn in buttonsMenu:
            vl=btn.property("menu-state")
            btn.setProperty("menu-state",value)
            # Forzar actualización del QSS
            self.updateStyles(btn)
    def changePage(self):
        target=self.sender() #Obtenemos el que origina el Signal
        index=int(target.property("page-index")) #Obtenemos el index de la pagina a la que queremos cambiar
        self.pages.setCurrentIndex(index) #Cambiamos de posicion el QStackedWidget
        print("cambiando pagina",index)
        buttonsMenu=self.querySelectorAll(self.buttons,"btn-menu")
        for btn in buttonsMenu:
            if btn == self.openMenuBtn: continue #me salto la iteracion ya que es el menu de hamburgesas
            if btn == target:
                btn.setProperty("state","selected")
            else:
                btn.setProperty("state","not selected")
            self.updateStyles(btn)
#Metodos Generales
    #Metodo que actualiza los estilos QSS de un contenedor de Qt
    def updateStyles(self,widget):
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()
    #Metodo para limpiar en Scrroll Area
    def clearScrollArea(self, scrollArea:QScrollArea):
        container = scrollArea.widget()
        layout = container.layout()

        if layout is None:
            return

        while layout.count():
            item = layout.takeAt(0)

            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()  # elimina el widget visual y de memoria  
    #Metodo similar a querySelectorAll en JS, me regresa los elementos que tienen esta propiedad
    def querySelectorAll(self,widgets,filter:str):
        elements=[]
        for wd in widgets:
            property_value=wd.property(filter)
            if property_value is not None:
                elements.append(wd)
        return elements #if len(elements)>1 else None
    #Metodo similar a querySelector en JS, me regresa el primer elemento que tiene esta propiedad
    def querySelector(self,parent,widget,filter:str):
        elements=parent.findChildren(widget)
        for el in elements:
            value=el.property(filter)
            if value is not None:
                return el
        return None #si no encuentra nada que retorna None
    #Metodo similar a el de JS, me permite crear un JSON en formato string a traves de un diccionario
    def stringify(data: dict) -> str | None:
        try:
            return json.dumps(data)
        except (TypeError, ValueError) as e:
            print(f"Error al convertir a string: {e}")
            return None
    #Metodo similar a el de JS, me permite obtenener un diccionario a traves de un JSON en formato string
    def parse(data: str) -> dict:
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            print(f"Error al convertir a diccionario: {e}")
            return None
    #Metodo que me permite leer archivos JSON a partir de diccionarios
    def readJSON(self,source:str) -> dict | None:
        try:
            if not os.path.exists(source):
                print(f"Archivo no encontrado: {source}")
                return None

            with open(source, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, IOError) as e:
            print(f"Error al leer el archivo JSON: {e}")
            return None
    #Metodo que me permite generar archivos JSON a partir de diccionarios
    def writeJSON(self,source:str,data:dict | list) -> bool:
        try:
            with open(source, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("Archivo guardado exitosamente.")
            return True
        except (PermissionError, FileNotFoundError) as e:
            print(f"Error de archivo: {e}")
            return False
        except TypeError as e:
            print(f"Error al serializar JSON: {e}")
            return False
        except Exception as e:
            print(f"Otro error inesperado: {e}")
            return False
    #Metodo que me permite eliminar archivos
    def deleteFile(self,source:str) -> bool:
        if os.path.exists(source) and os.path.isfile(source):
            try:
                os.remove(source)
                return True
            except OSError as e:
                print(f"Error al eliminar el archivo: {e}")
                return False
        else:
            return False
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())