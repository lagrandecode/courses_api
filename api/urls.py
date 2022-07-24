from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from api import views

urlpatterns = [
    path('api/',views.api_list),
    path('api/<int:pk>', views.apidetail)
]




