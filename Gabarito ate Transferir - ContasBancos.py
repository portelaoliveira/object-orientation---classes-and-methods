from datetime import datetime
import pytz


class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


# programa
conta_Lira = ContaCorrente("Lira", "111.222.333-45", 1234, 34062)
conta_Lira.consultar_saldo()

# depositando um dinheirinho na conta
conta_Lira.depositar(10000)
conta_Lira.consultar_saldo()

print('Saldo Final')
conta_Lira.consultar_saldo()
conta_Lira.consultar_limite_chequeespecial()

print('-' * 20)
conta_Lira.consultar_historico_transacoes()

print('-' * 20)
conta_maeLira = ContaCorrente('Beth', '222.333.444-55', 5555, 656565)
conta_Lira.transferir(1000, conta_maeLira)

conta_Lira.consultar_saldo()
conta_maeLira.consultar_saldo()

conta_Lira.consultar_historico_transacoes()
conta_maeLira.consultar_historico_transacoes()

