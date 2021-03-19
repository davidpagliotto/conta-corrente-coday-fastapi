from http.client import HTTPException

from starlette.requests import Request
from starlette.responses import JSONResponse


class ApiBaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self, status_code=500, detail=None) -> None:
        self.status_code = status_code
        self.detail = detail


async def generic_handler(_: Request, exception: ApiBaseException):
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": exception.detail}
    )
