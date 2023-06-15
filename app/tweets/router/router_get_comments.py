# from datetime import datetime
from typing import Any, List

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from fastapi import Depends
from pydantic import Field

from ..service import Service, get_service
from . import router


class GetComments(AppModel):
    id: Any = Field(alias="_id")
    content: str
    created_at: str
    author_id: str
    

@router.get("get_comments", response_model=List[GetComments])
def get_comments(
    id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> List[GetComments]:
    comments = svc.comment_repository.get_list_of_comments(tweets_id = id)
    return [GetComments(**comment) for comment in comments]
        
    