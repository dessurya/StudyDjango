import json
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin # wajib
from django.shortcuts import redirect
from django.http import JsonResponse

class loginSessionMiddleware(MiddlewareMixin):
    
    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        # Code that is executed in each request before the view is called
        response = self.get_response(request)
        # Code that is executed in each request after the view is called
        return response

    def process_request(self, request):
        # This code is executed just before the request is called
        if 'loginSess' in request.session:
            request.loginSess = json.loads(request.session['loginSess'])
        else:
            request.loginSess = None

    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        ajaxCek = request.is_ajax()
        current_uri = request.path

        if request.loginSess == None:
            if current_uri != '/auth/login':
                if ajaxCek == False:
                    return redirect('auth.login')
                elif ajaxCek == True:
                    return JsonResponse({
                        'response' : {
                            'login' : False, 'msg' : 'Your session is time out!'
                        }
                    })
        else:
            timoutSess = datetime.now() > datetime.strptime(request.loginSess['timeout'], "%Y-%m-%d %H:%M:%S.%f")
            if timoutSess == True:
                try:
                    del request.session['loginSess']
                except:
                    pass
                if current_uri != '/auth/login':
                    if ajaxCek == False:
                        return redirect('auth.login')
                    elif ajaxCek == True:
                        return JsonResponse({
                            'response' : {
                                'login' : False, 'msg' : 'Your session is time out!'
                            }
                        })
            elif timoutSess == False and current_uri == '/auth/login':
                return redirect('pageTo.dashboard')

    # def process_exception(self, request, exception):
        # This code is executed if an exception is raised

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        return response