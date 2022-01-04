# Movie_liker
From Title you Can see that this project is about Movies Where in a person can Like/Dislike a Movie.
This Project Mainly Consist of 2 Apps
1. Main App 
2. Server App

Main App was build by using **Flask** Where as Server App was Build Using **Django**, Both the apps will run in their repsective Docker Container inorder to Isoalte from each other and the apps communicate by using Internal Api Calls.The project interconnects Django and Flask services using the **pika** module.

#### Technical Requirement
1. Docker Install it from https://www.docker.com/get-started
2. Install Django by using  `pip install django`
3. Install Django Rest Framework using  `pip install djangorestframework`
4. Postman from https://www.postman.com/downloads/
5. CloudAMQP Account
#### How to Run in Local Environment
1. Git Clone or Download the Repository into your local Machine
2. Open Your Command Prompt and Direct it towards the local Repository
3. After Redirecting Create a Virtual Environment and activate it by using `env\Scripts\activate`

#### Follow Below Steps for Running Server App:
1. Go To the Server App By Typing **cd server_side** and then type `python manage.py makemigrations`
2. After that Type `docker-compose up --build` 

You can see that it is installing all the required packages and resources and after some time you can see a messaage displaying succesful connection with some adreess like `0.0.0.0:8000` Which says that Current Application is running at port 8000 you can check it by typing **127.0.1.1:8000** in the address bar of any browser. This application Mainly consist of Information regarding movies like *Movie Name, image, and likes*. Here MySQL Uses Port Number 3306 for connecting with SQL Server.

You can Perform **CRUD** By using Postman along with different requests like GET,POST,PUT,DELETE Requests Lets look at example below to get the Results

Enter the Data into The Table and Open Postman Application and Type The address as `127.0.1.1:8000/` movies in address section of Postman App, after that select GET Request to get list of movies that are present in the Table you can Some Text in **JSON Format** which contain Informating Regarding Movies, So in this way you can Perform Difefrent Operations

#### Follow Below Steps for Running Main App:
1. Open New Terminal And Activate Virtual Environment by using `env\Scripts\activate`
2. Go To the Main App By Typing **cd main** and then type `python manage.py makemigrations`
3. After that Type `docker-compose up --build` 

You can see that it is installing all the required packages and resources and after some time you can see a messaage displaying succesful connection with some adreess like `0.0.0.0:8001` Which says that Current Application is running at port 8001 you can check it by typing **127.0.1.1:8001** in the address bar of any browser. This application Mainly consist of Information regarding user like *User id, Movie id*. Here MySQL Uses Port Number 33067 for connecting with SQL Server.

You can get the information about User By using Postman Lets look at example below to get the Results
If a user want to see list of movies then he can type `localhost:8001/api/movies` in any browser to get list of movies and to like a movies user can type something like 
`localhost:8001/api/movies/id/like` in this way the user can like a movie

