# importando o Abstract BAse 
from abc import ABC, abstractmethod

# criando a classe produtos
class Produto:
    # definição do método construtor da classe e seus atributos
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    # definição do método exibir detalhes 
    def exibir_detalhes(self):
        print(f'\nProduto: {self.nome}\n Preço: R${self.preco:.2f}\n Estoque: {self.estoque} unidades' )
    
    # definição do método emitir notas
    def emitir_nota(self):
        print(f'Nota Fiscal gerada para {self.nome}')
    
    # definição do método repor para reposição do estoque    
    def repor(self, quantidade):
        self.estoque += quantidade
        print(f'Reposição: {quantidade} unidades. Estoque atual: {self.estoque}' )
    
    # definição do método vender para saida de estoque por uma venda
    def vender(self, quantidade):
        if quantidade > self.estoque:
            print(f'Quantidade indisponível no estoque. \nQuantidade disponível {self.estoque} unidades.')
        else:
            self.estoque -= quantidade
            print(f'Venda realizada. \nEstoque atual: {self.estoque} unidades')
        
# criando a subclasse produto nacional e definindo seus atributos
class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)

# criando a subclasse produto importado e definindo seus atributos
class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao
        
    # definindo o método para o cálculo do preço final
    def preco_final(self):
        return self.preco + (self.preco * self.taxa_importacao)
    
    # definindo o método para exibição dos detalhes
    def exibir_detalhes(self):
        print(f'\nProduto: {self.nome}\n Preço: R${self.preco:.2f}\n Estoque: {self.estoque} unidades \nTaxa de importação: {self.taxa_importacao}\n' )
        print(f'Preço normal: R${self.preco:.2f}')
        print(f'Preço importado: R${self.preco_final():.2f}')


# criando a classe base abstrata Funcionario e definindo seus atributos
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        
    @abstractmethod
    def calcular_pagamento(self):
        pass

# criando a subclasse funcionario CLT e seus atributos
class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario
        
    # definindo o método para calcular o pagamento do funcionario CLT
    def calcular_pagamento(self):
        return self.salario
    
# criando a subclasse funcionario PJ e seus atributos 
class FuncionarioPJ(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
        
    # definindo o método para calcular o pagamento do funcionario PJ    
    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora