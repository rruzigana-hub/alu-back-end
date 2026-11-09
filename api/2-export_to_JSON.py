#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file."""
import json
import requests
import sys


def export_to_json(employee_id):
    """Save all tasks of the employee with this id in USER_ID.json."""
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()

    username = user.get("username")

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_json(int(sys.argv[1]))
