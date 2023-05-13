from DAO import DAOcliente, DAOfuncionario, DAOcategoria, DAOestoque
from model import Cliente, Funcionario, Categoria, Produto, Estoque
class ControllerCliente:
    @classmethod
    def cadastrar(cls, nome : str, telefone: str, cpf: str, email: str, endereco: str):
        if (len(nome)>=3 and len(telefone) == 11 and len(cpf) == 11 and len(email)>10 and len(endereco)>5) and not(DAOcliente.verificar_nome(nome)):
            DAOcliente.salvar(Cliente(nome, telefone, cpf, email,endereco))
            return True
        return False
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

    def editar(cls, index, nome, telefone, cpf, email, endereco):
        if len(nome)>0 and len(telefone) == 11 and len(cpf) == 11 and len(email) > 0 and len(endereco) > 0:
            cls.cliente[index] = Cliente(nome, telefone, cpf, email, endereco)
            DAOcliente.zerar()
            for i in cls.cliente:
                DAOcliente.salvar(i)
            return True
        return False
    
    @classmethod
    def deletar(cls, index):
        cls.cliente.pop(index)
        DAOcliente.zerar()
        for i in cls.cliente:
            DAOcliente.salvar(i)

    @classmethod
    def pesquisar(cls, id):
        cls.cliente = DAOcliente.ler()
        for i in cls.cliente:
            if i.get_id() == int(id):
                return cls.cliente.index(i)
        return -1

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
        for i in cls.funcionario:
            if i.get_nome() == nome:
                return cls.funcionario.index(i)
        return -1
    
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
    def cadastrar(cls, produto: Produto, quantidade: int):
        if not DAOestoque.verificar(produto) and quantidade > 0:
            DAOestoque.salvar(produto, quantidade)
            return True
        return False
    
    @classmethod
    def editar(cls, index, nome, categoria, valor:float):
        if index != -1:
            if len(nome) > 4 and DAOcategoria.verificar(categoria) and valor > 0:
                cls.estoque[index] = Estoque(Produto(nome, Categoria(categoria), valor), 1)
                DAOestoque.zerar()
                for i in cls.estoque:
                    DAOestoque.salvar(i.get_produto(), i.get_quantidade())
    
    @classmethod
    def incrementar_estoque(cls, index, quantidade):
        cls.estoque[index].incrementar(quantidade)
        DAOestoque.zerar()
        for i in cls.estoque:
            DAOestoque.salvar(i.get_produto(), i.get_quantidade())

    @classmethod
    def decrementar_estoque(cls, index, quantidade):
        cls.estoque[index].decrementar(quantidade)
        DAOestoque.zerar()
        for i in cls.estoque:
            DAOestoque.salvar(i.get_produto(), i.get_quantidade())
            

    @classmethod
    def ver_estoque(cls):
        cls.estoque = DAOestoque.ler()
        print(f" {96*'-'} ")
        print("|{0:^40}|{1:^20}|{2:^18}|{3:^15}|".format('NOME', 'CATEGORIA', 'VALOR', 'QUANTIDADE'))
        print(f" {96*'-'} ")
        for i in cls.estoque:
            print("|{0:40}|{1:20}|{2:>18}|{3:>15}|".format(i.get_produto().get_nome(), i.get_produto().get_categoria().get_nome(),
                                                            i.get_produto().get_valor(), i.get_quantidade()))
            print(f" {96*'-'} ")
    
    @classmethod
    def pesquisar(cls, nome):
        cls.estoque = DAOestoque.ler()
        for i in cls.estoque:
            if i.get_produto().get_nome() == nome:
                return cls.estoque.index(i)
        return -1

class ControllerCaixa:
    pass

class ControllerVenda:
    @classmethod
    def realizar_venda(cls, index, vendedor, comprador, quantidadeVendida):
        produto = cls.estoque[index]
        pass

class ControllerProduto:
    @classmethod
    def cadastrar(cls, nome, categoria, valor):
        if len(nome) > 4 and DAOcategoria.verificar(categoria) and valor > 0:
            print("if ControllerProduto")
            ControllerEstoque.cadastrar(Produto(nome, Categoria(categoria), valor), 1)
