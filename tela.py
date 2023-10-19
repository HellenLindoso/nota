from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from moduloCadastrar import cadastrar
from converterData import converterData

class TelaDeCadastro(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregar = QUiLoader()
        self.tela = carregar.load("tela.ui")
        self.componentes()
    
    def componentes(self):
        self.caixaMovimentacao = self.tela.findChild(QtWidgets.QComboBox, "caixaMovimentacao")
        self.caixaDescricao = self.tela.findChild(QtWidgets.QLineEdit, "caixaDescricao")
        self.caixaValor = self.tela.findChild(QtWidgets.QLineEdit, "caixaValor")
        self.caixaCategoria = self.tela.findChild(QtWidgets.QComboBox, "caixaCategoria")
        self.caixaDataMovimentacao = self.tela.findChild(QtWidgets.QDateEdit, "caixaDataMovimentacao")
        self.botaoCadastrar = self.tela.findChild(QtWidgets.QPushButton, "botaoCadastrar")
        self.botaoCadastrar.clicked.connect(self.cadastrar)

    def cadastrar(self):
        movi = self.caixaMovimentacao.currentText()
        descr = self.caixaDescricao.text()
        valor = self.caixaValor.text()
        cate = self.caixaCategoria.currentText()
        dataP = self.caixaDataMovimentacao.text()
        cadastrar(movi, descr, valor, cate, converterData(dataP))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaDeCadastro()
    interface.tela.show()
    app.exec()