from django.urls import path
from ..views_dir import authView

urlpatterns = [
    path('login', authView.MyLoginView.as_view(), name='pageTo.login'),
]