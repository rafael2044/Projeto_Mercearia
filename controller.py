from DAO import DAOcliente, DAOfuncionario, DAOcategoria, DAOestoque
from model import Cliente, Funcionario, Categoria, Produto, Estoque
class ControllerCliente:
    @classmethod
    def cadastrar(cls, nome : str, telefone: str, cpf: str, email: str, endereco: str):
        if (len(nome)>=3 and len(telefone) == 11 and len(cpf) == 11 and len(email)>10 and len(endereco)>5) and not(DAOcliente.verificar(nome)):
            DAOcliente.salvar(Cliente(nome, telefone, cpf, email,endereco))
            return True
        return False
    @classmethod
    def ver_clientes(cls):
        clientes = DAOcliente.ler()
        print(" {0} \n|{1:^30}|{2:^15}|{3:^15}|{4:^25}|{5:30}|\n {0} "
              .format(119*"-", "NOME", "TELEFONE", "CPF", "E-MAIL", "ENDEREÇO"))
        for i in clientes:
            print("|{0:30}|{1:15}|{2:15}|{3:25}|{4:30}|"
                  .format(i.get_nome(), i.get_telefone(), i.get_cpf(),
                          i.get_email(), i.get_endereco()))
        print(" {0} ".format(119*"-"))
        

class ControllerFuncionario:
    @classmethod
    def cadastrar(cls ,clt: str, nome: str, telefone: str, cpf: str, email: str,endereco: str):
        if ((clt.lower() == 'sim' or clt.lower == 'não') and len(nome)>3 and len(telefone) == 11 and len(cpf) == 11 and len(email)>10 and len(endereco)>4) and not DAOfuncionario.verificar(nome):
            DAOfuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
            return True
        return False
    @classmethod
    def ver_funcionario(cls):
        funcionarios = DAOfuncionario.ler()
        print(" {0} \n|{1:^10}|{2:^30}|{3:^15}|{4:^15}|{5:^25}|{6:50}|\n {0} "
              .format(150*"-", "CLT", "NOME", "TELEFONE", "CPF", "E-MAIL", "ENDEREÇO"))
        for i in funcionarios:
            print("|{0:10}|{1:30}|{2:15}|{3:15}|{4:25}|{5:50}|"
                  .format(i.get_clt() ,i.get_nome(), i.get_telefone(), i.get_cpf(),
                          i.get_email(), i.get_endereco()))
        print(" {0} ".format(150*"-"))
    
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
    def pesquisar(cls, nome):
        cls.funcionario = DAOfuncionario.ler()
        for i in cls.funcionario:
            if i.get_nome() == nome:
                return cls.funcionario.index(i)
        return -1


class ControllerFornecedor:
    pass

class ControllerCategoria:
    @classmethod
    def cadastrar(cls, categoria):
        if len(categoria) > 4 and not DAOcategoria.verificar(categoria):
            DAOcategoria.salvar(Categoria(categoria))
            return True
        return False
    
    @classmethod
    def editar(cls, index, nome):
        if len(nome) > 0 and nome != cls.categoria[index].get_nome():
            cls.categoria[index] = Categoria(nome)
            DAOcategoria.zerar()
            for i in cls.categoria:
                DAOcategoria.salvar(i)
    
    @classmethod
    def deletar(cls, index):
        if index != -1:
            cls.categoria.pop(index)
            DAOcategoria.zerar()
            for i in cls.categoria:
                DAOcategoria.salvar(i)
    
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
    def pesquisar(cls, nome):
        cls.categoria = DAOcategoria.ler()
        for i in cls.categoria:
            if nome.lower() == i.get_nome().lower():
                return cls.categoria.index(i)
        return -1

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
