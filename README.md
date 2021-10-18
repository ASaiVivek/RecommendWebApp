# RecommendWebApp
Project Title - MINDFRAME: Music and Movie Recommendations to uplift the current mood using Deep Learning.
[Published Paper in the IEEE Conference](https://ieeexplore.ieee.org/document/9526435)

:warning: [IMPORTANT] - In order for this project to run, you need to run [this Server](https://github.com/vivekboss99/EmotionsAPI), which will help this Project's Server to communicate for processing the input images.


To Run:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Files Summary:

- mrecommend: Main Application Directory
  - static/mrecommend: contains all the static content
    * styles.css: script that sets all the style properties of the website.
  - templates/mrecommend: Contains all the application template files
    * layout.html: Base template which is extended by all the other templates, it contains, the header and the footer section.
    * index.html: This template first assists the user in finding the emotion, then, gives options for the user to select music or movies.
    * music.html: This template displays the filtered music from the dataset along with playable content.
    * movies.html: This template displays the filtered movies from the dataset along with links for the content.
    * login.html: This template displays a form to take input from the users to verify and log them into the website by checking the credentials                   in the database.
    * register.html: This template displays a form to take input from the user to register him/her into the database.
  - models.py: We are adding an abstract user model here.
  - urls.py:  Contains all the application URLs.
  - views.py: Contains all the functions which run the application.
- RecommendWebApp: Main Project Directory.
  - settings.py:  Contains all the registered applications and settings of the web application.
  - urls.py: Contains the URLs which link to the Main Application.

