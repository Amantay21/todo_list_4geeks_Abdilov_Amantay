from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Task, status_choices


def index_view(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'index.html', context)


def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})


def create_task_view(request):
    if request.method == "GET":
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == "POST":
        task = Task.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            completed=request.POST.get('completed'),
            date_of_completion=request.POST.get('date_of_completion')
        )

        return redirect('task_view', pk=task.pk)


def update_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_update.html', {'task': task, 'status_choices': status_choices})
    elif request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.competed = request.POST.get('competed')
        task.date_of_completion = request.POST.get('date_of_completion')
        task.save()
        return redirect('task_view', pk=task.pk)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
