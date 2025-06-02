from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .form import UserForm
from .models import User
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.paginator import Paginator



def index(request,pk = None):
    print('inside index')
    data = {'title':'Index','heading':'Form','form':UserForm(),}
    print('inside index request',request.method)
    if request.method == 'POST':
        form = None
        if pk:
            user = User.objects.get(pk =pk)
            form = UserForm(request.POST,instance = user)
        else:
            form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            tableHtml = render_to_string('app/partials/table.html',{'query':[user]})
            return JsonResponse({'msg':'Good','id':user.id,"tableHtml":tableHtml,'update':pk is not None})

    page_number = request.GET.get('page')
    user = User.objects.order_by('-id')
    paginator = Paginator(user,3)
    page_obj = paginator.get_page(page_number)
    tableHtml = render_to_string('app/partials/table.html',{"query":page_obj})
    paginator = render_to_string('app/partials/paginator.html',{"page_obj":page_obj})

    if page_number:
        return JsonResponse({'tableHtml':tableHtml,'paginator':paginator})        
          
        
    data['tableHtml'] = tableHtml 
    data['paginator'] = paginator 
    data['page_obj'] = page_obj 

    print('paginator',paginator)
    print('page_obj',page_obj)
    print('page_number',page_number)

    return render(request,'app/index.html',data)



def delete(request):
    if request.method == 'POST':
        print('this is delete',request.POST)
        User.objects.get(pk = request.POST.get('pk')).delete()
        return JsonResponse({'msg':True})


def table(request):
    return render(request,'app/tableView.html',{'tableHtml':render_to_string('app/partials/table.html',{'query':User.objects.all()})})

def search(request):
    if request.method == 'POST':
        searchquery = request.POST.get('searchquery')
        rows = User.objects.filter(Q(name__icontains = searchquery) | Q(email__icontains = searchquery) | Q(comment__icontains = searchquery))
        tableHtml = None
        if len(rows):
            tableHtml = render_to_string('app/partials/table.html',{'query':rows})
        else:
            tableHtml = f'''<tr >
                        <td colspan = '5' class = 'text-center' > No record found for <b>{searchquery} </b></td>
                        </tr>'''

        return JsonResponse({'tableHtml':tableHtml})
    return JsonResponse({'msg':'this is search'})
