from django.views import View
from django.shortcuts import render

class Index(View):
    template_name = 'page/dashboard.html'
    def get(self, request):
        return render(request, self.template_name)