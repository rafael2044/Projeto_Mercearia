import os.path
from controller import ControllerEstoque, ControllerCategoria, ControllerCliente, ControllerFuncionario
from model import Categoria
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
          (30*"-","1 - Estoque", "2 - Produto","3 - Categoria", "4 - Cliente","5 - Funcionario", "6 - Vendas","0 - Sair", 30*'-'))
    op = int(input("Digite a opção: "))
    if op == 0:
        break
    if op == 1:
        while True:
            print(" {0} \n|{1:^30}|\n {0} ".format(30*'-',"Menu Estoque"))
            print("|{0:30}|\n|{1:30}|\n|{2:30}|\n|{3:30}|\n {4} ".format('1 - Ver Estoque', "2 - Incrementar Estoque", 
                                                        "3 - Decrementar Estoque", "0 - Voltar", 30*'-'))
            op_estoque = int(input("Digite a opção: "))
            if op_estoque == 0:
                break
            if op_estoque == 1:
                print("\n\n\n")
                ControllerEstoque.ver_estoque()
                input("Digite enter para fechar...")
                print("\n\n\n")
            if op_estoque == 2:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Incrementar Estoque"))
                index = ControllerEstoque.pesquisar(input("Digite o nome do produto que deseja aumentar o estoque: "))
                if index != -1:
                    ControllerEstoque.incrementar_estoque(index, int(input("Digite a quantidade que deseja incrementar: ")))
                else:
                    print("Falha ao incrementar estoque, produto não encontrado!")
    if op == 2:
        while True:
            print(" {0} \n|{1:^30}|\n {0} ".format(30*'-',"Menu Produto"))
            print("|{0:30}|\n|{1:30}|\n|{2:30}|\n|{3:30}|\n {4} ".format('1 - Cadastrar Produto', "2 - Alterar Produto",
                                                        "3 - Deletar Produto", "0 - Voltar", 30*'-'))
            op_produto = int(input("Digite a opção: "))
            if op_produto == 0:
                break
            
            if op_produto == 1:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Cadastrar Produto"))
                nome = input("Nome: ")
                categoria = input("Categoria: ")
                try:
                    valor = float(input("Valor: "))
                except ValueError as e:
                    valor = 0
                try:
                    quantidade = int(input("Digite a quantidade em estoque: "))
                except ValueError as e:
                    quantidade = 0
                print(f" {19*'-'} ")
                ControllerEstoque.cadastrar(nome, categoria, valor, quantidade)

            if op_produto == 2:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Alterar Produto"))
                id = int(input("Digite o id do produto: "))
                ControllerEstoque.editar(id, input("Digite o nome: "), input("Digite a Categoria: "), float(input("Digite o valor: ")),
                                         int(input("Digite a quantidade")))
            
            if op_produto == 3:
                print("\n\n {0} \n|{1:^20}|\n {0} ".format(19*"-" ,"Deletar Produto"))
                id = int(input("Digite o id do produto: "))
                ControllerEstoque.deletar(id)
                                                    
    if op == 3:
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
        
    if op == 4:
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
                while True:
                    nome = input("Nome: ")
                    if len(nome)>=3:
                        break
                    print("O nome invalido! Digite novamente")
                while True:
                    telefone = input("Telefone: ")
                    if len(telefone)==11:
                        break
                    print("Telefone invalido! Digite novamente.")
                while True:
                    cpf = input("cpf: ")
                    if len(cpf) == 11:
                        break
                    print("Cpf invalido! Digite novamente.")
                while True:
                    email = input("E-mail: ")
                    if len(email.split("@")) == 2:
                       break
                    print("Email Invalido! Digite novamente")
                while True:
                    endereco = input("Endereço: ")
                    if len(endereco) > 5:
                        break
                    print("Endereco invalido! Digite novamente.")

                if ControllerCliente.cadastrar(nome, telefone, cpf, email, endereco):
                    print("Cadastro realizado com Sucesso!")
                else:
                    print("Falha ao realizar cadastro!")
            if op_cliente == 3:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Editar Cliente"))
                index = ControllerCliente.pesquisar(input("Digite o id do cliente: "))
                if index != -1:
                    print("Realize a alteracao: ")
                    while True:
                        nome = input("Nome: ")
                        if len(nome)>=3:
                            break
                        print("O nome invalido! Digite novamente")
                    while True:
                        telefone = input("Telefone: ")
                        if len(telefone)==11:
                            break
                        print("Telefone invalido! Digite novamente.")
                    while True:
                        cpf = input("cpf: ")
                        if len(cpf) == 11:
                            break
                        print("Cpf invalido! Digite novamente.")
                    while True:
                        email = input("E-mail: ")
                        if len(email.split("@")) == 2:
                            break
                        print("Email Invalido! Digite novamente")
                    while True:
                        endereco = input("Endereço: ")
                        if len(endereco)>5:
                            break
                        print("O endereco invalido! Digite novamente.")

                    if ControllerCliente.editar(index, nome, telefone, cpf, email, endereco):
                        print("Alteracoes realizadas com sucesso!")
                    else:
                        print("Falha na alteracao, os dados nao foram preenchidos corretamente!")
                else:
                    print("Falha ao realizar alteracao, o cliente nao foi encontrado!")
            if op_cliente == 4:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Deletar Cliente"))
                index = ControllerCliente.pesquisar(input("Digite o id do cliente: "))
                if index != -1:
                    ControllerCliente.deletar(index)
                    print("Cliente deletado com sucesso!")
                else:
                    print("Falha ao tentar deletar, cliente nao encontrado!")
    if op == 5:
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
                clt = input("clt (sim/não): ")
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                cpf = input("cpf: ")
                email = input("E-mail: ")
                endereco = input("Endereço: ")
                if ControllerFuncionario.cadastrar(clt, nome, telefone, cpf, email, endereco):
                    print("Cadastro realizado com Sucesso!")
                else:
                    print("Falha ao realizar cadastro!")
            if op_funcionario == 3:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Editar Funcionario"))
                index = ControllerFuncionario.pesquisar_id(input("Digite o id do funcionario: "))
                if index != -1:
                    print("Realize as alteracoes: ")
                    clt = input("clt (sim/não): ")
                    nome = input("Nome: ")
                    telefone = input("Telefone: ")
                    cpf = input("cpf: ")
                    email = input("E-mail: ")
                    endereco = input("Endereço: ")
                    if ControllerFuncionario.editar(index, clt, nome, telefone, cpf, email, endereco):
                        print("Alteracoes realizadas com sucesso!")
                    else:
                        print("Falha na alteracao, os dados nao foram preenchidos corretamente!")
                else:
                    print("Falha ao realizar alteracao, o funcionario nao foi encontrado!")
            if op_funcionario == 4:
                print("\n\n\n {0} \n|{1:^20}|\n {0} ".format(20*'-',"Deletar Funcionario"))
                index = ControllerFuncionario.pesquisar_id(input("Digite o id do funcionario: "))
                if index != -1:
                    ControllerFuncionario.deletar(index)
                    print("Funcionario deletado com sucesso!")
                else:
                    print("Falha ao tentar deletar, funcionario nao encontrado!")