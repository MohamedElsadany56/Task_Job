from django.urls import path
from . import views

app_name = 'Task'

urlpatterns = [
    path('post/', views.post_task, name='postTask'),
]
