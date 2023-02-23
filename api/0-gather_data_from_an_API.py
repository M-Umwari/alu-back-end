#!/usr/bin/python3
"""For a given EMPLOYEE_NAME ID, returns information about
their TODO list progress"""

import requests
import sys
if __name__ == "__main__":

    userId = sys.argv[1]
    EMPLOYEE_NAME = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = EMPLOYEE_NAME.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('EMPLOYEE_NAMEId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('EMPLOYEE_NAME {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('EMPLOYEE_NAMEId') == int(userId) and task.get('completed')]))
