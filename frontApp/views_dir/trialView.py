import math
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from ..models_dir.user import UserModel


def Index(request):
    if request.method == 'GET':
        template_name = 'page/trial.html'
        arrConfig = [
            {
                'label' : 'Tools',
                'field' : 'tools',
                'order' : False,
                'seacrh' : None,
            },
            {
                'label' : 'Name',
                'field' : 'name',
                'order' : True,
                'seacrh' : 'text',
            },
            {
                'label' : 'Email',
                'field' : 'email',
                'order' : True,
                'seacrh' : 'email',
            },
            {
                'label' : 'Created At',
                'field' : 'created_at',
                'order' : True,
                'seacrh' : None,
            }
        ]
        return render(request, template_name, {
            'config':{
                'table_list_view':arrConfig
            }
        })
    else:
        pass
    

def ListData(request):
    if request.method == 'GET':
        response = {
            'email' : request.GET['email'],
            'name' : request.GET['name'],
            'show' : int(request.GET['show']),
            'order_by' : request.GET['order_by'],
            'order_by_value' : request.GET['order_by_value'],
            'halaman' : int(request.GET['halaman'])
        }
        offset = (response['halaman']-1)*response['show']
        limit = offset+response['show']

        if response['order_by_value'] == 'ASC':
            set_order = response['order_by']
        else:
            set_order = '-'+response['order_by']

        user = UserModel.objects
        if response['email'] != None and response['email'] != '':
            user = user.filter(email__contains=response['email'])
        if response['name'] != None and response['name'] != '':
            user = user.filter(name__contains=response['name'])

        user = user.using('servlaraqu')
        userCount = user.count()
        response['dataCount'] = userCount
        
        userPaginate = user.all().order_by(set_order)[offset:limit]
        data = list(userPaginate.values())
        response['data'] = data

        last_page = math.ceil(userCount/response['show'])
        response['last_page'] = last_page

        return JsonResponse({
            'response' : response
        })
    else:
        pass

def OpenData(request):
    if request.method == 'GET':
        response = { 'id' : request.GET['id'] }
        user = UserModel.objects.filter(id=response['id']).using('servlaraqu').all().order_by('id')
        response['data'] = list(user.values())[0]
        return JsonResponse({
            'response' : response
        })
    else:
        pass

def DeleteData(request):
    if request.method == 'POST':
        response = { 'id' : request.POST['id'] }
        users = UserModel.objects.using('servlaraqu').get(id=response['id'])
        users.delete()
        response['msg'] = 'Success Delete Data!'
        return JsonResponse({
            'response' : response
        })
    else: 
        pass

def StoreData(request):
    if request.method == 'POST':
        response = {
            'name' : request.POST['name'],
            'email' : request.POST['email'],
            'id' : request.POST['id'],
        }

        if response['id'] == '' or response['id'] == '0' or response['id'] == 0 or response['id'] == None:
            users = UserModel.objects.using('servlaraqu').create(name=response['name'],email=response['email'])
        else:
            users = UserModel.objects.using('servlaraqu').get(id=response['id'])
            users.name = response['name']
            users.email = response['email']
            users.save()

        response['id'] = users.id
        return JsonResponse({
            'response' : response
        })
    else:
        pass