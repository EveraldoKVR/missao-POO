# criando a classe produtos
class Produto:
    # definição do método construtor da classe e seus atributos
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    # definição do método exibir detalhes 
    def exibir_detalhes(self):
        print(f'\nProduto: {self.nome}\n Preço: R${self.preco:.2f}\n Estoque: {self.estoque} unidades\n' )

# criando a subclasse produto nacional e definindo seus atributos
class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)
# criando a subclasse produto importado e definindo seus atributos
class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao
    def exibir_detalhes(self):
        print(f'\nProduto: {self.nome}\n Preço: R${self.preco:.2f}\n Estoque: {self.estoque} unidades \nTaxa de importação: {self.taxa_importacao}\n' )

