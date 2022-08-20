#DJANGO CHEATSHEET

""" Django is a Python framework used for web development, it's known
for its easy and fast deployment of web apps. It builds around a MVT
(Model-View-Template) design and it configures the patterns to use
automatically, so you can focus only on building the app. """

#Setting up a virtual environment
1. py -m venv {venv_name} #for windows
2. python -m venv {venv_name} #for linux/macOS

#Activate your virtual environment
1. myproject\Scripts\activate.bat #for windows
2. source myproject/bin/activate #for linux/macOS

#Create a project
django-admin startproject {project_name}

#Run server
python manage.py runserver #it runs the server on your localhost http://127.0.0.1:8000/

