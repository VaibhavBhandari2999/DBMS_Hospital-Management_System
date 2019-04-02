__author__="Vaibhav"
import uuid
from src.common.database import Database
import datetime
import uuid

class Patient(object):

    def __init__(self,_id,Name,Date_of_Birth,gender,phone_no,Room_no,Doctor_Id,Equipment_Id):
        self._id=_id
        self.Name=Name
        self.Date_of_Birth=Date_of_Birth
        self.gender=gender
        self.phone_no=phone_no
        self.Room_no=Room_no
        self.Doctor_Id=Doctor_Id
        self.Equipment_Id=Equipment_Id

    def save_to_mongo(self):
        Database.insert(collection='Patient',
                        data=self.json())

    def json(self):
        return{
            '_id':self._id,
            'Name':self.Name,
            'Date_of_Birth' : self.Date_of_Birth,
            'gender' : self.gender,
            'phone_no' : self.phone_no,
            'Room_no' : self.Room_no,
            'Doctor_Id':self.Doctor_Id,
            'Equipment_Id':self.Equipment_Id
        }
    
    @staticmethod
    def delete_patient(query):
        Database.delete_one_record(collection='Patient',query={"_id" : query})
        
    @classmethod
    def get_patients(cls):
        patients = Database.find_collection(collection='Patient')
        return [cls(**patient) for patient in patients]
