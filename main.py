#importando a classe Produtos
from produto import Produto

# passando os valores para os atributos da classe Produto dentro da variavel produto_1
produto_1 = Produto("Teclado", 100.0, 20)
# chamando o método exibir detalhes com os atributos inseridos para o produto_1
produto_1.exibir_detalhes()