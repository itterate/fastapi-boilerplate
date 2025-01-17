# from typing import Any

from fastapi import Depends, Response
# from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
# from app.utils import AppModel

from ..service import Service, get_service

from . import router


# class GetMyTweetsTweet(AppModel):
#     id: Any = Field(alias="_id")
#     content: str
#     room: int


@router.delete("/{shanyrak_id:str}")
def delete_shanyrak(
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    delete_result = svc.repository.delete_shanyrak(shanyrak_id)
    # , jwt_data.user_id
    if delete_result.deleted_count == 1:
        return Response(status_code=200)
    return Response(status_code=404)
   