#!/usr/bin/python3
"""
Getting employee name and tasks completed
"""
import json
import requests
import sys


def get_employee(ID):
    """Getting employee name and tasks completed"""

    ID = int(ID)
    employee = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{ID}"
        ).json()
    todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/"
        ).json()
    tasks = []
    employee_name = employee.get("name")

    employee_username = employee.get("username")
    if todo:
        for i in todo:
            if i["userId"] == ID:
                todo_id = {}
                todo_id["title"] = i["title"]
                todo_id["completed"] = i["completed"]
                tasks.append(todo_id)

    number_of_tasks = 0
    total_number_of_done_tasks = 0

    for i in tasks:
        number_of_tasks += 1
        if i.get("completed") is True:
            total_number_of_done_tasks += 1
    data = {ID:[]}
    for i in tasks:
        entry = {}
        entry["task"] = i["title"]
        entry["completed"] = i["completed"]
        entry["username"] = employee_username
        data[ID].append(entry)
    with open(f"{ID}.json", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_employee(int(sys.argv[1]))

