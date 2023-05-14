from DAO import DAOcliente, DAOfuncionario, DAOcategoria, DAOestoque, DAOvenda
from model import Cliente, Funcionario, Categoria, Produto, Estoque, Venda
from functools import reduce
from datetime import datetime

class ControllerCliente:
    @classmethod
    def cadastrar(cls, nome : str, telefone: str, cpf: str, email: str, endereco: str):
        if len(nome)>=3 and not(DAOcliente.verificar_nome(nome)):
            if len(telefone) == 11 and len(list(filter(lambda x: x.get_telefone() == telefone, cls.cliente))) == 0:
                if len(cpf) == 11 and len(list(filter(lambda x: x.get_cpf() == cpf, cls.cliente))) == 0:
                    if len(email.split("@")) == 2 and len(list(filter(lambda x: x.get_email() == email, cls.cliente))) == 0:
                        if len(endereco) > 5:
                            DAOcliente.salvar(Cliente(nome, telefone, cpf, email,endereco))
                            print("Cadastro realizado com sucesso!")
                        else:
                            print("O endereco deve conter no minimo 6 caracteres!")
                    else:
                        print("O email ja existe!")
                else:
                    print("O cpf ja existe!")
            else:
                print("Telefone ja existe!")
        else:
            print("Clinte ja possui um cadastro!")
        
    @classmethod
    def ver_clientes(cls):
        clientes = DAOcliente.ler()
        print(" {0} \n|{1:^10}|{2:30}|{3:^15}|{4:^15}|{5:^25}|{6:30}|\n {0} "
              .format(130*"-", "ID","NOME", "TELEFONE", "CPF", "E-MAIL", "ENDEREÇO"))
        for i in clientes:
            print("|{0:^10}|{1:30}|{2:15}|{3:15}|{4:25}|{5:30}|"
                  .format(i.get_id() ,i.get_nome(), i.get_telefone(), i.get_cpf(),
                          i.get_email(), i.get_endereco()))
        print(" {0} ".format(130*"-"))

    @classmethod
    def editar(cls, nomeAlterar,nomeAlterado, telefone, cpf, email, endereco):
        if len(nomeAlterado)>=3 and not(cls.pesquisar_nome(nomeAlterado)):
            if len(telefone) == 11 and len(list(filter(lambda x: x.get_telefone() == telefone, cls.cliente))) == 0:
                if len(cpf) == 11 and len(list(filter(lambda x: x.get_cpf() == cpf, cls.cliente))) == 0:
                    if len(email.split("@")) == 2 and len(list(filter(lambda x: x.get_email() == email, cls.cliente))) == 0:
                        if len(endereco) > 5:
                            DAOcliente.zerar()
                            cls.cliente = list(map(lambda x: Cliente(nomeAlterado, telefone, cpf, email, endereco) if x.get_nome() == nomeAlterar else x, cls.cliente))
                            for i in cls.cliente:
                                DAOcliente.salvar(i)
                            print("Alteracoes realizadas com sucesso!")
                        else:
                            print("O endereco deve conter no minimo 6 caracteres!")
                    else:
                        print("O email ja existe!")
                else:
                    print("O cpf ja existe!")
            else:
                print("Telefone ja existe!")
        else:
            print("Cliente ja possui um cadastro!")
    @classmethod
    def deletar(cls, nomeCliente):
        if cls.pesquisar_nome(nomeCliente):
            cls.cliente.remove(list(filter(lambda x: x.get_nome() == nomeCliente, cls.cliente))[0])
            DAOcliente.zerar()
            for i in cls.cliente:
                DAOcliente.salvar(i)
            print("Cliente removido com sucesso")
        else:
            print("Cliente nao encontrado!")

    @classmethod
    def pesquisar_nome(cls, nomeCliente):
        cls.cliente = DAOcliente.ler()
        cliente = list(filter(lambda x: x.get_nome() == nomeCliente, cls.cliente))
        if len(cliente) == 1:
            return True
        return False

