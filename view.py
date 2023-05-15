import os.path
from controller import ControllerEstoque, ControllerCategoria, ControllerCliente, ControllerFuncionario, ControllerVenda

def criarArquivos(*nomes):
    for i in nomes:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")

criarArquivos("db/categoria.txt", 'db/clientes.txt', "db/estoque.txt", "db/fornecedor.txt", "db/funcionarios.txt",
              "db/venda.txt")

while True:
    print(" {0} \n|{1:^30}|\n {0} ".format(30*'-',"Menu Incial"))
    print("|{1:30}|\n|{2:30}|\n|{3:30}|\n|{4:30}|\n|{5:30}|\n|{6:30}|\n|{7:30}|\n {0} ".format
          (30*"-","1 - Estoque","2 - Categoria", "3 - Cliente","4 - Funcionario", "5 - Caixa",'6 - Relatorios',"0 - Sair"))
    op_menuInical = int(input("Digite a opção: "))
    if op_menuInical == 0:
        break
    if op_menuInical == 1:
        while True:
            print(" {0} \n|{1:^30}|\n {0} ".format(30*'-',"Menu Estoque"))
            print("|{0:30}|\n|{1:30}|\n|{2:30}|\n|{3:30}|\n {4} ".format('1 - Ver Estoque', "Cadastrar Produto", 
                                                        "3 - Editar Produto", "4 - Deletar Produto", "0 - Voltar", 30*'-'))
            op_estoque = int(input("Digite a opção: "))
            if op_estoque == 0:
                break
            if op_estoque == 1:
                print("\n\n\n")
                ControllerEstoque.ver_estoque()
                input("Digite enter para fechar...")
                print("\n\n\n")
            if op_estoque == 2:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Cadastrar Produto"))
                ControllerEstoque.cadastrar(input("Nome: "), input("Categoria: "), float(input("Valor: ")), int(input("Quantidade: ")))
            if op_estoque == 3:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Editar Produto"))
                nomeAlterar = input("Digite o nome do produto: ")
                ControllerEstoque.editar(nomeAlterar, input("Digite o novo nome: "), input("Digite a Categoria: "), float(input("Digite o valor: ")),
                                         int(input("Digite a quantidade")))
            if op_estoque == 4:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Deletar Produto"))
                nomeProduto = input("Digite o nome do produto: ")
                ControllerEstoque.deletar(nomeProduto)
                
    if op_menuInical == 2:
        while True:
            print(" {0} \n|{1:^30}|\n {0} ".format(29*'-',"Menu Categoria"))
            print("|{0:30}|\n|{1:30}|\n|{2:30}|\n|{3:30}|\n|{4:30}|\n {5} ".format('1 - Ver Categoria', "2 - Cadastrar Categoria",
                                                        "3 - Alterar Categoria", "4 - Deletar Categoria",
                                                        "0 - Voltar", 30*'-'))
            op_categoria = int(input("Digite a opção: "))
            if op_categoria == 0:
                break

            if op_categoria == 1:
                print("\n\n\n\n")
                ControllerCategoria.ver_categoria()
                input("Digite enter para fechar...")
                print("\n\n")
            if op_categoria == 2:
                print("\n\n|{0:^20}|".format("Cadastrar Categoria"))
                nomeCategoria = input(("Nome: "))
                ControllerCategoria.cadastrar(nomeCategoria)
                    
            if op_categoria == 3:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Alterar Categoria"))
                ControllerCategoria.editar(input("Digite o nome da categoria que deseja editar: "), input("Digite o novo nome da categoria: "))
                
            if op_categoria == 4:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Deletar Categoria"))
                ControllerCategoria.deletar(input("Digite o nome da categoria: "))
        
    if op_menuInical == 3:
        while True:
            print(" {0} \n|{1:^30}|\n {0} ".format(29*'-',"Menu Cliente"))
            print("|{0:30}|\n|{1:30}|\n|{2:30}|\n|{3:30}|\n|{4:30}|\n {5} ".format('1 - Ver Clientes', "2 - Cadastrar Cliente",
                                                            "3 - Alterar Cliente", "4 - Deletar Cliente",
                                                            "0 - Voltar", 30*'-'))
            op_cliente = int(input("Digite a opção: "))
            if op_cliente == 0:
                    break

            if op_cliente == 1:
                print("\n\n\n\n")
                ControllerCliente.ver_clientes()
                input("Digite enter para fechar...")
                print("\n\n")
            if op_cliente == 2:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Cadastrar Cliente"))
                ControllerCliente.cadastrar(input("Nome: "), input("Telefone: "), input("cpf: "), input("E-mail: "), input("Endereco: "))
                
            
            if op_cliente == 3:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Editar Cliente"))
                nomeAlterar = input("Digite o nome do cliente: ")
                ControllerCliente.editar(nomeAlterar, input("Novo nome: "), input("Telefone: "), input("cpf: "), input("E-mail: "), input("Endereço: "))
                
            if op_cliente == 4:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Deletar Cliente"))
                ControllerCliente.deletar(input("Digite o nome do cliente: "))
                
    if op_menuInical == 4:
        while True:
            print(" {0} \n|{1:^30}|\n {0} ".format(29*'-',"Menu Funcionario"))
            print("|{0:30}|\n|{1:30}|\n|{2:30}|\n|{3:30}|\n|{4:30}|\n {5} ".format('1 - Ver Funcionarios', "2 - Cadastrar Funcionario",
                                                            "3 - Alterar Funcionario", "4 - Deletar Funcionario",
                                                            "0 - Voltar", 30*'-'))
            op_funcionario = int(input("Digite a opção: "))
            if op_funcionario == 0:
                    break
            if op_funcionario == 1:
                print("\n\n\n\n")
                ControllerFuncionario.ver_funcionario()
                input("Digite enter para fechar...")
                print("\n\n")

            if op_funcionario == 2:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Cadastrar Funcionario"))
                ControllerFuncionario.cadastrar(input("clt: "), input("Nome: "), input("Telefone: "), input("cpf: "), input("E-mail: "), input("Endereço: "))
            
            if op_funcionario == 3:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Editar Funcionario"))
                ControllerFuncionario.editar(input("Digite o nome do funcionario: "), input("clt: "), input("Nome: "), input("Telefone: "), input("cpf: "), input("E-mail: "), input("Endereço: "))
                
            if op_funcionario == 4:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Deletar Funcionario"))
                ControllerFuncionario.deletar(input("Digite o nome do funcionario: "))

    if op_menuInical == 5:
        while True:
            print(" {0} \n|{1:^30}|\n {0} ".format(29*'-',"Caixa"))
            print("|{0:30}|\n|{1:30}|\n {2} ".format('1 - Realizar Venda', "0 - Voltar", 30*'-'))
            op_caixa = int(input("Digite a opção: "))
            if op_caixa == 0:
                break
            if op_caixa == 1:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Venda"))
                ControllerVenda.cadastrar(input("Nome do produto: "), input("Vendedor: "),input("Comprador: "), int(input("Quantidade: ")))
    
    if op_menuInical == 6:
        while True:
            print(" {0} \n|{1:^30}|\n {0} ".format(29*'-',"Relatorios"))
            print("|{0:30}|\n|{1:30}|\n|{2:30}|\n|{3:30}|\n|{4:30}|\n {5} ".format('1 - Relatorio Geral', "2 - Relatorio por Data",
                                                                "3 - Relatorio de Periodo", "4 - Relatorio de Produto",
                                                                "0 - Voltar", 30*'-'))
            op_relatorio = int(input("Digite a opção: "))
            if op_relatorio == 0:
                break
            if op_relatorio == 1:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Relatorio Geral"))
                ControllerVenda.relatorio_geral()
                input("Aperte enter para fechar...")
                print("\n\n\n")
            if op_relatorio == 2:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Relatorio por Data"))
                ControllerVenda.relatorio_parcial_data(input("Digite uma data: "))
                input("Aperte enter para fechar...")
                print("\n\n\n")
            if op_relatorio == 3:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Relatorio Periodo"))
                ControllerVenda.relatorio_periodo(input("Digite a data inicial: "),input("Digite a data Final: "))
                input("Aperte enter para fechar...")
                print("\n\n\n")
            if op_relatorio == 4:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Relatorio Periodo"))
                ControllerVenda.relatorio_parcial_produto(input("Digite o nome do produto: "))
                input("Aperte enter para fechar...")
                print("\n\n\n")