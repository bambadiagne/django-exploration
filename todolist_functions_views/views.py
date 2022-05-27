from django.shortcuts import redirect, render

from todolist_functions_views.models import Todo
from . import status_task
from todolist_functions_views.forms import TodoForm


def add(request):
    list_status = map(
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

    return render(request, "add_task.html", {"list_status": list_status, "form": ""})


def list(request):
    all_todos = Todo.objects.all()

    return render(request, "all_tasks.html", {"all_todos": all_todos})
