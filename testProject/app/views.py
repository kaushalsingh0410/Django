from django.shortcuts import render
from django.http import HttpResponse
from .form import UserForm
def index(request):

    data = {
        'title':'Index',
        'heading':'Form',
        'form':UserForm(),
        }
    return render(request,'app/index.html',data)

