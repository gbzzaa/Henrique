from abc import ABC, abstractmethod
from datetime import date

# Classe abstrata: nenhum "Produto" genérico pode ser criado,
# só Celular, Notebook ou Acessorio (que vêm depois).
class Produto(ABC):

    def __init__(self, nome, preco, quantidade, data_entrada):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        self._data_entrada = data_entrada

    # encapsulamento: atributos "escondidos" (_nome, _preco...)
    # acessados por fora com @property
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = novo_preco

    @property
    def quantidade(self):
        return self._quantidade

    def meses_em_estoque(self):
        hoje = date.today()
        return (hoje.year - self._data_entrada.year) * 12 + (hoje.month - self._data_entrada.month)

    # métodos abstratos: toda categoria é OBRIGADA a criar sua própria versão
    @abstractmethod
    def detalhes_tecnicos(self):
        pass

    @abstractmethod
    def calcular_garantia(self):
        pass


# Mixin = uma "classe extra" com uma regra que pode ser somada a outras classes.
# Aqui: regra de promoção (mais de 6 meses parado -> 20% de desconto)
class Promocao:

    def em_promocao(self):
        return self.meses_em_estoque() > 6

    def preco_com_promocao(self):
        if self.em_promocao():
            return self.preco * 0.8   # 20% de desconto
        return self.preco


# Mixin da regra exclusiva de notebook: desconto de estudante
class DescontoEstudante:

    def preco_com_desconto_estudante(self, preco_base, eh_estudante):
        if eh_estudante:
            return preco_base * 0.95   # 5% de desconto
        return preco_base
