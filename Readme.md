# The Gram

>[Alex-MWaura](https://hood21.herokuapp.com/)  
  
# Description  
This is a neighbourhood watch website that enables users to get updates and review some of the available amenities
##  Live Link  
 Click [View Site](https://hood21.herokuapp.com/)  to visit the site
  
 
## User Story  
  
* Sign in to the application to start using.  
* Add location if none is provided the application will break
* click icon to interract with sidenav
* Update profile 
*click on location button to view posts related to your location
* Search for different location.   
* click on business title to view details 

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Hood pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  * click on username to view the specific post  

 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.7](https://www.python.org/)  
* [Django 1.11.17](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [alexmwaura43@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)]()  
* Copyright (c) 2019 **Alex Mwaura**