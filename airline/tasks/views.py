from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = ["foo", "bar", "baz"]


class NewTasksForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    """
    It renders the `index.html` template, passing in the `tasks` variable

    :param request: The request object is the first parameter to every view function. It contains information about the
    request that was made to the server
    :return: The index.html file is being returned.
    """
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    """
    If the request is a POST request, then validate the form and add the task to the list of tasks

    :param request: The request object is a Python object that contains all the information about the request that was sent
    to the server
    :return: The form is being returned.
    """
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTasksForm()
    })
