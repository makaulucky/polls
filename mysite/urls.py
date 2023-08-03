from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("Home Page")

urlpatterns = [
    path('', index),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
