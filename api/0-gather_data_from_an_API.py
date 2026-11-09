#!/usr/bin/python3
"""Gather data from an API: show an employee's TODO list progress."""
import requests
import sys


def get_todo_progress(employee_id):
    """Print the TODO list progress of the employee with this id."""
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()

    name = user.get("name")
    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_todo_progress(int(sys.argv[1]))
