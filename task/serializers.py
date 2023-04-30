from rest_framework import serializers
from .models import Problem, Task

class ProblemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
        
class TaskSerialzer(serializers.ModelSerializer):
    problems = ProblemSerialzer(many=True)

    class Meta:
        model = Task
        fields = '__all__'
        depth = 2