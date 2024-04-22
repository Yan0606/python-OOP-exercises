class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Senha: {self.senha}"


class Produto:
    def __init__(self, nome, descricao, quantidade, valor):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor = valor

    def __str__(self):
        return f"Nome: {self.nome}, Descrição: {self.descricao}, Quantidade: {self.quantidade}, Valor: R${self.valor:.2f}"


if __name__ == "__main__":
    usuario1 = Usuario("yan", "yan@email.com", "senha123")

    produto1 = Produto("Notebook", "Notebook Acer", 10, 4500.50)

    print(usuario1)
    print(produto1)
