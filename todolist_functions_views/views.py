from django.http import HttpResponse
from django.shortcuts import redirect, render

from todolist_functions_views.models import Todo
from . import status_task
from todolist_functions_views.forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json


def add(request):
    LIST_STATUS = map(
        lambda task_tuple: task_tuple[0], status_task.STATUS_TASK)
    if(request.method == "POST"):
        taskForm = TodoForm(request.POST)
        if(taskForm.is_valid()):
            status = taskForm.cleaned_data["status"]
            task = taskForm.cleaned_data["task"]
            new_todo = Todo(task=task, status=status,
                            user_id=int(request.session["user_id"]))
            new_todo.save()
            return redirect('/')
        print(
            f"------------------\n{taskForm.error_class}\n-----------------------")
        return render(request, "add_task.html", {"form": taskForm})

    return render(request, "add_task.html", {"list_status": LIST_STATUS, "form": ""})


def list(request):
    result = Todo.objects.all().filter(user_id=request.session['user_id'])
    all_todos = {}
    for status in status_task.STATUS_TASK:

        all_todos[status[0]] = result.filter(status=status[0])

    return render(request, "all_tasks.html", {"all_todos": all_todos})
# @login_required(login_url='/users/signin')


def update(request, id):
    LIST_STATUS = map(
        lambda task_tuple: task_tuple[0], status_task.STATUS_TASK)
    task = Todo.objects.filter(id=id).first()
    if(request.method == 'POST'):

        taskForm = TodoForm(request.POST)
        if(taskForm.is_valid()):
            Todo.objects.filter(id=id).update(
                task=taskForm.cleaned_data['task'], status=taskForm.cleaned_data["status"])
            return redirect("/")
        return render(request, 'update_task.html', {'form': taskForm})
    print('lis', LIST_STATUS)
    return render(request, "update_task.html", {"task": task, "list_status": LIST_STATUS})


def delete(request, id):
    try:
        task = Todo.objects.filter(id=id).first().delete()
        return HttpResponse(json.dumps({'status': 'SUCCESSFUL'}))
    except BaseException as e:
        return HttpResponse(json.dumps({'status': 'FAILED', 'message': str(e)}))
