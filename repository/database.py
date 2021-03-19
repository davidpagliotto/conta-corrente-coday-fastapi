import sqlite3

DB_NAME = "conta_corrente.db"


class Database:

    @staticmethod
    def criar_db():
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE conta (
                    id_conta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    agencia TEXT NOT NULL,
                    numero_conta TEXT NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE correntista (
                    id_correntista INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE relacao_correntista_conta (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_correntista INTEGER NOT NULL,
                    id_conta INTEGER NOT NULL,
                    agencia TEXT NOT NULL,
                    numero_conta TEXT NOT NULL,
                    FOREIGN KEY (id_correntista) REFERENCES correntista (id_correntista),
                    FOREIGN KEY (id_conta) REFERENCES conta (id_conta)
                );
            """)
            cursor.execute("""
                CREATE TABLE lancamento (
                    id_lancamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_correntista INTEGER NOT NULL,
                    id_conta INTEGER NOT NULL,
                    tipo TEXT NOT NULL,
                    valor NUMERIC NOT NULL,
                    data DATE NOT NULL,
                    FOREIGN KEY (id_correntista) REFERENCES correntista (id_correntista),
                    FOREIGN KEY (id_conta) REFERENCES conta (id_conta)
                );
            """)
            conn.close()
        except Exception as e:
            print(e)
