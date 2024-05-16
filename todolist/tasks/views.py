from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import List, Task
from django.shortcuts import get_object_or_404


# Create your views here.
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'tasks/login.html')


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page.
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})



def logoutView(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
def homeView(request):
    context = {}
    if request.user.is_authenticated:
        lists = List.objects.filter(user = request.user)
        loggedIn = "in"
        context = {'lists': lists,'loggedIn':loggedIn}
    else:
        loggedIn = 'out'
        context = {'loggedIn': loggedIn}

    
    return render(request, 'tasks/home.html',context)


@login_required(login_url='login')
def createListView(request):
    if request.method == 'POST':
        listTitle = request.POST['list']
        List.objects.create(
            user = request.user,
            title = listTitle
        )
        messages.success(request, "List Created Successfully!")
        return redirect('home')
    
    context = {}
    return render(request, 'tasks/list_form.html', context)




@login_required(login_url='login')
def createTaskView(request,pk):
    task_list = get_object_or_404(List, id=pk, user=request.user)
    print("test list:")
    # list_instance = List.objects.get(id = pk)
    if request.method == 'POST':
        # listTitle = request.POST['list']
        taskTitle = request.POST['title']

        Task.objects.create(
            list = task_list,
            title = taskTitle
        )
        return redirect('home') 
    context = {'list':task_list}
    return render(request, 'tasks/home.html', context)





def updateTaskStatusView(request, pk):
    task = get_object_or_404(Task,id = pk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    # print(task)
    return redirect('home')
