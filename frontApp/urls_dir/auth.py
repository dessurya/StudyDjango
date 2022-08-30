from django.urls import path
from ..views_dir import authView

urlpatterns = [
    path('login', authView.Index, name='auth.login'),
    path('logout', authView.Logout, name='auth.logout'),
]