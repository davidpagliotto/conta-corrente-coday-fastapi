from datetime import date
from enum import Enum

from pydantic.main import BaseModel

from model.conta_model import Conta, ContaOutput
from model.correntista_model import Correntista, CorrentistaOutput


class TipoLancamentoEnum(Enum):
    DEBITO = "DEBITO"
    CREDITO = "CREDITO"


class Lancamento:

    def __init__(self):
        self.id_lancamento: int = 0
        self.correntista: Correntista = Correntista()
        self.conta: Conta = Conta()
        self.valor: float = .0
        self.tipo: TipoLancamentoEnum = TipoLancamentoEnum.DEBITO
        self.data: date = date.today()

    def valor_lancamento(self):
        return self.valor \
            if self.tipo in [TipoLancamentoEnum.CREDITO, TipoLancamentoEnum.CREDITO.value] \
            else self.valor * -1


class LancamentoInput(BaseModel):
    id_correntista: int
    agencia: str
    numero_conta: str
    valor: float
    tipo: TipoLancamentoEnum
    data: date


class LancamentoOutput(BaseModel):
    id_lancamento: int
    correntista: CorrentistaOutput
    conta: ContaOutput
    valor: float
    tipo: TipoLancamentoEnum
    data: date

    class Config:
        orm_mode = True


class SaldoOutput(BaseModel):
    conta: ContaOutput
    saldo: float

    class Config:
        orm_mode = True
