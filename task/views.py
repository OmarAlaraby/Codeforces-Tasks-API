from rest_framework import viewsets , status
from .models import Problem , Task
from .serializers import ProblemSerialzer , TaskSerialzer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import math



@api_view(['GET'])
def TaskView(request):
    serialzer = TaskSerialzer(Task.objects.all(), many=True)
    return Response({"Tasks" : serialzer.data}, status.HTTP_200_OK)

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