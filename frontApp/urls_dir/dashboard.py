from django.urls import path
from ..views_dir import dashboardView

urlpatterns = [
    path('', dashboardView.Index, name='pageTo.dashboard'),
    path('sendmail', dashboardView.Sendmail, name='sendmail'),
    path('createjson', dashboardView.CreateJSON, name='createjson'),
    path('createimgbase64', dashboardView.CreateIMGBASE64, name='createimgbase64'),
]