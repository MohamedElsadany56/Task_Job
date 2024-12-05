from django.shortcuts import render, redirect
from .models import Task
from .form import postTask

def post_task(request):
    if request.method == 'POST':
        form = postTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('tasks:task_list')  # Update with an appropriate redirect
    else:
        form = postTask()
    return render(request, 'task/postTask.html', {'form': form})

def task_list (request):
    task_list = Task.objects.all()
    context = {'tasks':task_list}
    return render(request,'task/task_list.html',context)



def task_detail(request,id):
    task_detail = Task.objects.get(id=id)
    context = {'tasks':task_detail}
    return render(request,'task/task_detail.html',context)