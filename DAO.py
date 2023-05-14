from model import Cliente, Funcionario, Categoria,Produto, Estoque, Venda

class DAOcliente:
    @classmethod
    def zerar(cls):
        with open("db/clientes.txt", "w") as arq:
            Cliente.zerar_id()
            arq.writelines("")

    @classmethod
    def salvar(cls, cliente:Cliente):
        with open("db/clientes.txt", 'a+') as arq:
            arq.writelines("{}|{}|{}|{}|{}|{}".format(str(cliente.get_id()) ,cliente.get_nome() ,cliente.get_telefone(),
                           cliente.get_cpf(), cliente.get_email(), cliente.get_endereco()))
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        with open("db/clientes.txt", 'r') as arq:
            cls.cliente = arq.readlines()
            cls.cliente = list(map(lambda x: x.replace("\n", ""), cls.cliente))
            cls.cliente = list(map(lambda x: x.split('|'), cls.cliente))
            cliente = []
            Cliente.zerar_id()
            for i in cls.cliente:
                cliente.append(Cliente(i[1],i[2],i[3],i[4],i[5]))
            return cliente
    @classmethod
    def verificar_nome(cls, nome):
        cliente = list(filter(lambda x: x.get_nome() == nome, cls.ler()))
        if len(cliente) == 1:
                return True
        return False
        
class DAOfuncionario:
    @classmethod
    def zerar(cls):
        with open("db/funcionarios.txt", "w") as arq:
            arq.writelines("")
            
    @classmethod
    def salvar(cls, funcionario : Funcionario):
        with open("db/funcionarios.txt", 'a+') as arq:
            arq.writelines("{}|{}|{}|{}|{}|{}|{}".format(str(funcionario.get_id()), funcionario.get_clt(),funcionario.get_nome(),
                           funcionario.get_telefone(),funcionario.get_cpf(), funcionario.get_email(),funcionario.get_endereco()))
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        with open("db/funcionarios.txt", 'r') as arq:
            cls.funcionario = arq.readlines()
            cls.funcionario = list(map(lambda x: x.replace("\n", ""), cls.funcionario))
            cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))
            funcionarios = []
            Funcionario.zerar_id()
            for i in cls.funcionario:
                funcionarios.append(Funcionario(i[1],i[2],i[3],i[4],i[5],i[6]))
            return funcionarios
    @classmethod
    def verificar_nome(cls, nome):
        funcionario = list(filter(lambda x: x.get_nome == nome, cls.ler()))
        if len(funcionario) == 1:
                return True
        return False
        
class DAOcategoria:
    @classmethod
    def zerar(cls):
        with open('db/categoria.txt', 'w') as arq:
            arq.writelines('')
    @classmethod
    def salvar(cls, categoria : Categoria):
        with open('db/categoria.txt', 'a+') as arq:
            arq.writelines(categoria.get_nome())
            arq.writelines("\n")
    @classmethod
    def ler(cls):
        with open('db/categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
            cls.categoria = list(map(lambda x: x.replace("\n", ''), cls.categoria))

            categoria = []
            for i in cls.categoria:
                categoria.append(Categoria(i))
            return categoria
    @classmethod
    def verificar(cls, categoria):
        categoria = list(filter(lambda x: x.get_nome().lower() == categoria.lower(), cls.ler()))
        if len(categoria) == 1:
                return True
        return False

class DAOestoque:
    @classmethod
    def zerar(cls):
        with open('db/estoque.txt', 'w') as arq:
            arq.writelines('')
            Produto.zerar_id()
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open("db/estoque.txt", 'a+') as arq:
            arq.writelines("{0}|{1}|{2}|{3}|{4}".format(str(produto.get_id()),produto.get_nome(),produto.get_categoria().get_nome(),produto.get_valor(),str(quantidade)))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("db/estoque.txt", 'r') as arq:
            cls.estoque = arq.readlines()
            cls.estoque = list(map(lambda x: x.replace("\n", ""), cls.estoque))
            cls.estoque = list(map(lambda x: x.split("|"), cls.estoque))
            estoque = []
            Produto.zerar_id()
            for produto in cls.estoque:
                estoque.append(Estoque(Produto(produto[1], Categoria(produto[2]), float(produto[3])), int(produto[4])))
            return estoque
    
    @classmethod
    def verificar(cls, nomeProduto):
        estoque = list(filter(lambda x: x.get_produto().get_nome().lower() == nomeProduto.lower(), cls.ler()))
        if len(estoque) == 1:
                return True
        return False
    
class DAOvenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open("db/venda.txt", "a+") as arq:
            arq.writelines("{0}|{1}|{2}|{3}|{4}|{5}|{6}".format(venda.get_itensVendido().get_nome(),
                                                                venda.get_itensVendido().get_categoria().get_nome(),
                                                                venda.get_itensVendido().get_valor(),
                                                                venda.get_vendedor(),venda.get_comprador(),
                                                                venda.get_quantidadeVendida(),venda.get_data()))
            arq.writelines("\n")
    def ler(cls):
        with open("db/venda.txt", 'r') as arq:
            cls.vendas = arq.readlines()
            cls.vendas = list(map(lambda x: x.replace('\n', ''), cls.vendas))
            cls.vendas = list(map(lambda x: x.split("|"), cls.vendas))
            vendas = []
            for i in cls.vendas:
                vendas.append(Venda(Produto(i[0], Categoria(i[1]), i[2]), i[3], i[4], i[5], i[6]))
            return vendas
            