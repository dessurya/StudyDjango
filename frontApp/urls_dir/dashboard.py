from django.urls import path
from ..views_dir import dashboardView

urlpatterns = [
    path('', dashboardView.Index.as_view(), name='pageTo.dashboard'),
]