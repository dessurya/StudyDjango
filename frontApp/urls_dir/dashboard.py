from django.urls import path
from ..views_dir import dashboardView

urlpatterns = [
    path('', dashboardView.Index, name='pageTo.dashboard'),
    path('sendmail', dashboardView.Sendmail, name='sendmail'),
]