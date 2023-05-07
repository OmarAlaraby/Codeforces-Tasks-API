from rest_framework import viewsets , status
from project.settings import REST_FRAMEWORK
from .models import Problem , Task , Trainee
from .serializers import ProblemSerialzer , TaskSerialzer
from .permissions import IsRegistered , UnRegistered
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
import math



@api_view(['GET'])
@permission_classes([IsRegistered])
def TaskView(request):
    serialzer = TaskSerialzer(Task.objects.all(), many=True)
    return Response({"Tasks" : serialzer.data}, status.HTTP_200_OK)

class ProblemView(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerialzer
    permission_classes = [IsRegistered]
    
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
@permission_classes([IsRegistered])
def Get_New_Task(request):
    user = Trainee.objects.first()
    curr_rate = user.rate
    number_of_problems = user.number_of_problems
    
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



@api_view(['POST'])
@permission_classes([UnRegistered])
def sign_up(request , Handle , Rate , NOP):
    if Rate % 100 != 0 or NOP > 20:
        return Response({"Response" : "Rate must be valid and number of problems shouldn't be larger tha 20"} , status.HTTP_400_BAD_REQUEST)
    
    Trainee.objects.create(Handle=Handle, rate=Rate, number_of_problems=NOP)
    return Response({"Response" : "User Added"} , status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsRegistered])
def user_update(request):
    user = Trainee.objects.first()
    
    new_handle = request.data.get('handle', user.Handle)
    new_rate = request.data.get('rate', user.rate)
    new_NOP = request.data.get('NOP', user.number_of_problems)
    
    if new_handle == user.Handle and new_rate == user.rate and new_NOP == user.number_of_problems:
        return Response({"Response" : "NOTHING TO UPDATE"} , status.HTTP_400_BAD_REQUEST)
    
    user.Handle = new_handle
    user.rate = new_rate
    user.number_of_problems = new_NOP
    user.save()
    return Response({"Response" : "user data updated"}, status.HTTP_200_OK)


# ------------------- for testing ----------------- #

# delete all tasks and restore the problems
@api_view(['DELETE'])
@permission_classes([IsRegistered])
def clear_tasks(request):
    tasks = Task.objects.all()
    tasks.delete()
    return Response({"Respons" : "all tasks has been deleted"} , status.HTTP_200_OK)

# restore problems ( set is_solved to False)
@api_view(['GET'])
@permission_classes([IsRegistered])
def restore_problems(request):
    problems = Problem.objects.filter(is_solved=True)
    for problem in problems:
        problem.is_solved = False
        problem.save()
    return Response({"Respons" : "all problems has been restored"} , status.HTTP_200_OK)
