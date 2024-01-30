from django.urls import path
from . import views
from capstoneapp import views
from .views import capstoneapi_list, SaveFile, home_capstone_view

urlpatterns = [
     # Home page URL
    path('', home_capstone_view, name='home'),
    #path('', views.index, name='index'),
    path('capstoneapi/', capstoneapi_list, name='capstoneapi-list'),
    path('capstoneapi/<int:id>/', capstoneapi_list, name='capstoneapi-detail'),

     # File upload URL
    path('capstoneapi/SaveFile', SaveFile, name='save-file'),

]



