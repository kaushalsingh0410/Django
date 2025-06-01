from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .form import UserForm
from .models import User
from django.template.loader import render_to_string
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
        user = User.objects.create(name =name,email = email,comment = comment)
        
        tableHtml = render_to_string('app/table.html',{'query':[user]})
        return JsonResponse({'msg':'Good',"tableHtml":tableHtml})



        
    data['tableHtml'] = render_to_string('app/table.html',{"query":User.objects.order_by('-id')})
    # print('table',data['table'],type(data['table']),len(data['table']))

    return render(request,'app/index.html',data)

