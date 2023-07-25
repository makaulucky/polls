from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("Home Page")

urlpatterns = [
<<<<<<< HEAD
    path('', include('polls.urls')),
=======
    path('', index),
>>>>>>> 8f8e74f6c24c359d1710c3afdf8b87d549631f10
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
