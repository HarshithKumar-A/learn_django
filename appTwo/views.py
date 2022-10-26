from django.http import HttpResponse
from django.shortcuts import render
from appTwo.models import User
from . import forms

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def user(request):
    # helpdict = {'help_insert':'HELP PAGE'}
    user_list  = User.objects.order_by('first_name')
    date_dict = {'access_records' : user_list}
    return render(request,'appTwo/user.html',context=date_dict)

def user_entry(request):
    form = forms.MyNewForm()
    if request.method == "POST":
        form = forms.MyNewForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR")

    return render(request, 'appTwo/form_page.html', {'form':form})