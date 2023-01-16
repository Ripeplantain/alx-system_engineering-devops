"""
    Accessing a list of employees from a todo rest api
"""

import requests 
import sys

if __name__ == "__main__":
    employeeID = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/todos"
    url = baseUrl + "/" + employeeID

    response = requests.get(url)
    employee_name = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if tasks.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks {}/{}".format(employee_name,done,len(done_tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))