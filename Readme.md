Iris-Classifier Web App using Flask Framework

Deployed on Heroku Cloud

App Link:
https://irisclassifierapp.herokuapp.com

Software Requirements:
1. Python3
2. Git
3. Heroku CLI

Link to download Git:
https://git-scm.com/download

Link to download Heroku CLI:
https://devcenter.heroku.com/articles/heroku-cli#download-and-install

Steps to push the flask app to Heroku Cloud:
1. Login to Heroku account in the terminal

Command: heroku login

2. Initialize a git repository

Command: git init

3. Connect to the created Heroku App

Command: heroku git:remote -a app_name

4. Add all project files and folder to stage

Command: git add .

5. Commit the project files and folders to the repository

Command: git commit -am “first commit”

6. Deploy the app (final step)

Command: git push heroku master
