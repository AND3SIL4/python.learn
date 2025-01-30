# This repository was created in order to store the basic concepts in Python language

## Python completely tech stack

### Best practices

- **Python packages**: uv

  ```sh
  brew install uv
  uv init [project_name]
  cd [project_name]
  uv add --dev [dependency] # uv add ruff, create automatily the virtual environment
  uv tool install [dependency] # to install any dependency
  uv tool upgrade [dependency]
  uv tree # see the tree of dependencies installed
  uv run [dependency] check # check for updates of the dependency
  uvx [dependency] # for running packages, it's a shorcut for 'uv tool run [dependency]'
  ```

- **Linter**: ruff

  ```sh
  ruff check [file (optional)] # validate if the file are correct or not
  ruff check [file (optional)] --fix # fix the inconsistencies into file
  ruff format [file (optional)] # to format after fixing linter validation
  ```

- **Configuration file**: pyproject.toml

  ```toml
    # Config base file
    [project]
    name = "basic-fastapi"
    version = "0.1.0"
    description = "Add your description here"
    readme = "README.md"
    requires-python = ">=3.13"
    dependencies = []

    [dependency-groups]
    dev = [
        "ruff>=0.9.3",
    ]

    # Ruff config file in this root location
    # ruff.toml

    # custom scripts
    [project.scripts]
  ```

### Technologies

- **Backend**: FastApi

  ```sh
  uv add fastapi --extra standard # for adding the dependencies in pyproject.toml
  uv run fastapi dev # it should contain the main.py file
  ```

  ```txt
  project
    └── app
        ├── __init__.py
        ├── main.py
        ├── dependencies.py
        ├── routers
        │   ├── __init__.py
        │   ├── items.py
        │   └── users.py
        └── internal
            ├── __init__.py
            └── admin.py
  ```

  ```sh
  # Activate the virtual environment
  source ./venv/bin/activate
  # Deactivate the virtual environment
  deactivate
  ```

## Here is the order of exercises at each level follow up by roadmap.sh

1. Beginner

- [task tracker](https://roadmap.sh/projects/task-tracker)

2. Intermediate

-

3. Advanced

-
