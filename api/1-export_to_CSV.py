#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file."""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Save all tasks of the employee with this id in USER_ID.csv."""
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()

    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(
            csv_file, quoting=csv.QUOTE_ALL, lineterminator="\n")
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_csv(int(sys.argv[1]))
