from django.urls import path
from projects import views
from django.conf.urls import include

urlpatterns = [
    path('', views.all_projects),
]
