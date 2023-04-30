# Codeforces-Tasks-API

### this API allow you to create a task consists of any number of problems and any rate range you want.

<hr>

## end points

you can make GET requset to the end point : http://127.0.0.1:8000/api/get-new-task/curr_rate/number_of_problems/

make sure to do the following steps:
- replace the number_of_problems with an integer value
- replace the curr_rate with the range rate you want , make sure it's a valid rate

**Note:** if you passed rate = 1000. So, the API will return problems with rate [900, 1000, 1100]


you can make GET request to the end point : http://127.0.0.1:8000/api/all-tasks/

it returns all tasks you have requested
