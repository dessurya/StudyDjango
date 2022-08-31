from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail

# from ..models_dir.user import UserModel

def Index(request):
    if request.method == 'GET':
        template_name = 'page/dashboard.html'
        return render(request, template_name, {'params':None})
    else:
        pass

def Sendmail(request):
    if request.method == 'GET':
        subject = 'TESTING EMAIL DARI JANGO'
        message = 'INI TESTING EMAIL KIRIM DARI DJANGO'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['fourline66@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
        return JsonResponse({
            'response' : {
                'msg':'success',
                'subject':subject,
                'message':message,
                'email_from' :email_from
            }
        })
    else:
        pass