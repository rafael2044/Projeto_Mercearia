from datetime import datetime
class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self._nome = nome
        self._telefone = telefone
        self._cpf = cpf
        self._email = email
        self._endereco = endereco

    def get_nome(self):
        return self._nome
    def get_telefone(self):
        return self._telefone
    def get_cpf(self):
        return self._cpf
    def get_email(self):
        return self._email
    def get_endereco(self):
        return self._endereco
    
    def set_nome(self, nome):
        self._nome = nome
    def set_telefone(self, telefone):
        self._telefone = telefone
    def set_cpf(self, cpf):
        self._cpf = cpf
    def set_email(self, email):
        self._email = email
    def set_endereco(self, endereco):
        self._endereco = endereco
    
class Cliente(Pessoa):
    count_id = 0
    def __init__(self, nome, telefone, cpf, email, endereco):
        super().__init__(nome, telefone, cpf, email, endereco)
        self._id = self.gerar_id()
    

    @classmethod
    def gerar_id(cls):
        cls.count_id += 1
        return cls.count_id
    
    @classmethod
    def zerar_id(cls):
        cls.count_id = 0

    def get_id(self):
        return self._id

class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        super().__init__(nome, telefone, cpf, email, endereco)
        self._clt = clt
        self._id = self.gerar_id()
        
    @classmethod
    def gerar_id(cls):
        cls.count_id += 1
        return cls.count_id

    @classmethod
    def zerar_id(cls):
        cls.count_id = 0

    def get_id(self):
        return self._id
    
    def get_clt(self):
        return self._clt

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self._nome = nome
        self._cnpj = cnpj
        self._telefone = telefone
        self._categoria = categoria

class Categoria:
    def __init__(self, categoria):
        self._categoria = categoria

    def get_nome(self):
        return self._categoria
    
class Produto:
    def __init__(self, nome : str, categoria : Categoria, valor : float):
        self._nome = nome
        self._categoria = categoria
        self._valor = valor
        
    def get_valor(self):
        return self._valor
    def get_nome(self):
        return self._nome
    def get_categoria(self):
        return self._categoria
    
class Estoque:
    def __init__(self, produto: Produto, quantidade : int):
        self._produto = produto
        self._quantidade = quantidade

    def get_produto(self):
        return self._produto
    def get_quantidade(self):
        return self._quantidade
    def incrementar(self, quantidade):
        if quantidade > 0:
            self._quantidade += quantidade
    def decrementar(self, quantidade):
        if quantidade > 0 and self._quantidade >= quantidade:
            self._quantidade -= quantidade

class Venda:
    def __init__(self, itensVendido : Produto, vendedor, comprador, quantidadeVendida, data = datetime.now()):
        self._itensVendido = itensVendido
        self._vendedor = vendedor 
        self._comprador = comprador
        self._quantidadeVendida = quantidadeVendida
        self._data = data
    
    def get_itensVendido(self):
        return self._itensVendido
    def get_vendedor(self):
        return self._vendedor
    def get_comprador(self):
        return self._comprador
    def get_quantidadeVendida(self):
        return self._quantidadeVendida
    def get_data(self):
        return datetime.strftime(self._data, "%d/%m/%Y-%H:%M:%S")