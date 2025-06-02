#importando a classe Produto, e as subclasses ProdutoNacional e ProdutoInportado
from produto import Produto, ProdutoImportado, ProdutoNacional

# passando os valores para os atributos da classe Produto dentro da variavel produto_1 e exibindo através do método exibir_detalhes
produto_1 = Produto('Teclado', 100.0, 20)
produto_1.exibir_detalhes()
produto_1.emitir_nota()
# teste de estoque para produto
produto_1.vender(3)
produto_1.vender(21) # venda vai dar errado
produto_1.repor(15)
# passando os valores para os atributos da subclasse produto nacional e importado e exibindo os detalhes usando o método exibir_detalhes
produto_nacional_1 = ProdutoNacional('Mouse', 50.0, 15)
produto_nacional_1.exibir_detalhes()
produto_nacional_1.emitir_nota()
# teste de estoque produto nacional
produto_nacional_1.vender(10)
produto_nacional_1.vender(20)# venda vai dar errado
produto_nacional_1.repor(30)
# passando os valores para os atributos da subclasse produto importado e importado e exibindo os detalhes usando o método exibir_detalhes
produto_importado_1 = ProdutoImportado('Notebook', 5000.0, 5, 0.15)
produto_importado_1.exibir_detalhes()
produto_importado_1.emitir_nota()
#teste de estoque produto importado
produto_importado_1.vender(1)
produto_importado_1.vender(10)# venda vai dar errado
produto_importado_1.repor(6)

