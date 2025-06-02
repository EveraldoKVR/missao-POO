# criando a classe produtos
class Produto:
    # definição do método construtor da classe e seus atributos
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    # definição do método exibir detalhes 
    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} unidades")

