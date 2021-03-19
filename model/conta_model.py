from pydantic.main import BaseModel


class Conta:

    def __init__(self):
        self.id_conta: int = 0
        self.agencia: str = ""
        self.numero_conta: str = ""


class ContaInput(BaseModel):
    id_correntista: int
    agencia: str
    numero_conta: str


class ContaOutput(BaseModel):
    id_conta: int
    agencia: str
    numero_conta: str

    class Config:
        orm_mode = True
