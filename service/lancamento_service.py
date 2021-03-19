from typing import Optional

from configuration.exceptions import ApiBaseException
from model.lancamento_model import LancamentoInput, Lancamento, SaldoOutput
from repository.conta_repository import ContaRepository
from repository.correntista_controller import CorrentistaRepository
from repository.lancamento_repository import LancamentoRepository


class LancamentoService:

    def __init__(self):
        self._repository = LancamentoRepository()
        self._correntista_repository = CorrentistaRepository()
        self._conta_repository = ContaRepository()

    def novo_lancamento(self, lancamento_input: LancamentoInput):
        correntista = self._correntista_repository.get_by_id(lancamento_input.id_correntista)
        conta = self._conta_repository.get_by_agencia_numero_conta(lancamento_input.agencia,
                                                                   lancamento_input.numero_conta)
        if not correntista:
            raise ApiBaseException(detail=f"Correntista com id {lancamento_input.id_correntista} não encontrado")

        if not conta:
            raise ApiBaseException(detail=f"Conta com agencia {lancamento_input.agencia} "
                                          f"e numero {lancamento_input.numero_conta} não encontrada")

        lancamento = Lancamento()
        lancamento.correntista = correntista
        lancamento.conta = conta
        lancamento.valor = lancamento_input.valor
        lancamento.tipo = lancamento_input.tipo
        lancamento.data = lancamento_input.data

        lancamento = self._repository.insert(lancamento)
        return lancamento

    def get_lancamentos(self, id_correntista: int, agencia: Optional[str] = None, numero_conta: Optional[str] = None):
        lancamentos = self._repository.get_lancamentos(id_correntista, agencia, numero_conta)
        return lancamentos if lancamentos else []

    def get_saldo(self, id_correntista: int, agencia: Optional[str] = None, numero_conta: Optional[str] = None):
        lancamentos = self.get_lancamentos(id_correntista, agencia, numero_conta)

        saldos = []
        for lancamento in lancamentos:
            conta = lancamento.conta
            saldo = next((saldo for saldo in saldos if saldo.conta.id_conta == conta.id_conta), None)
            if not saldo:
                saldo = SaldoOutput(conta=conta, saldo=lancamento.valor_lancamento())
                saldos.append(saldo)
            else:
                saldo.saldo += lancamento.valor_lancamento()

        return saldos
