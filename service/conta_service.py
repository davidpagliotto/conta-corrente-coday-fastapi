from configuration.exceptions import ApiBaseException
from model.conta_model import ContaInput, Conta
from model.correntista_model import Correntista
from repository.conta_repository import ContaRepository
from repository.correntista_controller import CorrentistaRepository


class ContaService:

    def __init__(self):
        self._repository = ContaRepository()
        self._correntista_repository = CorrentistaRepository()

    def nova_conta(self, conta_input: ContaInput):
        correntista = self._correntista_repository.get_by_id(conta_input.id_correntista)
        if not correntista:
            raise ApiBaseException(detail=f"Correntista com id {conta_input.id_correntista} não encontrado")

        conta = Conta()
        conta.agencia = conta_input.agencia
        conta.numero_conta = conta_input.numero_conta
        conta = self._repository.insert(conta)

        self._repository.insert_relacao_correntista_conta(correntista, conta)

        return conta
