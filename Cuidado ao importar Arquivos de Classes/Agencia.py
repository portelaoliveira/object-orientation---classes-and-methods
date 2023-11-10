from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do n�vel recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O Valor de Caixa est� ok. Caixa Atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empr�stimo n�o � poss�vel. Dinheiro n�o dispon�vel em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O Cliente n�o tem o patrim�nio m�nimo necess�rio para entrar na Ag�ncia Premium')


if __name__ == '__main__':
    agencia1 = Agencia(22223333, 2000000000, 4568)

    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 22224444, 15200000000)
    agencia_virtual.verificar_caixa()
    agencia_comum = AgenciaComum(22225555, 25500000000)
    agencia_premium = AgenciaPremium(22226666, 55500000000)

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    agencia_premium.adicionar_cliente('Lira', 15000000000, 50000000)
    print(agencia_premium.clientes)

    agencia_comum.adicionar_cliente('Irm�o do lira', 10200000000, 10)
    print(agencia_comum.clientes)