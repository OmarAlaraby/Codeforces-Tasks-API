# Codeforces-Tasks-API

this API allow you to create a task consists of any number of problems and any rate range you want.
and more than 3000+ problem stored in the database.

<hr>
<br>

## installation

### follow those steps carefully

1. ##### colne the repo using the following command :

` git clone https://github.com/OmarAlaraby/Codeforces-Tasks-API.git `

<br>


2. ##### install pipenv

`pip install pipenv`

<br>

3. go to project's direction

`cd Codeforces-Tasks-API`

<br>

4. activate the virtual environment

`pipenv shell`

<br>

5. ##### install dependency

`pipenv install Pipfile`

<br>

6. ##### run the local server

`python manage.py runserver`

<br>

now you are ready to call the endpoints

enjoy :)

<br><hr><br>

## end points
<br>

- ### sign up

##### endpoint : http://127.0.0.1:8000/api/sign-up/Handle/Rate/NOP/

this endpoint takes [ Handle , Rate , number of problems ] as a parameters , if the user is already signed in, it will return ERROR 403.

<br><br>

- ### Create new task

##### endpoint : http://127.0.0.1:8000/api/get-new-task/

make sure to do the following steps:
1. replace the number_of_problems with an integer value
2. replace the curr_rate with the range rate you want , make sure it's a valid rate

![CodeFroces Task API](https://user-images.githubusercontent.com/99359641/235442398-213db619-6a09-4937-b973-35e8e4c80b97.png)

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
