# fullThrottle(client-side URL: https://fullthrottle-3406a.firebaseapp.com/) 
(Server-side URL: https://immense-forest-90921.herokuapp.com/searchString/getform?q=these)
This repo contains the application build using the Django framework. Repo contains the functionality of autocomplete by suggesting the possible words that can be derived from user input. The results presented are limited to 25 queries only.

# Pre-Requisite
1. Install Python3 (refer to https://www.python.org/downloads/ for more details on Installation).
2. Install Django Framework using pip. Run command `pip install -e django\` for windows. For more installtion guide refer to link https://docs.djangoproject.com/en/2.1/topics/install/ 
3. Install node.js for running the client-side application.
4. Install Ionic Framework. Refer to https://ionicframework.com/docs/intro/installation for installation instructions.

# Run server

1. Clone the repository
2. After cloning the repository, head to the fullThrottle folder
3. Run `python manage.py runserver 8080` to run the server
4. Clone the repository mentioned here. It is link to the client side application. Link: https://github.com/sagarmanghnani/frontend-fullThrottle.
5. After cloning the client side head to the "frontend-fullThrottle" folder and run command `ionic serve`. This command will run the client side of the application.
6. Please Enter the text in searchbox to receive the autocomplete suggestion.
    Note: Please wait for 2-3 seconds as autocomplete takes time to loads.
7. Please take above action if no autocomplete suggestion is shown on the screen
   
7.1. Please check the port on which server is running on. Server should be running on port 8080 as API end point is configured to run on port 8080.

7.2. This project reads the dataset and then save these dataset to database. There are several actions which are required for proper functionality of the application
These steps are mentioned below
    a. Head to the http://127.0.0.1:8080/searchString/ to check if application is running properly. "Hello world" message will be displayed on the screen.
    b.Note: This step is only to be taken when autocomplete suggestion is not showing after few seconds. 
    Another reason for not showing any suggestions may be beacause the entries of the dataset is not inserted to the database. To insert the entries in the database
    please head to url http://127.0.0.1:8080/searchString/checkdata. This Url will run method which reads the dataset and stores it in database.
    c. Wait for few minutes as dataset entries are huge and will take time to enter in the database
    d. After waiting for few minutes Please move to the client usl i.e `localhost:8100` and retry to put text in searchbar. Wait for few seconds Autocomplete suggestion will show up.
    
# Screenshots

![pic1](https://user-images.githubusercontent.com/20658754/47961357-78d35280-e02f-11e8-8e17-b480bd1348a5.PNG)
![pic2](https://user-images.githubusercontent.com/20658754/47961358-78d35280-e02f-11e8-8695-b3b14de09d59.PNG)
![pic3](https://user-images.githubusercontent.com/20658754/47961359-78d35280-e02f-11e8-9954-4369e402c3d2.PNG)