class ControllerFuncionario:
    @classmethod
    def cadastrar(cls ,clt: str, nome: str, telefone: str, cpf: str, email: str,endereco: str):
        funcionarios = DAOfuncionario.ler()
        if clt == 'sim' or clt == 'nao':
            if len(nome)>=3 and not(DAOcliente.verificar_nome(nome)):
                if len(telefone) == 11 and len(list(filter(lambda x: x.get_telefone() == telefone, funcionarios))) == 0:
                    if len(cpf) == 11 and len(list(filter(lambda x: x.get_cpf() == cpf, funcionarios))) == 0:
                        if len(email.split("@")) == 2 and len(list(filter(lambda x: x.get_email() == email, funcionarios))) == 0:
                            if len(endereco) > 5:
                                DAOfuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                                print("Cadastro realizado com sucesso!")
                            else:
                                print("O endereco deve conter no minimo 6 caracteres!")
                        else:
                            print("O email ja existe!")
                    else:
                        print("O cpf ja existe!")
                else:
                    print("Telefone ja existe!")
            else:
                print("Funcionario ja possui um cadastro!")
        else:
            print("A clt so pode assumir o valor 'sim' ou 'nao'!")
    
    @classmethod
    def ver_funcionario(cls):
        funcionarios = DAOfuncionario.ler()
        print(" {0} \n|{1:^10}|{2:^10}|{3:^30}|{4:^15}|{5:^15}|{6:^25}|{7:50}|\n {0} "
              .format(160*"-", "ID", "CLT", "NOME", "TELEFONE", "CPF", "E-MAIL", "ENDEREÇO"))
        for i in funcionarios:
            print("|{0:10}|{1:10}|{2:30}|{3:15}|{4:15}|{5:25}|{6:50}|"
                  .format(i.get_id() ,i.get_clt() ,i.get_nome(), i.get_telefone(), i.get_cpf(),
                          i.get_email(), i.get_endereco()))
        print(" {0} ".format(160*"-"))
    
    @classmethod
    def editar(cls, index, clt, nome, telefone, cpf, email, endereco):
        if len(nome)>0 and len(telefone) == 11 and len(cpf) == 11 and len(email) > 0 and len(endereco) > 0:
            cls.funcionario[index] = Funcionario(clt, nome, telefone, cpf, email, endereco)
            DAOfuncionario.zerar()
            for i in cls.funcionario:
                DAOfuncionario.salvar(i)
            return True
        return False
    
    @classmethod
    def deletar(cls, index):
        cls.funcionario.pop(index)
        DAOfuncionario.zerar()
        for i in cls.funcionario:
            DAOfuncionario.salvar(i)

    @classmethod
    def pesquisar_nome(cls, nome):
        cls.funcionario = DAOfuncionario.ler()
        funcionario = list(filter(lambda x: x.get_nome() == nome, cls.funcionario))
        if len(funcionario) == 1:
            return True
        return False
    
    @classmethod
    def pesquisar_id(cls, id):
        cls.funcionario = DAOfuncionario.ler()
        for i in cls.funcionario:
            if i.get_id() == int(id):
                return cls.funcionario.index(i)
        return -1

class ControllerFornecedor:
    pass

