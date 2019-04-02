__author__="Vaibhav"
import uuid
from src.common.database import Database
import datetime
import uuid

class Doctor(object):

    def __init__(self,_id,Employee_id,Department_id):
        self._id=_id
        self.Employee_id=Employee_id
        self.Department_id=Department_id

    def save_to_mongo(self):
        Database.insert(collection='Doctor',
                        data=self.json())

    def json(self):
        return{
            '_id':self._id,
            'Employee_id':self.Employee_id,
            'Department_id' : self.Department_id
        }
    
    def delete_doctor(query):
        Database.delete_one_record(collection="Doctor",query={"_id" : query})
        
    @classmethod
    def get_doctors(cls):
        doctors = Database.find_collection(collection='Doctor')
        return [cls(**doctor) for doctor in doctors]
