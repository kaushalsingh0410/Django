from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .form import UserForm
from .models import User
from django.template.loader import render_to_string
def index(request,pk = None):

    data = {
        'title':'Index',
        'heading':'Form',
        'form':UserForm(),
        }
    print('inside index request',request.method)
    if request.method == 'POST':
        form = None
        if pk:
            user = User.objects.get(pk =pk)
            form = UserForm(request.POST,instance = user)
            print('This is update')
            # name = request.POST.get('name')
            # email = request.POST.get('email')
            # comment = request.POST.get('comment')
            # user = User.objects.create(name =name,email = email,comment = comment)
            
            # tableHtml = render_to_string('app/table.html',{'query':[user]})
            # return JsonResponse({'msg':'Good',"tableHtml":tableHtml})
            # return JsonResponse({'msg':'update'})
        else:
            form = UserForm(request.POST)
            # name = request.POST.get('name')
            # email = request.POST.get('email')
            # comment = request.POST.get('comment')
            # user = User.objects.create(name =name,email = email,comment = comment)
        if form.is_valid():
            user = form.save()
            
            tableHtml = render_to_string('app/table.html',{'query':[user]})
            return JsonResponse({'msg':'Good',
                                 'id':user.id,
                                 "tableHtml":tableHtml,
                                 'update':pk is not None})
          




        
    data['tableHtml'] = render_to_string('app/table.html',{"query":User.objects.order_by('-id')})
    # print('table',data['table'],type(data['table']),len(data['table']))

    return render(request,'app/index.html',data)



def delete(request):
    if request.method == 'POST':
        print('this is delete',request.POST)
        User.objects.get(pk = request.POST.get('pk')).delete()
        return JsonResponse({'msg':True})


def table(request):
    # return render(request,'app/tableView.html'  )
    return render(request,'app/tableView.html',{'tableHtml':render_to_string('app/table.html',{'query':User.objects.all()})})
