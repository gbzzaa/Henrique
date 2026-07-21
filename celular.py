from produto import Produto, Promocao

class Celular(Produto, Promocao):

    def __init__(self, nome, preco, quantidade, marca, data_entrada):
        super().__init__(nome, preco, quantidade, data_entrada)
        self._marca = marca

    def detalhes_tecnicos(self):
        return f"Celular da marca {self._marca}"

    def calcular_garantia(self):
        return 12   # meses
