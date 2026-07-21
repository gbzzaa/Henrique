from produto import Produto, Promocao, DescontoEstudante

# Notebook herda de 3 classes ao mesmo tempo -> herança múltipla
class Notebook(Produto, Promocao, DescontoEstudante):

    def __init__(self, nome, preco, quantidade, processador, data_entrada):
        super().__init__(nome, preco, quantidade, data_entrada)
        self._processador = processador

    def detalhes_tecnicos(self):
        return f"Notebook com processador {self._processador}"

    def calcular_garantia(self):
        return 18   # meses

    def preco_final(self, eh_estudante=False):
        preco = self.preco_com_promocao()
        return self.preco_com_desconto_estudante(preco, eh_estudante)
