__author__="Vaibhav"
import uuid
from src.common.database import Database
import datetime
import uuid

class Equipment(object):

    def __init__(self,_id,name,type,Department_Id):
        self._id=_id
        self.name=name
        self.type=type
        self.Department_Id=Department_Id

    def save_to_mongo(self):
        Database.insert(collection='Equipment',
                        data=self.json())

    def json(self):
        return{
            '_id':self._id,
            'name':self.name,
            'type' : self.type,
            'Department_Id' : self.Department_Id
        }

    @staticmethod
    def delete_equipment(query):
        Database.delete_one_record(collection="Equipment",query={"_id" : query})

    @classmethod
    def get_equipments(cls):
        equipments = Database.find_collection(collection='Equipment')
        return [cls(**equipment) for equipment in equipments]
