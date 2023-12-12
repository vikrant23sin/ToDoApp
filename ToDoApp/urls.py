from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='todo'),
    path('del/<str:item_id>', remove, name='del')
]
