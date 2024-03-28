# hrms-management-App

This hrms management application is designed to manage employee information in a company for hr managers, which can adding new employees, retrieving their informations and marking their attendance. This application is developed with flask, a lite use web-app framework availabe in python and uses sqlite for managing the database.

##  Description

This hrms app is designed with pythom famework flask, which helps the hr managers in an organization to do their company's employee managment by adding new employees to the database, tracking their daily attendance and retrieving department-wise employee details, etc.

### Features

- **Employee Management**: Add and view employee details.
- **Attendance Tracking**: Mark daily attendance for each employees.
- **Department Report**: Generate reports showing the number of employees in each department, with table and bar chart.

## Project structure

This is the basic overview of the project structure:

│
├── instance/
│ └── hrms.db # SQLite database file

├── static/ # Static files directory
│ └── styles.css # CSS file for styling the application

├── templates/ # Templates directory for Jinja2 HTML templates
│ ├── add_employee.html # Template for adding a new employee
│ ├── base.html # Base template for inheriting common structures
│ ├── department_report.html# Template for departmental report and charts
│ ├── employee_attendance.html # Template for employee attendance details
│ ├── employee_list.html # Template for listing employees
│ ├── home.html # Template for the homepage
│ └── mark_attendance.html # Template for marking employee attendance

├── venv/ # Virtual environment directory for project dependencies
├── requirements.txt # Lists all Python dependencies for the project
├── .gitignore # Specifies intentionally untracked files to ignore
├── app.py # Main application file with Flask routes and all functions
├── models.py # Defining the db models
└── view_db.py # script to view contents of the database

## API Endpoints and Routes

- `GET /`: The home page which lists all employees.

- `GET /employee/add`: Displays a form to add a new employee.

- `POST /employee/add`: Submits the form data to add a new employee to the database.
  - Request body contains employee details such as `name`, `designation`, `department`, etc.

- `GET /employee/list`: Lists all employees with their details.
 - `GET /attendance/mark/<employee_id>`: Displays a form to mark attendance for that employee.

- `POST /attendance/mark/<employee_id>`: Submits attendance data for the specified employee.
  - URL parameter: `employee_id` (integer) — The ID of the employee for whom attendance is being marked.
  - 
- `GET employee/<employee_id>/attendance`: Displays a attendance of specific employee.

- `GET /department-report`: Shows a report with the count of employees in each department.
  
