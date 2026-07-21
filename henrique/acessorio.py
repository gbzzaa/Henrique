from produto import Produto, Promocao

class Acessorio(Produto, Promocao):

    def __init__(self, nome, preco, quantidade, tipo, data_entrada):
        super().__init__(nome, preco, quantidade, data_entrada)
        self._tipo = tipo

    def detalhes_tecnicos(self):
        return f"Acessório do tipo {self._tipo}"

    def calcular_garantia(self):
        return 3   # meses
