## Grazioso-Salvare
This is a dashboard that connects to MongoDB and displays that information. For this specific purpose, it was connected to a database containing the data for animals in local animal shelters. The animals were displayed in a table and below that a pie chart is displayed showing breed information, along with a map that centers on the animals location.

<details> 
  <summary>Table of Contents</summary> 
  <ol> 
    <li><a href="#writing-programs-that-are-maintainable-readable-and-adaptable">Writing Programs that are Maintainable, Readable, and Adaptable</a></li> 
    <li><a href="#my-approach">My Approach</a></li> 
    <li><a href="#what-do-computer-scientists-do">What Do Computer Scientists Do?</a></li> 
    <li><a href="#ethical-responsibilities">Ethical Responsibilities</a></li> 
  </ol> 
</details> 

### Writing Programs that are Maintainable, Readable, and Adaptable
The first part of this project was to create a separate Python file that gave me create, read, update, and delete (CRUD) capabilities when accessing MongoDB through Python. Having this functionality in a separate file allows me to have modular code that I can extend to other programs. I can use my CRUD Python module in any application that requires me to access MongoDB without having to rewrite any code. I specifically wrote the module to be as generic as possible and for each future use of this module, the specifics are passed in through function parameters

### My Approach
My approach to this problem was to get the minimum viable product working, and then improving the interface from there. In this case, the first step was to make sure the dashboard connected to MongoDB and displayed the information correctly. Once that step was complete, I formatted the data table to make it easier to read and navigate for the user. Finally, I made sure that the pie chart and map updated correctly based on the information that was displayed in the data table. In future projects involving databases, my approach would be similar to this. The first step is to get the data into the dashboard, the next steps are about how can I make this easier for a user.

### >What Do Computer Scientists Do?
Computer scientists use technology to solve problems in innovative ways. Sometimes this is as simple as developing a web application, other times it is creating revolutionary artificial intelligence systems. My work on this project helps a company like Grazioso Salvare navigate a very large amount of data in a way that a non-programmer is able to intuitively use. This is one of my favorite aspects of computer science.
