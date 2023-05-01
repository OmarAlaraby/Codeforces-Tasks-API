# Codeforces-Tasks-API

this API allow you to create a task consists of any number of problems and any rate range you want.
and more than 3000+ problem stored in the database.

<hr>
<br>

## installation

colne the repo using the following command :
```
git clone https://github.com/OmarAlaraby/Codeforces-Tasks-API.git


install pipenv
```
pip install pipenv


open the project's folder and run those commands :

activate the virtual environment
```
pipenv shell


install dependency
```
pipenv install Pipfile


run the local server
```
python manage.py runserver


now you are ready to call the endpoints

enjoy :)

## end points
<br>

- ### Create new task

##### endpoint : http://127.0.0.1:8000/api/get-new-task/curr_rate/number_of_problems/

make sure to do the following steps:
1. replace the number_of_problems with an integer value
2. replace the curr_rate with the range rate you want , make sure it's a valid rate

**Note:** if you passed rate = 1000. So, the API will return problems with rate [900, 1000, 1100]

<br><br>

- ### view all tasks you have created : 
##### endpoint : http://127.0.0.1:8000/api/all-tasks/


<br><br>

- ### delete all tasks you have created
##### endpoint : http://127.0.0.1:8000/api/clear-all-tasks/

<br><br>

- ### restore all problems
##### endpoint : http://127.0.0.1:8000/api/restore-all-problems/

why you need to restore problems ?
the problems in all tasks are unique. So, if deleted all tasks you need to restore all problems if you want.
