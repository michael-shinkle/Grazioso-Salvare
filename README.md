## Grazioso-Salvare
This is a dashboard that connects to MongoDB and displays that information. For this specific purpose, it was connected to a database containing the data for animals in local animal shelters. The animals were displayed in a table and below that a pie chart is displayed showing breed information, along with a map that centers on the animals location.

<details> 
  <summary>Table of Contents</summary> 
  <ol> 
    <li><a href="#writing-programs-that-are-maintainable-readable-and-adaptable">Writing Programs that are Maintainable, Readable, and Adaptable</a></li> 
    <li><a href="#my-approach">My Approach</a></li> 
    <li><a href="#what-do-computer-scientists-do">What Do Computer Scientists Do?</a></li> 
  </ol> 
</details> 

### About the Project
Grazioso Salvare is a rescue-animal training company and part of their work is to find dogs that are good candidates for search and rescue training. Grazioso Salvare has asked for software that can interact with existing data from animal shelters in the aim of identifying suitable candidates for training. The end state of this project will be a full stack software program capable of identifying and filtering training candidates. The first step of this project is to create Python middleware that can interact with MongoDB, specifically CRUD (Create, Read, Update, Delete) functionality.  

### Motivation
The goal of this project is to create an open-source dashboard that will allow Grazioso Salvare and other companies to utilize this system and adjust them to their own purposes. This program could be adjusted to filter for service dogs, therapy dogs, or simply be used by an adoption agency to find animals that customers request. This makes the software much more modular and able to expand into different areas of the industry. 

### Tools Used
MongoDB was selected as the database utility because it is an extremely powerful and fast database manager. There is also a library that interfaces it with python extremely well in the form of PyMongo. Dash is used as the framework to display the information derived from MongoDB to the website dashboard. To interface between MongoDB and Dash, Pandas was used to create data frames from the MongoDB data that Dash can read and display in html format. 

### Getting Started
To get started, import a csv database file into MongoDB using the following command in the terminal or command prompt window: 
  
    mongoImport --db=DatabaseName --collection=CollectionName --type=csv --headerline --file=./fileName.csv 
    
If the database requires authentication, add the csv file as an administrator using the following command: 

    mongoImport --authenticationDatabase "admin" -u "AdminUserName" -p=password --db=DatabaseName --collection=CollectionName --type=csv --headerline --file=./fileName.csv 
    
Add the AnimalShelter.py file to the directory where your project files are and import it using the following command: 

```python
from AnimalShelter import AnimalShelter 
```

### Installation
Pymongo, numpy, pandas, dash, jupyter-dash, and dash-leaflet are required for this project. To install them enter the following command into your terminal: 

```
pip install pymongo numpy pandas dash jupyter-dash dash-leaflet 
```

### Usage
#### Connecting to MongoDB 
To connect to a database, instantiate a new AnimalShelter object with the following command: 

```python
animalShelter = AnimalShelter('userName', 'password', 'ipAddress', 'port', 'databaseName') 
```

Where each data member is a string relevant to the database you are trying to access. Upon successful connection to the database, a message will be printed as shown in this example: 

![connect](/screenshots/connect-success.PNG?raw=true "connect success")

If the server is unavailable, or if the login info is incorrect an exception will be raised, and the program will terminate. 
![connect fail](/screenshots/connect-failure.PNG?raw=true "connect failure")
![auth fail](/screenshots/authentication-failure.PNG?raw=true "authentication failure")

#### Access the Grazioso Salvare Dashboard 
To access the Grazioso Salvare Dashboard, add the ProjectTwoDashboard.ipynb file to the same directory as AnimalShelter.py. Update the login credentials to match your MongoDB and run the code. When the information is displayed you will see a table with 10 rows corresponding to each document in your database. The table is paginated to avoid an overflow of data on the screen. Below the data table is a pie chart showing the breed information of the data currently being shown in the data table, as well as a map showing the location of the animal. If you select a row in the data table, the map will automatically recenter on the location of that animal. You can also filter for animals that would be adept at the type of training that is displayed in the radio buttons at the top. When you make a selection from the radio buttons, the data table and pie chart will automatically update to match the search query. The reset button returns the original data frame that was generated when the dashboard was first loaded. 

Dashboard when first loaded: 
![dashboard](/screenshots/dashboard-default.PNG?raw=true "dashboard default")

Dashboard filtered for Mountain Rescue Dogs: 
![dashboard](/screenshots/dashboard-filteredt.PNG?raw=true "dashboard filtered")

### Writing Programs that are Maintainable, Readable, and Adaptable
The first part of this project was to create a separate Python file that gave me create, read, update, and delete (CRUD) capabilities when accessing MongoDB through Python. Having this functionality in a separate file allows me to have modular code that I can extend to other programs. I can use my CRUD Python module in any application that requires me to access MongoDB without having to rewrite any code. I specifically wrote the module to be as generic as possible and for each future use of this module, the specifics are passed in through function parameters

### My Approach
My approach to this problem was to get the minimum viable product working, and then improving the interface from there. In this case, the first step was to make sure the dashboard connected to MongoDB and displayed the information correctly. Once that step was complete, I formatted the data table to make it easier to read and navigate for the user. Finally, I made sure that the pie chart and map updated correctly based on the information that was displayed in the data table. In future projects involving databases, my approach would be similar to this. The first step is to get the data into the dashboard, the next steps are about how can I make this easier for a user.

### What Do Computer Scientists Do?
Computer scientists use technology to solve problems in innovative ways. Sometimes this is as simple as developing a web application, other times it is creating revolutionary artificial intelligence systems. My work on this project helps a company like Grazioso Salvare navigate a very large amount of data in a way that a non-programmer is able to intuitively use. This is one of my favorite aspects of computer science.
