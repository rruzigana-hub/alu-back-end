# alu-back-end

## API project

This project uses a REST API to get employee data and TODO lists.
The scripts are written in Python 3 and use the `requests` module.
They show the data on the screen or save it in CSV and JSON files.

API used: https://jsonplaceholder.typicode.com

### Requirements

- Python 3
- The `requests` module
- Code style: PEP 8
- All files are executable and start with `#!/usr/bin/python3`

### Files (in the `api` directory)

| File | What it does |
| ---- | ------------ |
| `0-gather_data_from_an_API.py` | Shows the TODO list progress of an employee |
| `1-export_to_CSV.py` | Saves all tasks of an employee in `USER_ID.csv` |
| `2-export_to_JSON.py` | Saves all tasks of an employee in `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Saves the tasks of all employees in `todo_all_employees.json` |

### How to use

Go to the `api` directory. Then run a script with the employee ID:

    ./0-gather_data_from_an_API.py 2
    ./1-export_to_CSV.py 2
    ./2-export_to_JSON.py 2
    ./3-dictionary_of_list_of_dictionaries.py

### Example output

    $ ./0-gather_data_from_an_API.py 2
    Employee Ervin Howell is done with tasks(8/20):
    	 distinctio vitae autem nihil ut molestias quo
    	 voluptas quo tenetur perspiciatis explicabo natus
    	 ...

## Author

Ruzigana Irakiza Junior Raul (rruzigana-hub), African Leadership University
