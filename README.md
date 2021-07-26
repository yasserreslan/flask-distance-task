# Flask Test Task for Neuro.net Junior Python developer 

# Table of contents
* [Objective](#objective-and-usage)
* [Technologies](#technologies)
* [Setup](#setup)

## Objective and Usage
This Project's goal aims at creating a Flask Blueprint serving as a distance calculator between input addresses entered by the user and a static address chosen by the Host, in out case Moscow Ring Road, using Geocoding libraries. 

Directly running the flask application, the user  is asked to enter an address in the input of the html page he sees. Once "Go" is pressed, the page automatically refreshes and the desired results are logged into app.log file located in the same directory as the flask application.


## Technologies 
Project is created with:
* Python version: 3.9.4
* Flask version: 1.1.2


## Setup 

This application requires python 3.7+ to run.
Install the dependencies and start the servr
```sh
pip install -r requirements.txt
cd Flask_Task
export FLASK_DEBUG=1
flask run
```
Then Visit http://localhost:5000

You are already up and running!
To check the address logs make sure to check app.log file.
