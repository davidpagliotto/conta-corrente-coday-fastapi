from fastapi import APIRouter

from model.conta_model import ContaInput, ContaOutput
from service.conta_service import ContaService

router = APIRouter()
conta_router = dict(
    router=router,
    prefix="/contas",
    tags=["Conta"],
)


@router.post("", response_model=ContaOutput)
def post_nova_conta(body: ContaInput):
    service = ContaService()
    return service.nova_conta(body)
