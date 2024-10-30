# Backend

## 1. Installation Process
We will use [Poetry](https://python-poetry.org/) as the package manager for our project. This tool allows us to define the basic properties of the project and its dependencies.

The project definition can be found in the file [pyproject.toml](./backend/pyproject.toml). If you review it, you will see that it includes both project information (name, version, etc.) and the list of dependencies needed.

The first thing we need to do is install Poetry. You can follow the updated instructions in their [documentation](https://python-poetry.org/docs/#installation), or use the manual installer:

**Linux, macOS, Windows (WSL)**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
**Windows (PowerShell)**
```PowerShell
curl -sSL (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

We can verify that the installation was successful by running:
```bash
poetry --version
```

This should display the current version: ```Poetry (version 1.8.2)```. Now we can create a virtual environment with everything our project needs. To do this, we navigate to the backend directory and run:
```bash
poetry install
```
If we have already installed the dependencies but need to add some, we can update the environment using:
```bash
poetry update
```
Now we can see all the information about our virtual environment with:
```bash
poetry env info
```
Open a Python interpreter within this environment:
```bash
poetry shell
```
Activate the environment to be our default:
```bash
poetry env use
```
Or run any command within the environment:
```bash
poetry run <command>
```

### 2. Backend Configuration
We will configure our application via an environment file ```.env```. This file will contain sensitive information, such as passwords, so we must ensure that it is not stored in the code repository (GitHub). You can check that the ```.gitignore``` file contains a line for this file, making it ignored.

Create a new file at the root of the project named ```.env```, and add the following content (replacing the XXX with values you consider appropriate):
```dotenv
PROJECT_NAME=BookHub
FIRST_SUPERUSER=XXXX
FIRST_SUPERUSER_PASSWORD=XXXX
BACKEND_CORS_ORIGINS=http://localhost:8080

HOST = hosturl
USERDB = userdatabase
PASSWORD = passwordatabase
DATABASE = database
```
### 3. Creating the Database
The database used for development will be [SQL](https://www.sqlite.org/). 
This database system has the peculiarity that it only requires a file and is very lightweight. 
The models of our application are defined in the Python package **app.models** in the backend. 
We will use a migration management system called [Alembic](https://alembic.sqlalchemy.org/), which will allow us to update 
the database as our project progresses and the model changes.

### 4. Start the Backend
Ro start the backend do this, run the command:

```bash
poetry run uvicorn app.main:app
```

If we are making changes, we can add the parameter ```--reload``` so that changes made to the code are automatically applied:

```bash
poetry run uvicorn app.main:app --reload
```

Additionally, we can select a different port by adding ```--port #port``` or make it listen for connections from other machines using ```--host 0.0.0.0```.

## 5. Execution
```bash
cd website_project_a2/backend
poetry install
poetry run uvicorn app.main:app --reload
```