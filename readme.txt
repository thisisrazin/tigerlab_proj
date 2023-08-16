1) Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2) Install pipenv using Homebrew
brew install pipenv

3) Open the terminal and change the directory to the django project folder titled 'tigerlab_proj'
(alternatively you can just open the project in VSCode and use the integrated terminal within the IDE)

4) Install the required packages in a newly created Python Virtual Environment
pipenv install -r requirements.txt

5) Activate the Python Virtual Environment
pipenv shell

Note: The terminal should now have (tigerlab_proj) at the beginning the directory
to indicate that the Python Virtual Environment is activated

6) Migrate the Database
python manage.py makemigrations
python manage.py migrate

7) Run the 'tigerlab_proj' django project
python manage.py runserver

8) Go to the admin page and log in
127.0.0.1:8000/admin/

user: tigerlab
password: tiger123

9) Go to main page of the app
http://127.0.0.1:8000/sports_league/upload/

10) Start using the App