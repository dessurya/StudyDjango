import json
from datetime import datetime, timedelta
from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse

from ..models_dir.user import UserModel

def Index(request):
	if request.method == 'GET':
		template_name = 'page/login.html'
		return render(request, template_name, {'params':None})
	elif request.method == 'POST':
		response = { 
			'email' : request.POST['email'],
			'password' : request.POST['password'],
		}
		user = UserModel.objects.filter(email=response['email']).using('servlaraqu')
		userCount = user.count()
		if userCount == 0:
			return JsonResponse({
				'response' : {
					'login' : False, 'msg' : 'Invalid login!', 'userCount' : userCount
				}
			})
		else:
			user = user.order_by('id').values()
			userList = list(user)[0]
			# cek password || saat ini di bypass
			userList['timeout'] = datetime.now() + timedelta(hours=5)
			# userList['timeout'] = datetime.now() + timedelta(seconds=35)
			loginData = json.dumps(userList, default=str) 
			request.session['loginSess'] = loginData
			return JsonResponse({
				'response' : { 'login':True, 'msg':'Success login!' }
			})
	else:
		pass

def Logout(request):
	try:
		del request.session['loginSess']
	except:
		pass
	return redirect('auth.login')