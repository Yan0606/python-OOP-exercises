class Professor:
    def __init__(self, matricula, nome, titulacao, telefone, email, salario):
        self.matricula = matricula
        self.nome = nome
        self.titulacao = titulacao
        self.telefone = telefone
        self.email = email
        self.salario = salario

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_titulacao(self):
        return self.titulacao

    def set_titulacao(self, titulacao):
        self.titulacao = titulacao

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def imprime(self):
        print(f"Matrícula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Titulação: {self.titulacao}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print(f"Salário: R${self.salario:.2f}")


class Departamento:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.lista_professores = []

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def adicionar_professor(self, professor):
        self.lista_professores.append(professor)

    def excluir_professor(self, matricula):
        for professor in self.lista_professores:
            if professor.get_matricula() == matricula:
                self.lista_professores.remove(professor)
                return True
        return False

    def busca_professor(self, matricula):
        for professor in self.lista_professores:
            if professor.get_matricula() == matricula:
                return True
        return False

    def imprime(self):
        print(f"Nome do Departamento: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print("Lista de Professores:")
        for professor in self.lista_professores:
            professor.imprime()
            print("-------------------------")


if __name__ == "__main__":
    prof1 = Professor(1, "Bruno", "Doutor", "1234-5678", "Bruno@gmail.com", 10000.00)
    prof2 = Professor(2, "Vanessa", "Doutora", "9876-5432", "Vanessa@gmail.com", 10000.00)

    
    departamento = Departamento("Departamento de Suporte TI", "1111-2222", "suporte1@gmail.com")

    departamento.adicionar_professor(prof1)
    departamento.adicionar_professor(prof2)

   
    departamento.imprime()

    departamento.excluir_professor(1)

    print(departamento.busca_professor(2))
