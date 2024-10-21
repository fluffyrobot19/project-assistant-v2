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

- Learning a new stack (Python / Flask) and server-side rendering
- Practicing containerization and process automation with scripts
- Advancing my learning process in AWS resources

### Built with

![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white) <br>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br>
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) <br>
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) <br>
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) <br>
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white) <br>
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) <br>

### How to run at this stage of development

Please run the `RUN.sh` script from a Bash terminal.
There are 3 options for running the application:

1. **Running locally**
  - Dependencies: python3 / postgresql / postgres account with admin privileges for the database connection

2. **Running in Docker**
  - Dependencies: docker / docker-compose

3. **Running in AWS with Terraform - Coming soon...**


This script will do some process checks (whether the necessary ports are free and dependencies are installed), and then prompt you to start the application or opt-out from running it.

**Login**

Once you see the main page, you may log in with the following test user credentials:

    username: happy_sloth
    password: password123

**Sensitive information**

The `RUN.sh` script will save your postgres username and password to a `.pgpass` file in your home directory. This file helps facilitate the database connection and set up the Project Assistant database. The file will be deleted after the script finishes.
### Coming up...

![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) <br>
