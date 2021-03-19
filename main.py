import uvicorn
from fastapi import FastAPI

from configuration.exceptions import ApiBaseException, generic_handler
from controller.conta_controller import conta_router
from controller.correntista_controller import correntista_router
from controller.lancamento_controller import lancamento_router
from repository.database import Database


def _init_app():
    app = FastAPI()
    configura_exception_handler(app)
    configura_routers(app)
    return app


def configura_exception_handler(app):
    app.add_exception_handler(ApiBaseException, generic_handler)


def configura_routers(app):
    app.include_router(**conta_router)
    app.include_router(**correntista_router)
    app.include_router(**lancamento_router)


if __name__ == '__main__':
    app = _init_app()
    Database.criar_db()
    uvicorn.run(app, host='127.0.0.1', port=8000)
