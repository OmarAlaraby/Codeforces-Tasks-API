from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'problems', views.ProblemView, basename='problem')

urlpatterns = [
    
    path('get-new-task/', views.Get_New_Task),
    path('all-tasks/', views.TaskView),
    path('clear-all-tasks/', views.clear_tasks),
    path('restore-all-problems/', views.restore_problems),
    path('sign-up/<str:Handle>/<int:Rate>/<int:NOP>/', views.sign_up),
    path('update-user/', views.user_update),
    
] + router.urls