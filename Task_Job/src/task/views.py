from django.shortcuts import render, redirect
from .models import Task
from .form import PostTask

def post_task(request):
    if request.method == 'POST':
        form = PostTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('tasks:task_list')  # Update with an appropriate redirect
    else:
        form = PostTask()
    return render(request, 'task/postTask.html', {'form': form})
