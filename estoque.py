class Estoque:

    def __init__(self):
        self._produtos = []   # lista com todos os produtos

    def adicionar(self, produto):
        self._produtos.append(produto)

    def listar_todos(self):
        return self._produtos

    def listar_em_promocao(self):
        # só produtos que tem o método em_promocao (herdaram de Promocao)
        return [p for p in self._produtos if p.em_promocao()]
