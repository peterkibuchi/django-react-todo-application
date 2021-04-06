# Django React To-Do Application
> This is a simple To-Do Application built off Django (including the Django REST Framework for API CRUD operations) and React.
<!-- > Live demo [_here_](https://www.example.com). -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Inspiration](#inspiration)
* [Contact](#contact)


## General Information
- This application allows users to create tasks and mark them as complete or incomplete.
- I undertook this project as a means of:
  - familiarizing myself with the Django Rest Framework
  - learning how to connect a Django backend to a Front End Framework (React, in this case)


## Technologies Used
- Django
- Django Rest Framework
- React


## Features
- The ability to create, update, or delete tasks.
- The ability to mark tasks as complete or incomplete.


## Setup
<!-- Provide a link to the demo version here as well. -->
> You need to have your command line set up, preferably _Git Bash_. If you don't already, you can follow these [instructions to it set up](https://www.codecademy.com/articles/command-line-setup).
>
> You will also need to have _Python3_, _pipenv_ and _npm_ installed.
>
> If you don't have them installed, you can follow these [_instructions to install Python_](https://www.codecademy.com/articles/install-python3) and these [_instructions to install Node.js_](https://www.codecademy.com/articles/setting-up-node-locally) (npm will be installed automatically along with Node.js).
>
> To install pipenv simply run the following command (after successfully setting up Python): `pip install pipenv`

1. Navigate to the directory you would like the project to reside. Use the command line interface to clone the project:
   ```
   git clone https://github.com/peterkibuchi/django-react-todo-application
   ```

2. Navigate into the project directory: 
   ```
   cd django-react-todo-application
   ```

3. Create a virtual environment and activate it by running the following command:
   ```
   pipenv shell
   ```

4. Install the dependencies:
   ```
   pipenv install
   ```

5. Navigate into the frontend directory and run migrations:
   ```
   python manage.py migrate
   ```

6. Navigate into the frontend directory and install the dependencies:
   ```
   cd frontend
   npm install
   ```

To run the application you will need two terminal windows (one pointed to the frontend directory, the other to the backend directory) to start the servers:
1. In one terminal window, navigate to the _backend_ directory and run the following command to start the backend server:
   ```
   python manage.py runserver
   ```
   (The virtual environment has to be active for it to work)

2. In the other terminal window, navigate to the _frontend_ directory and run the following command to start the frontend server:
   ```
   npm start
   ```
   This will run the server and should automatically open a new browser window at the address `http://localhost:3000`.

Voila! You're all set up. Feel free to experiment with the application.



## Project Status
Project is: _complete_.


## Room for Improvement
Room for improvement:
- Improve the visual design.
- Make it responsive.

To do:
- Incorporate the Ionic Framework to allow the application to run on any platform.
- Add an authentication system that enables users to access their task items from any device.


## Inspiration
- This project was based on [this tutorial](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react) by the Digital Ocean Community.


## Contact
Created by [Peter Kibuchi](https://peterkibuchi.com) - feel free to get in touch.
