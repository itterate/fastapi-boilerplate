from typing import Any, List

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from app.utils import AppModel
from fastapi import Depends, Response
from pydantic import Field

from ..service import Service, get_service
from . import router


class GetMyTweetsTweet(AppModel):
    id: Any = Field(alias="_id")
    content: str
    room: int
    price: int


class GetMyTweetsResponse(AppModel):
    tweets: List[GetMyTweetsTweet]


@router.get("/{shanyrak_id:str}", response_model=GetMyTweetsResponse)
def get_shanyrak(
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyrak = svc.repository.get_shanyrak(shanyrak_id)
    if shanyrak is None:
        return Response(status_code=404)
    return GetMyTweetsResponse(**shanyrak)
