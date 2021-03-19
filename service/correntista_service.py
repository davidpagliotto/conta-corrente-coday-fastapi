from model.correntista_model import CorrentistaInput, Correntista
from repository.correntista_controller import CorrentistaRepository


class CorrentistaService:

    def __init__(self):
        self._repository = CorrentistaRepository()

    def novo_correntista(self, correntista_input: CorrentistaInput):
        correntista = Correntista()
        correntista.nome = correntista_input.nome

        correntista = self._repository.insert(correntista)
        return correntista
