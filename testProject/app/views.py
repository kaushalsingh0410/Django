from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .form import UserForm
def index(request):

    data = {
        'title':'Index',
        'heading':'Form',
        'form':UserForm(),
        }
    print('inside index request',request.method)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        print('name',name)
        print('email',email)
        print('comment',comment)
        return JsonResponse({'msg':'Good'})
    return render(request,'app/index.html',data)

