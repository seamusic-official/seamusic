import pydantic
from fastapi import Request, Depends
from starlette.responses import Response
from sqlalchemy.sql.functions import current_user

from src.exceptions import services, api
from src.schemas.auth import User


class V1ExceptionsMiddleware:
    async def __call__(self, request: Request, call_next, user: User | None = Depends(current_user)) -> Response:
        if not user:
            raise api.UnauthorizedException()

        try:
            response = await call_next(request)

        except services.InvalidRequestException or pydantic.ValidationError:
            raise api.InvalidRequestException()
        except services.NoRightsException:
            raise api.NoRightsException()
        except services.NotFoundException():
            raise api.NotFoundException()
        except services.ServerError() as e:
            raise api.CustomException(status_code=500, detail=e.detail)

        return response


class V1AuthExceptionsMiddleware:
    async def __call__(self, request: Request, call_next) -> Response:
        try:
            response = await call_next(request)
        except services.InvalidRequestException or pydantic.ValidationError:
            raise api.InvalidRequestException()
        except services.NoRightsException:
            raise api.NoRightsException()
        except services.NotFoundException():
            raise api.NotFoundException()
        except services.ServerError() as e:
            raise api.CustomException(status_code=500, detail=e.detail)

        return response
