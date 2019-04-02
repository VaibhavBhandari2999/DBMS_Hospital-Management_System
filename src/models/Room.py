__author__="Vaibhav"
import uuid
from src.common.database import Database
import datetime
import uuid

class Room(object):

    def __init__(self,_id,room_type):
        self._id=_id
        self.room_type=room_type

    def save_to_mongo(self):
        Database.insert(collection='Room',
                        data=self.json())

    def json(self):
        return{
            '_id':self._id,
            'room_type':self.room_type
        }
    
    @staticmethod
    def delete_room(query):
        Database.delete_one_record(collection='Room',query={"_id" : query})
        
    @classmethod
    def get_rooms(cls):
        rooms = Database.find_collection(collection='Room')
        return [cls(**room) for room in rooms]


