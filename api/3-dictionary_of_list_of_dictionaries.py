#!/usr/bin/python3
"""
Getting employee name and tasks completed
"""
import json
import requests
import sys


def get_employee():
    """Getting employee name and tasks completed"""
    employees = requests.get(
        f"https://jsonplaceholder.typicode.com/users/"
        ).json()
    todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/"
        ).json()

    todo_all_employees = {}

    for i in range(len(employees)):
        entry = []
        for j in todo:
            if j["userId"] == i + 1:
                username = employees[i].get("username")
                task = j["title"]
                completed = j["completed"]

                entry2 = {}
                entry2["username"] = username
                entry2["task"] = task
                entry2["completed"] = completed

                entry.append(entry2)
        todo_all_employees[f"{i + 1}"] = entry

    with open("to_do_all_employees.JSON", "w") as file:
        json.dump(todo_all_employees, file, indent=4)


if __name__ == "__main__":
    get_employee()
