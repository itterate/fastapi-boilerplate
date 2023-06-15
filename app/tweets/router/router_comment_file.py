from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from fastapi import Depends, HTTPException, Response

from ...utils import AppModel
from ..service import Service, get_service
from . import router

# client = MongoClient('<mongodb_connection_string>')


class createFileComments(AppModel):
    comment: str
    

@router.post("/files/{file_id}/comments")
def createcomment(
    id: str,
    comment_request: createFileComments,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> Response:
    user_id = jwt_data.user_id
    success = svc.comment_repository.create_comment(tweets_id=id, user_id=user_id, collection=request.dict())  
    if not success:
        raise HTTPException(status_code=404, detail=f"Could not insert")
    return Response(status_code=200)
        
