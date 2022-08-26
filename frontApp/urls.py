from django.urls import path,include

urlpatterns = [
    path('', include('frontApp.urls_dir.dashboard')),
    path('trial/', include('frontApp.urls_dir.trial')),
    path('auth/', include('frontApp.urls_dir.auth')),
]