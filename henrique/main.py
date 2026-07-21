from datetime import date, timedelta

from celular import Celular
from notebook import Notebook
from acessorio import Acessorio
from estoque import Estoque

estoque = Estoque()

hoje = date.today()
ha_8_meses = hoje - timedelta(days=8 * 30)   # simula produto parado há 8 meses
ha_2_meses = hoje - timedelta(days=2 * 30)

celular = Celular("iPhone 17", 3500, 5, "Apple", ha_8_meses)
notebook = Notebook("Dell Inspiron", 4200, 3, "Intel i9", ha_8_meses)
acessorio = Acessorio("Capinha", 40, 20, "Capinha", ha_2_meses)

estoque.adicionar(celular)
estoque.adicionar(notebook)
estoque.adicionar(acessorio)

print("=== GARANTIA DE CADA PRODUTO (calculada automaticamente) ===")
for produto in estoque.listar_todos():
    print(f"{produto.nome} -> {produto.detalhes_tecnicos()} -> garantia de {produto.calcular_garantia()} meses")

print()
print("=== PRODUTOS EM PROMOÇÃO (mais de 6 meses parados) ===")
for produto in estoque.listar_em_promocao():
    print(f"{produto.nome}: de R${produto.preco} por R${produto.preco_com_promocao():.2f}")

print()
print("=== DESCONTO DE ESTUDANTE (só existe em Notebook) ===")
print(f"Preço normal: R${notebook.preco_final():.2f}")
print(f"Preço com comprovante de estudante: R${notebook.preco_final(eh_estudante=True):.2f}")
