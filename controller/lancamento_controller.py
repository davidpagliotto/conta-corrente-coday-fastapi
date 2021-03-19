from typing import List, Optional

from fastapi import APIRouter

from model.lancamento_model import LancamentoInput, LancamentoOutput, SaldoOutput
from service.lancamento_service import LancamentoService

router = APIRouter()
lancamento_router = dict(
    router=router,
    prefix="/lancamentos",
    tags=["Lancamento"],
)


@router.post("", response_model=LancamentoOutput)
def post_novo_lancamento(body: LancamentoInput):
    service = LancamentoService()
    return service.novo_lancamento(body)


@router.get("", response_model=List[LancamentoOutput])
def get_lancamentos(id_correntista: int, agencia: Optional[str] = None, numero_conta: Optional[str] = None):
    service = LancamentoService()
    return service.get_lancamentos(id_correntista, agencia, numero_conta)


@router.get("/saldos", response_model=List[SaldoOutput])
def get_saldo(id_correntista: int, agencia: Optional[str] = None, numero_conta: Optional[str] = None):
    service = LancamentoService()
    return service.get_saldo(id_correntista, agencia, numero_conta)
