# VirtualGym
# Project Background:
The Virtual Gym project aims to build a web app for both Physiotherapists and their patients to assist in exercise. The Physiotherapists will build and upload videos for exercises for the patients to perform. The web app will allow user to edit and annotate the videos, as well as provide tags and descriptions for the exercise. The patients will be able to view, discuss, and ask questions about the exercises that have been uploaded. In this project, we will also construct the backend to support the application.

Enviroment:
  * virtualenv
  
Required Software:
  * python 3.5
  * Django 1.11.5 (back end)
  * python-social-auth 0.3.6 (back end)
  * bootstrap 3 (front end)
  * Sass 3.5.1 (front end)
  * jquery (front end)
  * jquery-ui (front end)
  
Testing Software (Optional):
  * Selenium
  * Geckodriver
  
Instructions to run locally:
  * Install python
  * Use Pip to install each of the required libraries
  * Navigate to ./VirtualGym/VirtualGym_WebProject/src
  * Run command line: python3 manage.py runserver localhost:8000 (manage.py is the file, runserver starts it and localhost:8000 sets the local address to be used)
  * Use chrome or firefox use address localhost:8000 (safari has issues with the mp4 player mp4 player)

Run UI test case:
 * Install selenium, geckodriver library
 * Run the server locally as above
 * Run command line: python3 manage.py test (under  VirtualGym/VirtualGym_WebProject/src)
 * (Need the newest version of Firefox for selenium to work)
 
