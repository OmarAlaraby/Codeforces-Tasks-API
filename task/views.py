from rest_framework import viewsets , status
from .models import Problem , Task
from .serializers import ProblemSerialzer , TaskSerialzer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import math



@api_view(['GET'])
def TaskView(request):
    serialzer = TaskSerialzer(Task.objects.all(), many=True)
    return Response({"Tasks" : serialzer.data}, status.HTTP_400_BAD_REQUEST)

class ProblemView(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerialzer
    
    def gen_url(self ,contest_id , index):
        return f"https://codeforces.com/contest/{contest_id}/problem/{index}"
    
    def create(self ,request):
        
        data = request.data
        
        for problem in data: 
            
            contest_id = problem['contestId']
            index = problem['index']
            rate = problem.get('rating', 3000)
            name = problem['name']
            url = self.gen_url(contest_id , index)
            
            Problem.objects.create(name=name, rate=rate, url=url)
            
        return Response({"Response" : "problem/problems added"} , status.HTTP_200_OK)
    


@api_view(['GET'])
def Get_New_Task(request, curr_rate, number_of_problems):
    
    if not (curr_rate % 10 == 0 and curr_rate >= 800 and curr_rate <= 4000):
        return Response({"ERROR" : "ENTER A VALID RATE"}, status.bad)
    
    task = Task.objects.create()
    
    problems = Problem.objects.filter(rate=curr_rate - (100 if curr_rate > 800 else curr_rate), is_solved=False)
    for i in range(min(len(problems) , math.ceil(number_of_problems / 3))):
        problems[i].Task.add(task)
        problems[i].is_solved = True
        problems[i].save()
        
    problems = Problem.objects.filter(rate=curr_rate, is_solved=False)
    for i in range(min(len(problems) , math.ceil(number_of_problems / 3))):
        problems[i].Task.add(task)
        problems[i].is_solved = True
        problems[i].save()
        
    problems = Problem.objects.filter(rate=curr_rate + (100 if curr_rate < 2800 else curr_rate), is_solved=False)
    for i in range(min(len(problems) , number_of_problems - 2 * math.ceil(number_of_problems / 3))):
        problems[i].Task.add(task)
        problems[i].is_solved = True
        problems[i].save()
        
    task.save()
    serializer = TaskSerialzer(task)
    return Response({"Task" : serializer.data}, status.HTTP_200_OK)


# delete all tasks and restore the problems
@api_view(['POST'])
def clear_tasks(request):
    tasks = Task.objects.all()
    for task in tasks:
        for problem in task.problems:
            problem.is_solved = False
            problem.save()
        task.problems.clear()
    
    tasks.delete()
    return Response({"Respons" : "all tasks has been deleted"} , status.HTTP_200_OK)

# restore problems ( set is_solved to False)
@api_view(['POST'])
def restore_problems(request):
    problems = Problem.objects.filter(is_solved=True)
    for problem in problems:
        problem.is_solved = False
        problem.save()
    return Response({"Respons" : "all problems has been restored"} , status.HTTP_200_OK)
