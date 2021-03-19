import sqlite3

from model.conta_model import Conta
from model.correntista_model import Correntista
from repository import database


class ContaRepository:

    @staticmethod
    def insert(conta: Conta):
        conn = sqlite3.connect(database.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO conta (agencia, numero_conta) VALUES (?, ?)", (conta.agencia, conta.numero_conta))
        conn.commit()
        conta.id_conta = cursor.lastrowid
        conn.close()
        return conta

    @staticmethod
    def insert_relacao_correntista_conta(correntista: Correntista, conta: Conta):
        conn = sqlite3.connect(database.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO relacao_correntista_conta (id_correntista, id_conta, agencia, numero_conta) VALUES (?, ?, ?, ?)
        """, (correntista.id_correntista, conta.id_conta, conta.agencia, conta.numero_conta))
        conn.commit()
        conn.close()

    def get_by_id(self, id_conta: int):
        conn = sqlite3.connect(database.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id_conta, agencia, numero_conta FROM conta where id_conta = ?", (id_conta,))
        linha = cursor.fetchone()
        conn.close()

        if linha:
            return self._converte_linha(linha)

        return None

    def get_by_agencia_numero_conta(self, agencia: str, numero_conta: str):
        conn = sqlite3.connect(database.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id_conta, agencia, numero_conta FROM conta where agencia = ? and numero_conta = ?",
                       (agencia, numero_conta))
        linha = cursor.fetchone()
        conn.close()

        if linha:
            return self._converte_linha(linha)

        return None

    @staticmethod
    def _converte_linha(linha):
        conta = Conta()
        conta.id_conta = linha[0]
        conta.agencia = linha[1]
        conta.numero_conta = linha[2]
        return conta
