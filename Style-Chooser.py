import sys
from PyQt4 import QtGui
from PyQt4 import QtCore



def setStyleHelper(widget, style):
        widget.setStyle(style)
        widget.setPalette(style.standardPalette())
        for child in widget.children():
            if isinstance(child, QtGui.QWidget):
                setStyleHelper(child, style)

def change_style(widget, style):
    style=QtGui.QStyleFactory.create(style)
    if style: setStyleHelper(widget, style)



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupActions()
        self.setupMenus()
        self.setupUi()


    def change_stylecleanlooks(self): change_style(app, 'cleanlooks')
    def change_styleplastique(self): change_style(app, 'plastique')
    def change_stylecde(self): change_style(app, 'cde')
    def change_stylemotif(self): change_style(app, 'motif')
    def change_stylewindowsvista(self): change_style(app, 'windowsvista')


    def setupActions(self):

        # scale mode
        self.scale_fitAction = QtGui.QAction(self.tr("Fit in view"), self)
        self.scale_scaleAction = QtGui.QAction(self.tr("Scale and crop"), self)
        self.scale_fitAction.setCheckable(True)
        self.scale_scaleAction.setCheckable(True)

        self.scaleGroup = QtGui.QActionGroup(self)
        self.scaleGroup.addAction(self.scale_fitAction)
        self.scaleGroup.addAction(self.scale_scaleAction)
        self.scale_fitAction.setChecked(True)

        # qt-styles
        self.style_plastiqueAction = QtGui.QAction(self.tr("Plastuique"), self)
        self.style_cleanlooksAction = QtGui.QAction(self.tr("Cleanlooks"), self)
        self.style_cdeAction = QtGui.QAction(self.tr("cde"), self)
        self.style_motifAction = QtGui.QAction(self.tr("motif"), self)
        self.style_windowsvistaAction = QtGui.QAction(self.tr("windowsvista"), self)

        self.style_plastiqueAction.setCheckable(True)
        self.style_cleanlooksAction.setCheckable(True)
        self.style_cdeAction.setCheckable(True)
        self.style_motifAction.setCheckable(True)
        self.style_windowsvistaAction.setCheckable(True)

        self.styleGroup = QtGui.QActionGroup(self)
        self.styleGroup.addAction(self.style_plastiqueAction)
        self.styleGroup.addAction(self.style_cleanlooksAction)
        self.styleGroup.addAction(self.style_cdeAction)
        self.styleGroup.addAction(self.style_motifAction)
        self.styleGroup.addAction(self.style_windowsvistaAction)
        self.style_cleanlooksAction.setChecked(True)
        self.style_plastiqueAction.setChecked(True)
        self.style_cdeAction.setChecked(True)
        self.style_motifAction.setChecked(True)
        self.style_windowsvistaAction.setChecked(True)

        # style conns
        self.connect(self.style_plastiqueAction, QtCore.SIGNAL('triggered()'), self.change_styleplastique)
        self.connect(self.style_cleanlooksAction, QtCore.SIGNAL('triggered()'), self.change_stylecleanlooks)
        self.connect(self.style_cdeAction, QtCore.SIGNAL('triggered()'), self.change_stylecde)
        self.connect(self.style_motifAction, QtCore.SIGNAL('triggered()'), self.change_stylemotif)
        self.connect(self.style_windowsvistaAction, QtCore.SIGNAL('triggered()'), self.change_stylewindowsvista)


    def setupMenus(self):
        styleMenu = self.menuBar().addMenu(self.tr("Style"))
        styleMenu.addAction(self.style_cleanlooksAction)
        styleMenu.addAction(self.style_plastiqueAction)
        styleMenu.addAction(self.style_cdeAction)
        styleMenu.addAction(self.style_motifAction)
        styleMenu.addAction(self.style_windowsvistaAction)

    def setupUi(self):
        bar = QtGui.QToolBar()
        mainLayout = QtGui.QVBoxLayout()
        widget = QtGui.QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)
        self.setWindowTitle("styler")


if __name__ == '__main__':
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    change_style(app, "cleanlooks")
    window = MainWindow()
    window.show()
    app.exec_()
