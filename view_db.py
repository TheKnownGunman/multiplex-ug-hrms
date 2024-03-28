import sqlite3

def view_all_employees():
    # Adjust the path to match where your hrms.db file is located
    db_path = 'instance/hrms.db'

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Query to select all rows from the Employee table
    query = 'SELECT * FROM attendance'
    query1 = 'SELECT * FROM employee'
    
    try:
        cur.execute(query)
        employees = cur.fetchall()

        # Print column names
        columns = [description[0] for description in cur.description]
        print(columns)
        
        # Print each row in the table
        for employee in employees:
            print(employee)
        print("****************************")
        cur.execute(query1)
        att = cur.fetchall()

        # Print column names
        columns = [description[0] for description in cur.description]
        print(columns)
        
        # Print each row in the table
        for ate in att:
            print(ate)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection to the database
        conn.close()

if __name__ == '__main__':
    view_all_employees()