class ControllerCategoria:
    @classmethod
    def cadastrar(cls, novaCategoria):
        if len(novaCategoria) > 4 and not DAOcategoria.verificar(novaCategoria):
            DAOcategoria.salvar(Categoria(novaCategoria))
            print("Categoria cadastrada com sucesso.\n\n")
        else:
            print("Falha ao cadastrar Categoria.\nERRO: Categoria ja existe.\n\n")
    
    @classmethod
    def editar(cls, categoriaAlterar, categoriaAlteracao):
        if cls.pesquisar(categoriaAlterar):
            if not DAOcategoria.verificar(categoriaAlteracao):
                if len(categoriaAlteracao) > 0:
                    cls.categoria = list(map(lambda x: Categoria(categoriaAlteracao) if x.get_nome().lower() == categoriaAlterar.lower() else x, DAOcategoria.ler()))
                    DAOcategoria.zerar()
                    for i in cls.categoria:
                        DAOcategoria.salvar(i)
                    print(f"Categoria {categoriaAlterar} alterada para {categoriaAlteracao} com sucesso!")
                else:
                    print("A nova categoria nao pode ser vazia!\n\n")
            else:
                print(f"A categoria {categoriaAlteracao} ja existe!\n\n")
        else:
            print(f"Categoria {categoriaAlterar} nao existe.\n\n")
    
    @classmethod
    def deletar(cls, categoriaDeletar):
        if cls.pesquisar(categoriaDeletar):
            cls.categoria.remove(list(filter(lambda x: x.get_nome().lower() == categoriaDeletar.lower(), cls.categoria))[0])
            DAOcategoria.zerar()
            for i in cls.categoria:
                DAOcategoria.salvar(i)
            estoque = DAOestoque.ler()
            DAOestoque.zerar()
            estoque = list(map(lambda x: Estoque(Produto(x.get_produto().get_nome(), Categoria(""), x.get_produto().get_valor()),
                                                 x.get_quantidade()) if x.get_produto().get_categoria().get_nome() == categoriaDeletar else x, estoque))
            print(estoque)
            for i in estoque:
                DAOestoque.salvar(i.get_produto(), i.get_quantidade())

            print("Categoria {} deletada com sucesso!\n\n".format(categoriaDeletar))
        else:
            print("Falha ao deletar categoria {}!\nERRO: categoria nao existe.".format(categoriaDeletar))
    
    @classmethod
    def ver_categoria(cls):
        cls.categoria = DAOcategoria.ler()
        print(f" {19*'-'} ")
        print("|{0:^20}|".format('Nome'))
        print(f" {19*'-'} ")
        for categoria in cls.categoria:
            print("|{0:20}|".format(categoria.get_nome()))
            print(f" {19*'-'} ")

    @classmethod
    def pesquisar(cls, nomeCategoria):
        cls.categoria = DAOcategoria.ler()
        categoria = list(filter(lambda x: x.get_nome().lower() == nomeCategoria.lower(), cls.categoria))
        if len(categoria) > 0:
            return True
        return False

class ControllerEstoque:
    @classmethod
    def cadastrar(cls, nome, categoria, valor:float, quantidade: int):
        if not DAOestoque.verificar(nome):
            if DAOcategoria.verificar(categoria):
                if valor > 0 and quantidade > 0:
                    DAOestoque.salvar(Produto(nome, Categoria(categoria), valor), quantidade)
                    print("Produto Cadastrado com sucesso!")
                else:
                    print("Preco ou quantidade invalidas.")
            else:
                print("Categoria nao existe!")
        else:
            print("O produto ja existe!")
       
    @classmethod
    def editar(cls, id:int, nome, categoria, valor:float, quantidade: int):
        if cls.pesquisar_id(id):
            if not cls.pesquisar_nome(nome):
                if DAOcategoria.verificar(categoria):
                    if len(nome)>4:
                        if valor>0 and quantidade > 0: 
                            cls.estoque = list(map(lambda x: Estoque(Produto(nome, categoria, valor), quantidade) if x.get_produto().get_id == id else x, cls.estoque))
                            DAOestoque.zerar()
                            for i in cls.estoque:
                                DAOestoque.salvar(i.get_produto(), i.get_quantidade())
                            print("Produto Alterado com sucesso!")
                        else:
                            print("Valor ou quantidade invalidos!")
                    else:
                        print("Nome invalido!")
                else:
                    print("Categoria nao existe!")
            else:
                print("O produto ja existe!")
        else:
            print("Id nao existe!")
    
    @classmethod
    def deletar(cls, id):
        if cls.pesquisar_id(id):
            cls.estoque.remove(list(filter(lambda x: x.get_produto().get_id() == id, cls.estoque))[0])
            DAOestoque.zerar()
            for i in cls.estoque:
                DAOestoque.salvar(i.get_produto(), i.get_quantidade())
            print("Produto deletado com sucesso!")
        else:
            print("Produto nao existe!")
    @classmethod
    def incrementar_estoque(cls, index, quantidade):
        cls.estoque[index].incrementar(quantidade)
        DAOestoque.zerar()
        for i in cls.estoque:
            DAOestoque.salvar(i.get_produto(), i.get_quantidade())

    @classmethod
    def decrementar_estoque(cls, id, quantidade):
        cls.estoque = DAOestoque.ler()
        cls.estoque = list(map(lambda x: Estoque(x.get_produto(), x.get_quantidade() - quantidade) if x.get_produto().get_id() == id else x, cls.estoque))
        cls.estoque = list(filter(lambda x: x.get_quantidade() > 0, cls.estoque))
        DAOestoque.zerar()
        for i in cls.estoque:
            DAOestoque.salvar(i.get_produto(), i.get_quantidade())
            
    @classmethod
    def quantidade_estoque(cls, nomeProduto):
        if cls.pesquisar_nome(nomeProduto):
            return cls.retorna_produto(nomeProduto).get_quantidade()
    @classmethod
    def ver_estoque(cls):
        cls.estoque = DAOestoque.ler()
        print(" {5} \n|{0:^10}|{1:^40}|{2:^20}|{3:^18}|{4:^15}|\n {5} ".format("ID",'NOME', 'CATEGORIA', 'VALOR', 'QUANTIDADE', 106*'-'))
        for i in cls.estoque:
            print("|{0:^10}|{1:40}|{2:20}|{3:>18}|{4:>15}|".format(i.get_produto().get_id(),i.get_produto().get_nome(), i.get_produto().get_categoria().get_nome(),
                                                            i.get_produto().get_valor(), i.get_quantidade()))
            print(f" {106*'-'} ")
    
    @classmethod
    def pesquisar_nome(cls, nomeProduto):
        cls.estoque = DAOestoque.ler()
        produto = list(filter(lambda x: x.get_produto().get_nome() == nomeProduto, cls.estoque))
        if len(produto) == 1:
                return True
        return False
    @classmethod
    def pesquisar_id(cls, idProduto):
        cls.estoque = DAOestoque.ler()
        produto = list(filter(lambda x: x.get_produto().get_id() == idProduto, cls.estoque))
        if len(produto) == 1:
            return True
        return False
    
    @classmethod
    def retorna_produto(cls, nomeProduto):
        if cls.pesquisar_nome(nomeProduto):
            return list(filter(lambda x: x.get_produto().get_nome() == nomeProduto, cls.estoque))[0]
        else:
            return None

