from DAO import DAOcliente, DAOfuncionario, DAOcategoria, DAOestoque, DAOvenda
from model import Cliente, Funcionario, Categoria, Produto, Estoque, Venda
class ControllerCliente:
    @classmethod
    def cadastrar(cls, nome : str, telefone: str, cpf: str, email: str, endereco: str):
        if (len(nome)>=3 and len(telefone) == 11 and len(cpf) == 11 and len(email)>10 and len(endereco)>5) and not(DAOcliente.verificar_nome(nome)):
            DAOcliente.salvar(Cliente(nome, telefone, cpf, email,endereco))
            print("Cadastro realizado com sucesso!")
        else:
            print("Erro ao cadastrar cliente!")
        
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

    def editar(cls, id, nome, telefone, cpf, email, endereco):
        if not cls.pesquisar_nome(nome):
            if len(nome)>=3 and len(telefone) == 11 and len(cpf) == 11 and len(email.split("@")) > 1  and len(endereco) > 5:
                DAOcliente.zerar()
                cls.cliente = list(map(lambda x: Cliente(nome, telefone, cpf, email, endereco) if x.get_id() == id else x, cls.cliente))
                for i in cls.cliente:
                    DAOcliente.salvar(i)
                print("Alteracoes realizadas com sucesso!")
            else:
                print("Falha ao inserir dados!")
        else:
            print("Cliente ja existe")
    
    @classmethod
    def deletar(cls, id):
        if cls.pesquisar_id(id):
            cls.cliente.remove(list(filter(lambda x: x.get_id() == id, cls.cliente))[0])
            DAOcliente.zerar()
            for i in cls.cliente:
                DAOcliente.salvar(i)
            print("Cliente removido com sucesso")
        else:
            print("Cliente nao encontrado!")

    @classmethod
    def pesquisar_id(cls, id):
        cls.cliente = DAOcliente.ler()
        cliente = list(filter(lambda x: x.get_id() == id, cls.cliente))
        if len(cliente) == 1:
            return True
        return False
    
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
        if ((clt.lower() == 'sim' or clt.lower == 'não') and len(nome)>3 and len(telefone) == 11 and len(cpf) == 11 and len(email)>10 and len(endereco)>4) and not DAOfuncionario.verificar_nome(nome):
            DAOfuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
            return True
        return False
    
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
            return list(filter(lambda x: x.get_produto(), cls.estoque))[0]
        else:
            return None
class ControllerCaixa:
    pass

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
    def ver_vendas(cls):
        cls.vendas = DAOvenda.ler()
        print(" {8} \n|{0:^30}|{1:^15}|{2:^10}|{3:^30}|{4:^30}|{5:^10}|{6:^15}|{7:^15}|\n {8} "
              .format('NOME PRODUTO','CATEGORIA', 'PRECO', 'VENDEDOR', 'COMPRADOR', 'QUANTIDADE', "DATA", "TOTAL", 162*'-'))
        for i in cls.vendas:
            print("|{0:30}|{1:15}|{2:^10}|{3:30}|{4:30}|{5:^10}|{6:^15}|{7:^15}|"
                  .format(i.get_itensVendido().get_nome(), i.get_itensVendido().get_categoria().get_nome(), i.get_itensVendido().get_valor(),
                          i.get_vendedor(), i.get_comprador(), i.get_quantidadeVendida(), i.get_data(),
                          str(i.get_total())))
            print(f" {162*'-'} ")

ControllerVenda.ver_vendas()
#ControllerEstoque.cadastrar("Coca Cola 2l", "Bebida", 8.50, 100)
