# Readme

## Mealy

---

![homeshot.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/homeshot.png)

link to live site

## About

---

Mealy is a web app designed to create meal plans containing ingredients that can be automatically added to a shopping list.

### Contents

---

## UX

---

### User stories completed

[User Stories](https://www.notion.so/b4b14f4882f7465b9731e2a18a66ebb2)

## Design

---

### Wireframes

---

[iphone6-3up-grid.8e014a7f copy.pdf](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/iphone6-3up-grid.8e014a7f_copy.pdf)

---

[iphone6-3up-grid.8e014a7f copy copy 2 copy.pdf](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/iphone6-3up-grid.8e014a7f_copy_copy_2_copy.pdf)

---

[iphone6-3up-grid.8e014a7f copy copy 2.pdf](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/iphone6-3up-grid.8e014a7f_copy_copy_2.pdf)

---

## Design Thinking

---

---

### Empathise:

- as a user i want to be able to streamline my shopping, cooking and meal prep workflow and reduce food waste to save myself time, money and effort.
- i need the software i use to do this to be simple and efficient reducing the complexity of the above workflow, not adding complexity.
- I want to be able to get a quick but detailed overview of all stages of the process with no friction so i can spend the minimal amount of needed to see the relevant info i need and to crud this info effortlessly.

---

### Questions:

- what will keep users coming back to engage with site and make it part of their daily life?
- how can we make the site as smooth as possible for the user to achieve the desired result?
- how can we flesh out features of the site to offer optional additional services to the user if they want more content and tools to manage there food workflow? (recipe suggestions, user shared content etc)

---

### Examine:

- If i was a user i would like to be able to manage crud functionality intuitively with no bloated features.
- I would like to be able to see all the info I need at a glance for example while shopping or in the middle of a meal shopping lists and recipes should be accessible in seconds with a clear UI to achieve this.
- some additional features such as recipe suggestions from my ingredients in stock, other users recipes and customization features would be beneficial once they do not bloat the core functionality and add extra steps to time sensitive actions.

---

## Features

---

### Responsive design

### Home Meal View

![home.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/home.png)

---

### Shopping List View

![shopping_list.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/shopping_list.png)

---

### Add Meal View

![add_meal.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/add_meal.png)

---

### Add Ingredient View

![add_ingredient.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/add_ingredient.png)

---

### Sign In

![Sign_In.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Sign_In.png)

---

### Sign Out

![Sign_Out.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Sign_Out.png)

---

### Sign Up

![Sign_Up.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Sign_Up.png)

---

## **Technologies**

---

### **Database**

- [SQLite](https://www.sqlite.org/index.html)
    - Cloud based database to hold the product, user, order and blog fields.
- [Postgres](https://www.postgresql.org/)

### **Database Design**

The database uses SQL through PostgreSQL and was originally formed from fixtures *[categories.json](https://github.com/suzybee1987/knit-happens/blob/main/products/fixtures/categories.json)* and *[products.json](https://github.com/suzybee1987/knit-happens/blob/main/products/fixtures/products.json)*

The Database schema is below

![my_project_visualized.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/my_project_visualized.png)

### **Languages**

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used to show the questions through pagination and for the game play.
- [Python 3](https://www.python.org/)
    - Used to run the site and database

### **Frameworks and Libraries**

- [Django](https://www.djangoproject.com/)
    - The high-level framework used for rapid development of the site.

## Technologies used

- CRUD
- Django
- Python
- HTML
- Bootstrap
- Github
- Gitpod
- Heroku
- Heroku Postgres
- MVC Framework
- Code Institute template
- Agile method (User Stories)
- Online Testers and validators
- notion
- todoist
- cloudinary
- Remarkable 2

# Development Implementation

---

## Testing

---

### Manual Testing

- Manual testing on Urls, Views and Functions
- Coverage is at 89%

### Light House

![lighthouse.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/lighthouse.png)

### Code Validation

- Html Validated

![Screenshot from 2022-04-10 22-29-27.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_from_2022-04-10_22-29-27.png)

- Djlint templates validated
- Pylint validated

### manual testing

- all links have been verified to work.
- all forms are validated and will not accept incorrect entry.

## Deployment

---

## Deployment and making a clone

### Deployment to Heroku

**In your app**

1. add the list of requirements  "pip3 freeze --local > requirements.txt"
2. commit all changes

**Log into Heroku**

1. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in
2. create new app
3. Choose Region closest to your location

**Project Page**

1. Go to the Resources tab and init a new Postgres DB
2. Database URL will be available on the config variable page.
3. Add Django secret key, stripe keys and AWS keys to the config variables.
4. This document describes the s3 init process
    
    [](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf)
    

**In Repo**

1. Profile needs to be created in your app

`web: gunicorn PROJ_NAME.wsgi`

1. In settings in your app add Heroku to ALLOWED_HOSTS
2. Add and commit the changes in your code and push to GitHub

**Final step - deployment**

1. Go to section "deployment method ", choose "GitHub Automatic Deployments”
2. type the name of your repository and click "search"
3. once Heroku finds your repository - click "connect"
4. Click "Enable automatic deploys” and now your app will rebuild with each new commit

## Agile Planning

---

![Screenshot from 2022-04-09 22-04-12.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_from_2022-04-09_22-04-12.png)

![Screenshot 2022-04-11 112932.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_2022-04-11_112932.png)

## Agile planning

---

### I used agile principles to manage my time and user stories for this project

- Notion user story database was used for original user stories.

---

![Screenshot 2022-04-11 112932.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_2022-04-11_112932%201.png)

---

![Screenshot from 2022-04-09 22-04-12.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_from_2022-04-09_22-04-12%201.png)

### Jira was used for tasks for v2

![Screenshot from 2022-08-30 21-36-43.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_from_2022-08-30_21-36-43.png)

![Screenshot from 2022-08-30 21-37-05.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_from_2022-08-30_21-37-05.png)

---

## Agile planning

---

### I used agile principles to manage my time and user stories for this project

- Notion user story database was used for original user stories.

---

![Screenshot 2022-04-11 112932.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_2022-04-11_112932%201.png)

---

![Screenshot from 2022-04-09 22-04-12.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_from_2022-04-09_22-04-12%201.png)

### Jira was used for tasks for v2

![Screenshot from 2022-08-30 21-36-43.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_from_2022-08-30_21-36-43.png)

![Screenshot from 2022-08-30 21-37-05.png](Readme%20b0a41e8d98084c7b8e6f6d0ba2076a58/Screenshot_from_2022-08-30_21-37-05.png)

---

## Credits

---

- code institute codestar blog walkthrough for helping me understand the technology
- this document for guiding the deployment
    
    [Django Deployment Instructions](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)
    
- the Django docs for helping me with syntax and best practice advice
- the bootstrap docs for speeding up front-end design.
- my family for helping me test the application
- my mentor for the guidance along the way
