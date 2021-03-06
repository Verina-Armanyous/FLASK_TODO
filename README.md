# Flask Kanban Board 
A Kanban board is a simple form of task management. Every task that you add can be in one of three states:
- Todo
- Doing
- Done

It also supports the following functionalities:
- Creating a new task and selecting its state 
- Moving tasks to different states
- Deleting tasks

![ezgif-7-c8dd76fb5ebc](https://user-images.githubusercontent.com/47928071/111052764-c4257900-8412-11eb-91f9-80345392aee3.gif)

##### Requirements
* Python 3
* Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3

### Steps to run the app: 
##### 1- Installation of virtual environment
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### 2- Create virtual environment
Creation of virtualenv:

    $ python3 -m venv venv
##### 3- Activate virtual environment
To activate the virtualenv:

    $ source venv/bin/activate

Or, if you are **using Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

    $ venv\Scripts\activate

To deactivate the virtualenv (after you finished working):

    $ deactivate
##### 4- Install dependencies
Install dependencies in virtual environment:

    $ pip3 install -r requirements.txt


##### 5- Start the server

Start the server by running:

    $ python3 app.py

## Unit Tests
To run the unit tests use the following commands:

    $ python3 -m venv venv_unit
    $ source venv_unit/bin/activate
    $ pip3 install -r requirements.txt
    $ export DATABASE_URL='sqlite:///web.db'
    $ python3 unittesting.py
