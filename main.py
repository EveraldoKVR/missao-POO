
from produtos import FuncionarioCLT, FuncionarioPJ, Produto, ProdutoImportado, ProdutoNacional

produtos =[
        ProdutoNacional('Teclado', 100.0, 20),
        ProdutoNacional('Mouse', 50.0, 15),
        ProdutoImportado('Notebook', 2700.0, 5, 0.15),
        ProdutoImportado('Headset Gamer', 260.0, 10, 0.15)  
    ]
    
funcionarios = [
        FuncionarioCLT('João', 3000.0),
        FuncionarioPJ('Maria', 160, 25.0),
        FuncionarioCLT('José', 2600.0)        
        
    ]
    
# Relatório de produtos
print('\n' + '='*50)
print('RELATÓRIO DE PRODUTOS'.center(50))
print('='*50)
for produto in produtos:
    produto.exibir_detalhes()
    produto.emitir_nota()
    print('-'*50)

# Operações de estoque
print('\n' + '='*50)
print('OPERAÇÕES DE ESTOQUE'.center(50))
print('='*50)
produtos[0].vender(3)     
produtos[2].vender(10)      
produtos[1].repor(15)      
produtos[3].vender(2)       

# Folha de pagamento
print('\n' + '='*50)
print('FOLHA DE PAGAMENTO'.center(50))
print('='*50)
total_folha = 0
for func in funcionarios:
    pagamento = func.calcular_pagamento()
    print(f'{func.nome}  Pagamento: R${pagamento:.2f}')
    total_folha += pagamento
print(f'\nTOTAL DA FOLHA: R${total_folha:.2f}')

# Resumo financeiro
print('\n' + '='*50)
print('RESUMO FINANCEIRO'.center(50))
print('='*50)
total_estoque = sum(p.preco_final() * p.estoque for p in produtos)
print(f'\nValor total em estoque: R${total_estoque:.2f}')
print(f'\nTotal da folha de pagamento: R${total_folha:.2f}\n')

