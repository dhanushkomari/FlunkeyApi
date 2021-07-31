# Flunkey API.

## Installation steps.

**Create virtual environment in python by using Following command**
> _python3 -m venv NameOfTheEnvironment_

**Activate the virtual environment.**
> _Scripts\activate_

**Copy the project folder into env folder.**
**open terminal and change dir to project folder.**

**install the required libraries using the following command.**
>_pip install -r requirements.txt_

**Change directory to FlunkyProject folder.**
**Run the Following Commands.**
>_python3 manage.py runserver_

**To create DB and tables Deployment into database.**
>_python3 manage.py makemigrations_ 

>_python3 manage.py migrate_

>_python3 manage.py runserver_

## Working of Project on Local.
**Click on the Following link to open the Application**
>_http://127.0.0.1:8000_

**Select the Bot.**

**Select the table.**

**APi is generated with the bot and table details.**

## Handling Api using python requests

### TO GET API DATA, run the following script.
>_import requests_

>_a = request.get("http://127.0.0.1:8000/api-data/latest")_

>_b = a.json()_

>_print(b)_

## TO UPDATE, the TABLE and BOT use the following links.

>_requests.post('http://127.0.0.1:8000/api-data/update-bot/2', {'avialable': False})_

>_requests.post('http://127.0.0.1:8000/api-data/update-bot/2', {'avialable': False})_




