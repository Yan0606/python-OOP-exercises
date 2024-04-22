from datetime import date


class Imovel:
    def __init__(self, endereco, dataContrucao, areaTotal, areaConstruida, qtdDormitorios, qtdBanheiros, qtdVagasGaragem, valorIptu, valorVenda, valorAluguel):
        self.__endereco = endereco
        self.__dataContrucao = dataContrucao
        self.__areaTotal = areaTotal
        self.__areaConstruida = areaConstruida
        self.__qtdDormitorios = qtdDormitorios
        self.__qtdBanheiros = qtdBanheiros
        self.__qtdVagasGaragem = qtdVagasGaragem
        self.__valorIptu = valorIptu
        self.__valorVenda = valorVenda
        self.__valorAluguel = valorAluguel

    def enderecoGet(self):
        return self.__endereco

    def enderecoSet(self, endereco):
        self.__endereco = endereco

    def dataConstrucaoGet(self):
        return self.__dataContrucao

    def dataConstrucaoSet(self, dataContrucao):
        self.__dataContrucao = dataContrucao

    def areaTotalGet(self):
        return self.__areaTotal

    def areaTotalSet(self, areaTotal):
        self.__areaTotal = areaTotal

    def areaConstruidaGet(self):
        return self.__areaConstruida

    def areaConstruidaSet(self, areaConstruida):
        self.__areaConstruida = areaConstruida

    def qtdDormitoriosGet(self):
        return self.__qtdDormitorios

    def qtdDormitoriosSet(self, qtdDormitorios):
        self.__qtdDormitorios = qtdDormitorios

    def qtdBanheirosGet(self):
        return self.__qtdBanheiros

    def qtdBanheirosSet(self, qtdBanheiros):
        self.__qtdBanheiros = qtdBanheiros

    def qtdVagasGaragemGet(self):
        return self.__qtdVagasGaragem

    def qtdVagasGaragemSet(self, qtdVagasGaragem):
        self.__qtdVagasGaragem = qtdVagasGaragem

    def valorIptuGet(self):
        return self.__valorIptu

    def valorIptuSet(self, valorIptu):
        self.__valorIptu = valorIptu

    def valorVendaGet(self):
        return self.__valorVenda

    def valorVendaSet(self, valorVenda):
        self.__valorVenda = valorVenda

    def valorAluguelGet(self):
        return self.__valorAluguel

    def valorAluguelSet(self, valorAluguel):
        self.__valorAluguel = valorAluguel

    def imprimir(self):
        print(f"Endereço: {self.__endereco}")
        print(f"Data da Construção: {self.__dataContrucao}")
        print(f"Área total do terreno: {self.__areaTotal}")
        print(f"Área total construída: {self.__areaConstruida}")
        print(f"Quantidade de dormitórios: {self.__qtdDormitorios}")
        print(f"Quantidade de Banheiros: {self.__qtdBanheiros}")
        print(f"Quantidade de vagas na garagem: {self.__qtdVagasGaragem}")
        print(f"Valor do IPTU: R${self.__valorIptu}")
        print(f"Valor da Venda: R${self.__valorVenda}")
        print(f"Valor aluguel: R${self.__valorAluguel}")


# =============CLASSE RESIDENCIAL=============
class CasaResidencial(Imovel):
   def __init__(self, endereco, dataConstrucao, areaTotal, areaConstruida,
                 qtdDormitorios, qtdBanheiros, qtdVagasGaragem, valorIptu,
                 valorVenda, valorAluguel):
        super().__init__(endereco, dataConstrucao, areaTotal, areaConstruida,
                         qtdDormitorios, qtdBanheiros, qtdVagasGaragem, valorIptu,
                         valorVenda, valorAluguel)


# =============APARTAMENTO RESIDENCIAL=============
class ApartamentoResidencial(Imovel):
    def __init__(self, endereco, dataConstrucao, areaTotal,
                 qtdDormitorios, qtdBanheiros, qtdVagasGaragem, valorIptu,
                 valorVenda, valorAluguel, andar, possuiSacada, valorCondominio):
        super().__init__(endereco, dataConstrucao, areaTotal, areaTotal,
                         qtdDormitorios, qtdBanheiros, qtdVagasGaragem, valorIptu,
                         valorVenda, valorAluguel)
        self.__andar = andar
        self.__possuiSacada = possuiSacada
        self.__valorCondominio = valorCondominio

    def andarGet(self):
        return self.__andar

    def andarSet(self, andar):
        self.__andar = andar

    def possuiSacadaGet(self):
        return self.__possuiSacada

    def possuiSacadaSet(self, possuiSacada):
        self.__possuiSacada = possuiSacada

    def valorCondominioGet(self):
        return self.__valorCondominio

    def valorCondominioSet(self, valorCondominio):
        self.__valorCondominio = valorCondominio

    def getValorAluguel(self):
        return self.valorAluguel * 1.2

    def valorAluguelSet(self, valorAluguel):
        self.__valorAluguel = valorAluguel


# =============CLASSE COMERCIAL=============
class Comercial(Imovel):
    def __init__(self, endereco, dataConstrucao, areaTotal,
                 qtdDormitorios, qtdBanheiros, qtdVagasGaragem, valorIptu,
                 valorVenda, valorAluguel, tipoComercio, taxaImpostoFederal, taxaImpostoEstadual):
        super().__init__(endereco, dataConstrucao, areaTotal, areaTotal,
                         qtdDormitorios, qtdBanheiros, qtdVagasGaragem, valorIptu,
                         valorVenda, valorAluguel)
        self.__tipoComercio = tipoComercio
        self.__taxaImpostoFederal = taxaImpostoFederal
        self.__taxaImpostoEstadual = taxaImpostoEstadual

    def tipoComercioGet(self):
        return self.__tipoComercio

    def tipoComercioSet(self, tipoComercio):
        self.__tipoComercio = tipoComercio

    def taxaImpostoFederalGet(self):
        return self.__taxaImpostoFederal

    def taxaImpostoFederalSet(self, taxaImpostoFederal):
        self.__taxaImpostoFederal = taxaImpostoFederal

    def taxaImpostoEstadualGet(self):
        return self.__taxaImpostoEstadual

    def taxaImpostoEstadualSet(self, taxaImpostoEstadual):
        self.__taxaImpostoEstadual = taxaImpostoEstadual



# =============MENU DE ESCOLHA=============
def menu():
    print("Escolha o tipo de imóvel:")
    print("1 - Casa Residencial")
    print("2 - Apartamento Residencial")
    print("3 - Comercial")
    opcao = input("Digite o número correspondente ao tipo de imóvel desejado: ")
    return opcao

def main():
    opcao = menu()

    if opcao == "1":
        imovel = CasaResidencial("José Ribeiro da Motta", date.today(), 300000, 150000, 3, 3, 3, 1200.00, 500000, 2000)
    elif opcao == "2":
        imovel = ApartamentoResidencial("José Ribeiro da Motta", date.today(), 300000, 3, 3, 3, 1200.00, 500000, 2000, 2, True, 1000)
    elif opcao == "3":
        imovel = Comercial("José Ribeiro da Motta", date.today(), 300000, 3, 3, 3, 1200.00, 500000, 2000, "Venda", 150, 250)
    else:
        print("Opção inválida!")
        return

    imovel.imprimir()

if __name__ == "__main__":
    main()