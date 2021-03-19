import sqlite3

from model.correntista_model import Correntista
from repository import database


class CorrentistaRepository:

    @staticmethod
    def insert(correntista: Correntista):
        conn = sqlite3.connect(database.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO correntista (nome) VALUES (?)", (correntista.nome,))
        conn.commit()
        correntista.id_correntista = cursor.lastrowid
        conn.close()
        return correntista

    @staticmethod
    def get_by_id(id_correntista: int):
        conn = sqlite3.connect(database.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id_correntista, nome FROM correntista where id_correntista = ?", (id_correntista,))
        linha = cursor.fetchone()
        conn.close()

        if linha:
            correntista = Correntista()
            correntista.id_correntista = linha[0]
            correntista.nome = linha[1]
            return correntista

        return None
