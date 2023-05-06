from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=255)
    rate = models.IntegerField(db_index=True)
    is_solved = models.BooleanField(default=False, null=True)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    problems = models.ManyToManyField(Problem, related_name='Task', blank=True)

class Trainee(models.Model):
    Handle = models.CharField(max_length=255)
    rate = models.IntegerField(db_index=True, default=800)
    number_of_problems = models.IntegerField(default=0)
    
    def __str__(self):
        return self.Handle