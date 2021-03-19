from fastapi import APIRouter

from model.correntista_model import CorrentistaInput, CorrentistaOutput
from service.correntista_service import CorrentistaService

router = APIRouter()
correntista_router = dict(
    router=router,
    prefix="/correntistas",
    tags=["Correntista"],
)


@router.post("", response_model=CorrentistaOutput)
def post_novo_correntista(body: CorrentistaInput):
    service = CorrentistaService()
    return service.novo_correntista(body)
