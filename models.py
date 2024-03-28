from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Employee(db.Model):
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

class Attendance(db.Model):
    __tablename__ = 'attendance'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # Expecting values like "Present" or "Absent"
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

    def __repr__(self):
        return f'<Attendance {self.date}: {self.status} for Employee ID {self.employee_id}>'
