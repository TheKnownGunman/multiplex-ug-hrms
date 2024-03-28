# import necessary python packages
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#initialize the sql database
db = SQLAlchemy()

#Define the class Employee which creates Employee table and to return it 
class Employee(db.Model):

    """
    Represents an Employee in the HRMS system.

    Attributes:
        id (int): Unique identifier for the employee.
        name (str): Name of the employee.
        designation (str): Job designation of the employee.
        department (str): Department where the employee works.
        date_of_joining (datetime): The date when the employee joined the company.
        attendances (relationship): A dynamic relationship to the employee's attendance records.
        
    The Employee model includes basic information about the employee such as name, designation, 
    and department, as well as a relationship to their attendance records.
    """

    __tablename__ = 'employee'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    date_of_joining = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to Attendance records
    attendances = db.relationship('Attendance', backref='employee', lazy='dynamic')

    def __repr__(self):
        return f'<Employee {self.name}, {self.designation}, {self.department}>'
# Initialze a class attendance to create that table and returning the table data
class Attendance(db.Model):

    """
    Represents an Attendance record for an Employee in the HRMS system.

    Attributes:
        id (int): Unique identifier for the attendance record.
        date (datetime.date): The date of the attendance.
        status (str): Attendance status ("Present" or "Absent").
        employee_id (int): The ID of the employee to which the attendance record belongs.
        
    The Attendance model tracks the attendance status of employees on specific dates and is 
    linked to the Employee model via a foreign key.
    """
    
    __tablename__ = 'attendance'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # Expecting values like "Present" or "Absent"
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

    def __repr__(self):
        return f'<Attendance {self.date}: {self.status} for Employee ID {self.employee_id}>'
