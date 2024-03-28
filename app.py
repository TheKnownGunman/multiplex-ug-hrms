from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hrms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hkjdqjdkj83998423rhjqkw'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Employee(db.Model):
    """
    Attributes:
        id (int): The id for the employee.
        name (str): The name of the employee.
        designation (str):  employee's job designation.
        department (str):  department the employee belongs to.
        date_of_joining (datetime):  date the employee joined the company.
        attendances (relationship): A dynamic relationship to the employee's attendance data.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    date_of_joining = db.Column(db.DateTime, default=datetime.utcnow)
    attendances = db.relationship('Attendance', backref='employee', lazy='dynamic')

class Attendance(db.Model):

    """
    Attributes:
        id (int): The unique identifier for the attendance record.
        date (date): The date of the attendance record.
        status (str): The attendance status, e.g., "Present" or "Absent".
        employee_id (int): The identifier of the employee this record belongs to.
    """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # "Present" or "Absent"
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

@app.route('/')
def home():
    employees = Employee.query.all()
    return render_template('home.html', employees=employees)

@app.route('/employee/add', methods=['GET', 'POST'])
def add_employee():
    
    """
    For GET requests: 
        Renders an employee addition form.
    For POST requests:
        Processes the submitted form and adds a new employee to the database.

    Returns:
        On POST: A redirect to the home page upon successful form submission.
        On GET: The add_employee.html template rendered.
    """

    if request.method == 'POST':
        new_employee = Employee(
            name=request.form['name'],
            designation=request.form['designation'],
            department=request.form['department'],
            date_of_joining=datetime.strptime(request.form['date_of_joining'], '%Y-%m-%d')
        )
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_employee.html')

# Define route and function to mark attendance of an employee
@app.route('/attendance/mark/<int:employee_id>', methods=['GET', 'POST'])
def mark_attendance(employee_id):

    """
    For GET requests:
        Renders the attendance marking form for the specified employee.
    For POST requests:
        Processes the submitted attendance form and adds the record to the database.

    Parameters:
        employee_id (int): The unique identifier of the employee for whom to mark attendance.

    Returns:
        On POST: A redirect to the home page upon successful form submission.
        On GET: The mark_attendance.html template rendered for the specified employee.
    """

    employee = Employee.query.get_or_404(employee_id)
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        status = request.form['status']
        attendance = Attendance(date=date, status=status, employee_id=employee_id)
        db.session.add(attendance)
        db.session.commit()
        flash('Attendance marked successfully!', 'success')
        return redirect(url_for('home'))

    # For GET request, render mark_attendance.html
    return render_template('mark_attendance.html', employee=employee)

# define route and function for viewing the attendance of an employee
@app.route('/employee/<int:employee_id>/attendance')
def employee_attendance(employee_id):

    """
    A route to view attendance data for an employee.

    Parameters:
        employee_id (int): The id of the employee.

    Returns:
        The employee_attendance.html template rendered with attendance records of the employee.
    """
    
    employee = Employee.query.get_or_404(employee_id)
    attendance_records = employee.attendances.all()
    return render_template('employee_attendance.html', employee=employee, attendance_records=attendance_records)

# Define a function to show the list of employee to mark attendace
@app.route('/attendance/list')
def list_employees():

    """
    A route to list all employees when 'mark attendance' button is clicked.

    Returns:
        The employee_list.html template rendered with a list of employees.
    """
    employees = Employee.query.all()
    return render_template('employee_list.html', employees=employees)

#Defining a route and function for showing the employee count by department
@app.route('/reports/department')
def department_report():
    """
    A route to generate and display a report of the employee count by department as a table and a chart.

    Returns:
        The department_report.html template rendered with the department report.
    """
    report = db.session.query(
        Employee.department, db.func.count(Employee.id)
    ).group_by(Employee.department).all()
    departments = [result[0] for result in report]
    counts = [result[1] for result in report]
    return render_template('department_report.html', report=report)

if __name__ == '__main__':
    app.run(debug=True)
