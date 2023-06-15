from datetime import datetime
from typing import Any, List

from bson.objectid import ObjectId
from fastapi import HTTPException
from pymongo.database import Database
from pymongo.results import UpdateResult


class TweetRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_tweet(self, input: dict):
        payload = {
            "content": input["content"],
            "price": input["price"],
            "user_id": ObjectId(input["user_id"]),
            "created_at": datetime.utcnow(),
        }

        self.database["tweets"].insert_one(payload)

    def get_tweet_by_user_id(self, user_id: str) -> List[dict]:
        tweets = self.database["tweets"].find(
            {
                "user_id": ObjectId(user_id),
            }
        )
        result = []
        for tweet in tweets:
            result.append(tweet)

        return result
    
    def update_tweet(self, shanyrak_id: str, user_id: str,
                     dict: dict[str, Any]):
        self.database["users"].update_one(
            filter={"_id": ObjectId(shanyrak_id, user_id)},
            update={
                "$set": {
                    "phone": dict["phone"],
                    "name": dict["name"],
                    "city": dict["city"],
                }
            },
        )
        
    def create_comment(self, tweets_id: str, user_id: str, collection: dict):
        collection["tweets_id"] = ObjectId(tweets_id)
        collection["author_id"] = user_id
        collection["created_at"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        tweet = self.database["tweets"].find_one({"_id": ObjectId(tweets_id)})
        if not tweet:
            raise HTTPException(status_code=404, detail=f"Could find shanyrak with id {tweets_id}")
        collection["user_id"] = ObjectId(user_id)
        insert_result = self.database["comments"].insert_one(collection)
        return insert_result.acknowledged
    
    def get_list_of_comments(self, tweets_id: str) -> List[dict]:
        comments = self.database["comments"].find({"shanyrak_id": ObjectId(tweets_id)})
        return list(comments) 
    
    def update_comments(self, user_id: str, content: str) -> UpdateResult:
        return self.database("content".update_one({"user": ObjectId(user_id)}), {"$set": content})
        
        
