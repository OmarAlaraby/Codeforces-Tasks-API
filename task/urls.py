from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'problems', views.ProblemView, basename='problem')

urlpatterns = [
    
    path('get-new-task/<int:curr_rate>/<int:number_of_problems>/', views.Get_New_Task),
    path('all-tasks/', views.TaskView),
    path('clear-all-tasks/', views.clear_tasks),
    path('restore-all-problems/', views.restore_problems),
    
] + router.urls