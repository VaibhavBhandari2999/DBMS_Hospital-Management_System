from src.common.database import Database
from src.models.Employee import Employee
from src.models.Patient import Patient
from src.models.Department import Department
from src.models.Equipment import Equipment
from src.models.Room import Room
from src.models.Doctor import Doctor
from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)
app.secret_key = "Vaibhav"
Database.initialize()
@app.route('/')
def main_template():
    #return make_response(dep_show())
    return render_template('Main.html')

@app.route('/login')
def emp_login_template(message=None):
    return render_template('Emp_login.html',message = message if message is not None else None)

@app.route('/auth/login', methods=['POST'])
def login_employee():
    username = request.form['Username']
    password = request.form['Password']
    employee = Employee.from_id(username)
        #print(User.login_vaild(email,password))
    if employee is not None:
        if employee.password == password:
            session['email'] = username
            print(password)
            return render_template('trial.html')

    else:
        session['email'] = None
    return make_response(emp_login_template("Incorrect login Please try again"))

@app.route('/Emp_add',methods=['POST','GET'])
def emp_add():
    if request.method == 'GET':
        return render_template('Employee_add.html')
    else:
        name = request.form['Emp_name']
        password=request.form['Emp_pass']
        Gender=request.form['Emp_gender']
        Contact_number=request.form['Emp_pno']
        _id=request.form['Emp_ID']
        Date_of_Birth=request.form['Emp_DoB']
        employee = Employee(_id,password,name,Contact_number,Gender,Date_of_Birth,None)
        employee.save_to_mongo()
        #message = "Successful"
        return render_template('trial.html',message = "Successfull")

@app.route('/Emp_del',methods=['POST','GET'])
def emp_del(message=None):
    if request.method == 'GET':
        return render_template('Employee_del.html')
    else:
        del1=request.form['Emp_del_id']
        Employee.delete_employee(del1)
        return render_template('Employee_del.html',message = "Succesful")

@app.route('/Emp_upd')
def emp_upd(message=None):
    return render_template('Employee_update.html',message = "Successful")

@app.route('/Pat_add',methods=['POST','GET'])
def pat_add():
    if request.method == 'GET':
        return render_template('Patient_add.html')
    else:
        Name=request.form['Pat_name']
        gender=request.form['Pat_gender']
        phone_no=request.form['Pat_pno']
        Date_of_Birth=request.form['Pat_DoB']
        Room_no=request.form['Pat_room']
        Doctor_Id=request.form['Pat_Doc_id']
        _id=request.form['Pat_ID']
        Equipment_Id=request.form['Pat_eqid']
        patient=Patient(_id,Name,Date_of_Birth,gender,phone_no,Room_no,Doctor_Id,Equipment_Id)
        patient.save_to_mongo()
        return render_template('trial.html',message = "Successful")

@app.route('/Pat_del',methods=['POST','GET'])
def pat_del(message=None):
    if request.method == 'GET':
        return render_template('Patient_del.html')
    else:
        del1 = request.form['Pat_del_id']
        Patient.delete_patient(del1)
        return render_template('trial.html',message = "Successful")

@app.route('/Pat_upd')
def pat_upd(message=None):
    return render_template('Patient_update.html',message = "Successful")

@app.route('/Dep_add',methods=['POST','GET'])
def dep_add(message=None):
    if request.method == 'GET':
        return render_template('Department_add.html')
    else:
        _id=request.form['Dept_id']
        Department_Name=request.form['Dept_name']
        Fields=request.form['Dept_field']
        dept=Department(_id,Department_Name,Fields)
        dept.save_to_mongo()
        return render_template('trial.html',message = "Successful")

@app.route('/Dep_del',methods=['POST','GET'])
def dep_del(message=None):
    if request.method == 'GET':
        return render_template('Department_del.html')
    else:
        del1=request.form['Dept_del_id']
        Department.delete_department(del1)
        return render_template('trial.html',message = "Successful")

@app.route('/Dep_upd')
def dep_upd(message=None):
    return render_template('Department_update.html',message = "Successful")

@app.route('/Room_add',methods=['POST','GET'])
def room_add(message=None):
    if request.method == 'GET':
        return render_template('Room_add.html')
    else:
        _id=request.form['Room_room']
        room_type=request.form['Room_type']
        room=Room(_id,room_type)
        room.save_to_mongo()
        return render_template('trial.html',message = "Successful")


@app.route('/Room_del',methods=['POST','GET'])
def room_del(message=None):
    if request.method == 'GET':
        return render_template('Room_del.html')
    else:
        del1=request.form['Room_del_id']
        Room.delete_room(del1)
        return render_template('trial.html',message = "Successful")

@app.route('/Room_upd')
def room_upd(message=None):
    return render_template('Room_update.html',message = "Successful")

@app.route('/Equip_add',methods=['POST','GET'])
def equip_add(message=None):
    if request.method == 'GET':
        return render_template('Equipment_add.html')
    else:
        _id=request.form['Equip_no']
        name=request.form['Equip_name']
        type=request.form['Equip_type']
        Department_Id=request.form['Equip_dept_id']
        equip=Equipment(_id,name,type,Department_Id)
        equip.save_to_mongo()
        return render_template('trial.html',message = "Successful")

@app.route('/Equip_del',methods=['POST','GET'])
def equip_del(message=None):
    if request.method == 'GET':
        return render_template('Equipment_del.html')
    else:
        del1=request.form['Eq_del_id']
        Equipment.delete_equipment(del1)
        return render_template('trial.html',message = "Successful")

@app.route('/Equip_upd')
def equip_upd(message=None):
    return render_template('Equipment_update.html',message = "Successful")

@app.route('/Doc_add',methods=['POST','GET'])
def doc_add(message=None):
    if request.method == 'GET':
        return render_template('Doctor_add.html')
    else:
        _id=request.form['Emp_id']
        Employee_id=request.form['Emp_doc_id']
        Department_id=request.form['Emp_dept_id']
        doc=Doctor(_id,Employee_id,Department_id)
        doc.save_to_mongo()
        return render_template('trial.html',message = "Successful")

@app.route('/Doc_del',methods=['POST','GET'])
def doc_del(message=None):
    if request.method == 'GET':
        return render_template('Doctor_del.html')
    else:
        del1=request.form['Doc_del_id']
        Doctor.delete_doctor(del1)
        return render_template('trial.html',message = "Successful")

@app.route('/Doc_upd')
def doc_upd(message=None):
    return render_template('Doctor_update.html',message = "Successful")

@app.route('/Dep_show',methods=['GET'])
def dep_show():
    departments = Department.get_departments()
    return  render_template('Department_show.html',departments = departments)

@app.route('/Equip_show',methods=['GET'])
def equip_show():
    equipments = Equipment.get_equipments()
    return  render_template('Equipment_show.html',equipment = equipments)

@app.route('/Emp_show',methods=['GET'])
def emp_show():
    employees = Employee.get_employees()
    return  render_template('Employee_show.html',employees = employees)

@app.route('/Doc_show',methods=['GET'])
def doc_show():
    doctors = Doctor.get_doctors()
    return  render_template('Doctor_show.html',doctors = doctors)
    
if __name__=='__main__':
    app.run(port=4995)
