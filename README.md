## Project Assistant (v2)

### About the project

A basic financial control application custom designed for a non-profit organisation that allows members to manage and compare European Commission-funded project budgets.
Its purpose is to alleviate the reliance on multiple spreadsheets for tracking project budgets and to streamline financial processes.

**Core features of application**

- Project budget management and automated budget statistics 
- Built-in currency conversion utilizing the European Central Bank's API
- Member profiles with customizable dashboards and notifications
- Different authorization levels and budget change approval chains

**Personal goals**

- Learning a new stack - Python / Flask 
- Practicing containerization and building CI/CD pipeline
- Practicing process automation and optimization with scripts
- Advancing my learning process in AWS resources

### Built with

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br>
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) <br>
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) <br>
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

### Dependencies

After cloning the repository and navigating to the root directory of the project, please run the following commands:

    python -m venv .venv
    source .venv/bin/activate
    pip install -r ./requirements.txt

**Env variables**

At this stage of the development, you will also need environmental variables. Please create a .env file within the backend folder with the following in order to run with your postgres server:

    HOST
    PORT
    DB_PORT
    DB_USERNAME
    DB_PASSWORD

### How to run

You may run the `main.py` file from your favourite IDE, or, from the command line after navigating to the root folder and activating the venv:

    source .venv/bin/activate
    python3 main.py

### Next steps in development

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) <br>
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) <br>
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white) <br>
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) <br>