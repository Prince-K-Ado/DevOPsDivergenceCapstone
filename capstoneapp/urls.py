from django.urls import path
from . import views
from django.contrib import admin
from capstoneapp import views
from .views import capstoneapi_list, SaveFile, home_capstone_view, capstoneapi_detail

urlpatterns = [
     # Home page URL
    path('', home_capstone_view, name='home'),
    #path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('capstoneapi/', capstoneapi_list, name='capstoneapi-list'),
    path('capstoneapi/<int:id>/', capstoneapi_detail, name='capstoneapi-detail'),
     # File upload URL
    path('capstoneapi/SaveFile', SaveFile, name='save-file'),

]



