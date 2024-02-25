from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import TaskForms
from webapp.models import Task


class TaskCreateView(TemplateView):
    template_name = 'tasks_create.html'
    form_class = TaskForms

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForms()
        return render(request, 'tasks_create.html', context=context)

    def post(self, request, *args, **kwargs):
        form = TaskForms(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
            )
            task.types.set(types)
            return redirect('tasks_view', pk=task.pk)
        return render(request, 'tasks_create.html', {'form': form})
    def form_valid(self, form):
        self.task = form.save()
        return redirect('tasks_view', pk=self.task.pk)



class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    form_class = TaskForms

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('article_view', pk=self.task.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForms(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'types': task.types.all()
        })
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForms(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.types.set(types)
            task.save()
            return redirect('tasks_view', pk=task.pk)
        else:
            return render(request, 'task_update.html', {'form': form})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')
class TaskCreateView(TemplateView):
    template_name = 'tasks_create.html'
    form_class = TaskForms

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForms()
        return render(request, 'tasks_create.html', context=context)

    def post(self, request, *args, **kwargs):
        form = TaskForms(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
            )
            task.types.set(types)
            return redirect('tasks_view', pk=task.pk)
        return render(request, 'tasks_create.html', {'form': form})
    def form_valid(self, form):
        self.task = form.save()
        return redirect('tasks_view', pk=self.task.pk)



class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    form_class = TaskForms

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('article_view', pk=self.task.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForms(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'types': task.types.all()
        })
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForms(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.types.set(types)
            task.save()
            return redirect('tasks_view', pk=task.pk)
        else:
            return render(request, 'task_update.html', {'form': form})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')
