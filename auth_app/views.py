from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
# def index(request):
#     return render(request, 'ex_user/index.html')
def index(request):
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def profile(request):
    return render(request, 'ex_user/index.html')