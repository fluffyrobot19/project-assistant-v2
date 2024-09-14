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
- Practicing containerization and building CI/CD pipeline
- Advancing my learning process in AWS resources

### Built with

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br>
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) <br>
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) <br>
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) <br>

### Dependencies

You will need Docker to run the app.

### How to run at this stage of development

First, please make sure that you have Docker running.

Then please run the `RUN.sh` script from your terminal. 

This script will check if port 3000 and 5432 are free, for Flask and Postgres, as well as run the `Dockerfile` and `docker-compose.yml`˙files.

A guest user is set up for the database in the `docker-compose.yml` file.

After finishing, the script will also remove the recently created Docker image.

### Coming up...

![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) <br>
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white) <br>
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) <br>