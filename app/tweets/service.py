from app.config import database

from .repository.repository import TweetRepository

from .adapter.s3_service import S3Service


class Service:
    def __init__(
        self,
        repository: TweetRepository,
        
    ):
        self.repository = repository
        self.s3_service = S3Service()


def get_service():
    repository = TweetRepository(database)

    svc = Service(repository)
    return svc


