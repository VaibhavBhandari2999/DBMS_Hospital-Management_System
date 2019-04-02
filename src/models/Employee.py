__author__="Vaibhav"
import uuid
from src.common.database import Database
import datetime
import uuid

class Employee(object):

    def __init__(self,_id,password,name,Contact_number,Gender,Date_of_Birth,Date_of_Joining=None):
        self._id=_id
        self.password=password
        self.name=name
        self.Contact_number=Contact_number
        self.Gender=Gender
        self.Date_of_Joining=datetime.datetime.utcnow() if Date_of_Joining is None else Date_of_Joining
        self.Date_of_Birth=Date_of_Birth

    def save_to_mongo(self):
        Database.insert(collection='Employee',
                        data=self.json())

    def json(self):
        return{
            '_id':self._id,
            'name':self.name,
            'password':self.password,
            'Contact_number' : self.Contact_number,
            'Gender' : self.Gender,
            'Date_of_Joining' : self.Date_of_Joining,
            'Date_of_Birth' : self.Date_of_Birth
        }
    @classmethod
    def from_id(cls,id):
        data = Database.find_one("Employee", {"_id": id})
        if data is not None:
            print(data)
            return cls(**data)
    
    @staticmethod
    def delete_employee(query):
        Database.delete_one_record(collection="Employee",query={"_id" : query})

    @classmethod
    def get_employees(cls):
        employees = Database.find_collection(collection='Employee')
        return [cls(**employee) for employee in employees]

#Database.initialize()
#employee = Employee('EMP1000','password','Vaibhav Bhandari',9945216957,'Male','29-APR-1999')
#employee.save_to_mongo()