class ControllerVenda:
    @classmethod
    def cadastrar(cls, nomeProduto, vendedor, comprador, quantidadeVendida: int):
        if ControllerEstoque.pesquisar_nome(nomeProduto):
            produto = ControllerEstoque.retorna_produto(nomeProduto)
            if ControllerFuncionario.pesquisar_nome(vendedor) and ControllerCliente.pesquisar_nome(comprador):
                if quantidadeVendida > 0 and ControllerEstoque.quantidade_estoque(nomeProduto) - quantidadeVendida >= 0:
                    DAOvenda.salvar(Venda(produto.get_produto(), vendedor, comprador, quantidadeVendida))
                    ControllerEstoque.decrementar_estoque(produto.get_produto().get_id(), quantidadeVendida)
                    print("Venda realizada com sucesso!")
                else:
                    print("Falha ao realizar Venda. quantidade invalida ou estoque baixo!")
            else:
                print("Comprador ou Vendedor nao cadastrados!")
        else:
            print("Produto informado nao existe!")
    @classmethod
    def relatorio_geral(cls):
        cls.vendas = DAOvenda.ler()
        relatorio = cls.pesquisa_geral()
        total = 0.0
        if relatorio is not None:
            print(" {0} \n|{1:^162}|".format(162*'-', "RELATORIO GERAL"))
            print(" {8} \n|{0:^30}|{1:^15}|{2:^10}|{3:^30}|{4:^30}|{5:^10}|{6:^15}|{7:^15}|\n {8} "
                .format('NOME PRODUTO','CATEGORIA', 'PRECO', 'VENDEDOR', 'COMPRADOR', 'QUANTIDADE', "DATA", "TOTAL", 162*'-'))
            for i in relatorio:
                print("|{0:30}|{1:15}|{2:^10}|{3:30}|{4:30}|{5:^10}|{6:^15}|{7:^15}|"
                    .format(i['produto'], i['categoria'], i['preco'],
                            i['vendedor'], i['comprador'], str(i['quantidade']), i['data'],
                            str(i['total'])))
                print(f" {162*'-'} ")
                total += i['total']
            print("|{2:>146}|{0:^15}|\n {1} ".format(str(total),162*'-',"TOTAL "))
        else:
            print("Nenhuma venda registrada")
    @classmethod
    def relatorio_parcial_data(cls, data):
        relatorio = cls.pesquisar_data(data)
        total = 0.0
        if relatorio is not None:
            print(" {0} \n|{1:^73}|".format(73*'-', "RELATORIO DATA: " + data))
            print(" {4} \n|{0:^30}|{1:^10}|{2:^15}|{3:^15}|\n {4} "
                .format('NOME PRODUTO', 'PRECO', 'QUANTIDADE', "TOTAL", 73*'-'))
            for i in relatorio:
                print("|{0:30}|{1:^10}|{2:^15}|{3:^15}|"
                        .format(i['produto'], str(i['preco']), str(i['quantidade']),str(i['total'])))
                print(f" {73*'-'} ")
                total += i['total']
            print("|{0:>57}|{1:^15}|\n {2} ".format("TOTAL ", str(total), 73*'-'))
        else:
            print("O existe nenhuma venda nesta data!")
    @classmethod
    def relatorio_periodo(cls, dataInicial, dataFinal):
        relatorio = cls.pesquisar_periodo(dataInicial, dataFinal)
        total = 0.0
        if relatorio is not None:
            print(" {0} \n|{1:^73}|".format(87*'-', "RELATORIO PERIODO: " + dataInicial + " - " + dataFinal))
            print(" {4} \n|{0:^30}|{1:^10}|{2:^15}|{3:^15}|{4:^15}|\n {4} "
                .format('NOME PRODUTO', 'PRECO', 'QUANTIDADE', 'DATA', "TOTAL", 89*'-'))
            for i in relatorio:
                print("|{0:30}|{1:^10}|{2:^15}|{3:^15}|{4:^15}|"
                        .format(i['produto'], str(i['preco']), str(i['quantidade']),i['data'],str(i['total'])))
                print(f" {89*'-'} ")
                total += i['total']
            print("|{0:>73}|{1:^15}|\n {2} ".format("TOTAL ", str(total), 89*'-'))
        else:
            print("O existe nenhuma venda nesta data!")
    @classmethod
    def relatorio_parcial_produto(cls, nomeProduto):
        relatorio = cls.pesquisar_produto(nomeProduto)
        if relatorio is not None:
            print(" {0} \n|{1:^73}|".format(73*'-', "RELATORIO PRODUTO: " + nomeProduto))
            print(" {4} \n|{0:^30}|{1:^10}|{2:^15}|{3:^15}|\n {4} "
                .format('NOME PRODUTO', 'PRECO', 'QUANTIDADE', "TOTAL", 73*'-'))
            print("|{0:30}|{1:^10}|{2:^15}|{3:^15}|"
                    .format(relatorio['produto'], str(relatorio['preco']), str(relatorio['quantidade']),str(relatorio['total'])))
            print(f" {73*'-'} ")
        else:
            print("O produto nao possui nenhuma venda ou nao existe em estoque!")
    @classmethod
    def pesquisar_data(cls, data):
        cls.vendas = DAOvenda.ler()
        vendas = list(filter(lambda x: x.get_data() == data, cls.vendas))
        if len(vendas)>0:
            relatorio=[]
            for i in vendas:
                nome = i.get_itensVendido().get_nome()
                quantidade = i.get_quantidadeVendida()
                if len(list(filter(lambda x: x['produto'] == nome, relatorio))) == 0:
                    relatorio.append({'produto':nome, 'quantidade':int(quantidade), 'preco':i.get_itensVendido().get_valor(), 'total':float(i.get_total())})
                else:
                    relatorio = list(map(lambda x: {'produto':nome, 'quantidade':x['quantidade'] + int(quantidade), 'preco':x['preco'], 
                                                    'total':x['total'] + float(i.get_total())} if x['produto'] == nome else x, relatorio))
                ordenado = sorted(relatorio, key=lambda k: k['produto'])
            return ordenado
        else:
            return None
    @classmethod
    def pesquisar_periodo(cls, dataInicial, dataFinal):
        cls.vendas = DAOvenda.ler()
        dataInicial = datetime.strptime(dataInicial, "%d/%m/%Y")
        dataFinal = datetime.strptime(dataFinal, "%d/%m/%Y")

        vendas = list(filter(lambda x: datetime.strptime(x.get_data(), "%d/%m/%Y") >= dataInicial and datetime.strptime(x.get_data(), "%d/%m/%Y") <= dataFinal, cls.vendas))
        if len(vendas)>0:
            relatorio=[]
            for i in vendas:
                nome = i.get_itensVendido().get_nome()
                quantidade = i.get_quantidadeVendida()
                if len(list(filter(lambda x: x['produto'] == nome and x['data'] == i.get_data(), relatorio))) == 0:
                    relatorio.append({'produto':nome, 'quantidade':int(quantidade), 'preco':i.get_itensVendido().get_valor(), 'data': i.get_data(),'total':float(i.get_total())})
                else:
                    relatorio = list(map(lambda x: {'produto':nome, 'quantidade':x['quantidade'] + int(quantidade), 'preco':x['preco'], 
                                                    'data': x['data'],'total':x['total'] + float(i.get_total())} if x['produto'] == nome and x['data'] == i.get_data() else x, relatorio))
                ordenado = sorted(relatorio, key=lambda k: k['data'])
            return ordenado
        else:
            return None
    @classmethod
    def pesquisar_produto(cls, nomeProduto):
        cls.vendas = DAOvenda.ler()
        vendas = list(filter(lambda x: x.get_itensVendido().get_nome() == nomeProduto, cls.vendas))
        if len(vendas)>0:
            relatorio = {"produto":nomeProduto, 'quantidade': 0, 'preco':vendas[0].get_itensVendido().get_valor(), 'total': float(vendas[0].get_total())}

            for i in vendas:
                relatorio['quantidade']+=int(i.get_quantidadeVendida())
                relatorio['total'] += float(i.get_total())
            return relatorio
        return None
        

        return list(filter(lambda x: x.get_itensVendido().get_nome() == nomeProduto, cls.vendas))
    @classmethod
    def pesquisa_geral(cls):
        cls.vendas = DAOvenda.ler()
        if len(cls.vendas)>0:
            relatorio = []
            for i in cls.vendas:
                nome = i.get_itensVendido().get_nome()
                quantidade = i.get_quantidadeVendida()
                if len(list(filter(lambda x: x['produto'] == nome and x['data'] == i.get_data() and x['comprador'] == i.get_comprador() and
                                   x['vendedor'] == i.get_vendedor(), relatorio))) == 0:
                    relatorio.append({'produto':nome, 'categoria':i.get_itensVendido().get_categoria().get_nome(), 'preco':i.get_itensVendido().get_valor(),
                                      'vendedor':i.get_vendedor(), 'comprador': i.get_comprador(),'quantidade':int(quantidade),'data':i.get_data(), 
                                      'total':float(i.get_total())})
                else:
                    relatorio = list(map(lambda x: {'produto':x['produto'], 'categoria':x['categoria'],'preco':x['preco'],'vendedor':x['vendedor'], 
                                                    'comprador':x['comprador'],'quantidade':x['quantidade'] + int(quantidade),'data':x['data'],
                                                    'total':x['total'] + float(i.get_total())} if x['produto'] == nome and x['data'] == i.get_data() and
                                                    x['comprador'] == i.get_comprador() and x['vendedor'] == i.get_vendedor() else x, relatorio))
            ordenado = sorted(relatorio, key=lambda k: k['data'])
            return ordenado
        else:
            return None
#ControllerVenda.cadastrar("Maracuja", 'Rayssa Flayny',"Carlos Rayllan", 10)

#ControllerEstoque.ver_estoque()
#ControllerCliente.cadastrar("Carlos Melo", "98982522521", "93845484343", "carlos.rayllan@gmail.com", "rua habitar brasil")
ControllerCliente.editar("Carlos Melo", "Rafael", "98982522594", "07385566378","mtadayz7@gmail.com", "Rua da banana")
#ControllerVenda.relatorio_parcial_produto('Coca Cola 2l')
#ControllerVenda.cadastrar("Tomate", "Rayssa Flayny", "Carlos Rayllan", 2)ff 
