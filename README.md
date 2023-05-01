# Codeforces-Tasks-API

### this API allow you to create a task consists of any number of problems and any rate range you want.

<hr>
<br>

## end points
<br>

### Create new task

##### endpoint : http://127.0.0.1:8000/api/get-new-task/curr_rate/number_of_problems/

make sure to do the following steps:
- replace the number_of_problems with an integer value
- replace the curr_rate with the range rate you want , make sure it's a valid rate

**Note:** if you passed rate = 1000. So, the API will return problems with rate [900, 1000, 1100]

<br><br>

### view all tasks you have created : 
##### endpoint : http://127.0.0.1:8000/api/all-tasks/


<br><br>

### delete all tasks you have created
##### endpoint : http://127.0.0.1:8000/api/clear-all-tasks/

<br><br>

### restore all problems
##### endpoint : http://127.0.0.1:8000/api/restore-all-problems/

why you need to restore problems ?
the problems in all tasks are unique. So, if deleted all tasks you need to restore all problems if you want.
