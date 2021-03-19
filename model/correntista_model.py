from pydantic.main import BaseModel


class Correntista:

    def __init__(self):
        self.id_correntista: int = 0
        self.nome: str = ""


class CorrentistaInput(BaseModel):
    nome: str


class CorrentistaOutput(BaseModel):
    id_correntista: int
    nome: str

    class Config:
        orm_mode = True
