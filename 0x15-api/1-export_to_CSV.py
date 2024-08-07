#!/usr/bin/python3
"""
This script fetches and displays the todo list progress
for a given employee ID using a REST API.
"""

import csv
import requests
import sys


def get_progress(employee_id):
    """Fetches and displays the todo list progress for an employee by ID."""
    try:
        # Fetch data
        website = 'https://jsonplaceholder.typicode.com'
        user_url = '{}/users/{}'.format(website, employee_id)
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todos_url = '{}/todos?userId={}'.format(website, employee_id)
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Extract user name
        employee_name = user_data.get('name')

        # Get the number of completed tasks
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task.get(
            'completed')]
        number_of_done_tasks = len(completed_tasks)

        # Print the list progress
        """print(
            f"Employee {employee_name} is done with tasks"
            f"({number_of_done_tasks}/{total_tasks}):"
        )
        for task in completed_tasks:
            print(f"\t {task.get('title')}")"""

        file_name = '{}.csv'.format(employee_id)
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            username = user_data.get('username')
            for task in todos_data:
                writer.writerow(
                    [employee_id, username, task.get('completed'), task.get(
                        'title')])

    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except KeyError as e:
        print(f"Invalid response data: {e}")
    except ValueError as e:
        print(f"Invalid JSON data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_progress(employee_id)
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)
