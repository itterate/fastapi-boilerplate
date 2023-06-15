from typing import Any
# import imghdr

from fastapi import Depends, Field, Response, HTTPException

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class update_comments_file(AppModel):
    id: Any = Field(alias="_id")
    content: str
    
    
@router.patch("Update_comments", response_model = update_comments_file)
def new_comment(
    id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service), 
    
) -> dict[str, str]:
    success = svc.comment_repository.update_comments(user_id = id, content = content)
    if success.modified_count == 1:
        return Response(status_code=200)
    raise HTTPException(status_code=404, detail=f"Shanyrak {id} not found")