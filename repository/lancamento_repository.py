import sqlite3
from typing import Optional

from model.lancamento_model import Lancamento
from repository import database
from repository.conta_repository import ContaRepository
from repository.correntista_controller import CorrentistaRepository


class LancamentoRepository:

    @staticmethod
    def insert(lancamento: Lancamento):
        conn = sqlite3.connect(database.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO lancamento (id_correntista, id_conta, valor, tipo, data) VALUES (?, ?, ?, ?, ?)",
                       (lancamento.correntista.id_correntista,
                        lancamento.conta.id_conta,
                        lancamento.valor,
                        lancamento.tipo.value,
                        lancamento.data))
        conn.commit()
        lancamento.id_lancamento = cursor.lastrowid
        conn.close()
        return lancamento

    @staticmethod
    def get_lancamentos(id_correntista: int, agencia: Optional[str] = None, numero_conta: Optional[str] = None):
        sql = "SELECT " \
              " lancamento.id_lancamento, " \
              " lancamento.id_correntista, " \
              " lancamento.id_conta, " \
              " lancamento.valor, " \
              " lancamento.tipo, " \
              " lancamento.data " \
              "FROM " \
              " lancamento " \
              " JOIN conta on lancamento.id_conta = conta.id_conta " \
              "WHERE " \
              " lancamento.id_correntista = ? "
        params = (id_correntista, )

        if agencia:
            sql += " AND conta.agencia = ? "
            params += (agencia, )

        if numero_conta:
            sql += " AND conta.numero_conta = ? "
            params += (numero_conta, )

        sql += " ORDER BY conta.id_conta, lancamento.data, lancamento.id_lancamento "

        conn = sqlite3.connect(database.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        linhas = cursor.fetchall()
        conn.close()

        lancamentos = []

        if linhas:
            correntista = CorrentistaRepository.get_by_id(id_correntista)
            conta_repository = ContaRepository()
            for linha in linhas:
                lancamento = Lancamento()
                lancamento.id_lancamento = linha[0]
                lancamento.correntista = correntista
                lancamento.conta = conta_repository.get_by_id(linha[2])
                lancamento.valor = linha[3]
                lancamento.tipo = linha[4]
                lancamento.data = linha[5]
                lancamentos.append(lancamento)

        return lancamentos
