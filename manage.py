import subprocess
from settings.settings import BASE_DIR

def quit_program():
    quit()


while True:
    operation = input(
        '1. init the project \n2. running the flask app\n0. quit\n\nSelect an operation: >>> ')
    if operation == '1':
        # Run main.py
        subprocess.run(["python",f"{BASE_DIR}/modules/main.py"])
        print('DateBase is created successfully\n')

        # Run add_update_countries.py
        print('Adding the countries to database.')
        subprocess.run(["python3",f"{BASE_DIR}/modules/add_update_countries.py"])
        print('Done\n')

        # Run add_ip_perfix.py
        print('Adding the ip perfixes to database.')
        subprocess.run(["python3",  f"{BASE_DIR}/modules/add_ip_perfix.py"])
        print('Done\n')

        # Run add_ip_country.py
        print('Adding the ip countries to database.')
        subprocess.run(["python3", f"{BASE_DIR}/modules/adding_ip_country.py"])
        print('Done\n')

    elif operation == '2':
        # Run flask_app.py
        print('Running the flask app')
        subprocess.run(["python3",f"{BASE_DIR}/modules/flask_app.py"])
        print('Done\n')

    else:
        quit_program()
