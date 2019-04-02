__author__="Vaibhav"
import uuid
from src.common.database import Database
import datetime
import uuid

class Department(object):

    def __init__(self,_id,Department_Name,Fields):
        self._id = _id
        self.Department_Name=Department_Name
        self.Fields=Fields

    def save_to_mongo(self):
        Database.insert(collection='Department',
                        data=self.json())
    def json(self):
        return{
            '_id':self._id,
            'Department_Name':self.Department_Name,
            'Fields' : self.Fields
            }
    
    def delete_department(query):
        Database.delete_one_record(collection="Department",query={"_id" : query})
    
    @classmethod
    def get_departments(cls):
        departments = Database.find_collection(collection='Department')
        return [cls(**department) for department in departments]
