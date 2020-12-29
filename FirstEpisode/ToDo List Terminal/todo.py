#!/usr/bin/env python
from pprint import pprint

import click
import json
import os
from PyInquirer import prompt, Separator

SAVE_FILE = 'data.txt'
data = {}


@click.group()
def cli():
    pass


@cli.command()
@click.option('-t', '--task',
              prompt='New task',
              required=True,
              help='The task you would like to do later')
def add(task):
    print(f'Saved new todo named {task}')
    data['tasks'] += [{'task': task}]
    save_data()


@cli.command()
def done():
    questions = [
        {
            'type': 'checkbox',
            'qmark': '📒',
            'message': 'What did you accomplish?',
            'name': 'tasks',
            'choices': [{'name': item['task']} for item in data['tasks']]
        }
    ]
    answers = prompt(questions)
    completed_tasks = answers['tasks']
    data['tasks'] = list(filter(lambda x: not (x['task'] in completed_tasks), data['tasks']))
    save_data()


@cli.command()
def plan():
    print('Tasks for today:')
    tasks = [item['task'] for item in data['tasks']]
    for task in tasks:
        print(f'🔵 {task}')


def save_data():
    with open(SAVE_FILE, 'w') as json_file:
        global data
        json.dump(data, json_file)


def read_data():
    with open(SAVE_FILE) as json_file:
        global data
        data = json.load(json_file)


def init_save():
    global data
    data = {
        'tasks': [],
    }
    with open(SAVE_FILE, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    if not os.path.isfile(SAVE_FILE):
        init_save()
    read_data()
    cli()
