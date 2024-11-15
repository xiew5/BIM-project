"""
URL configuration for PC_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),  
    path("list", book_list, name="book_list"),
    path("add/<str:name>/<str:author>/<slug:date>/<str:price>", addbook, name="add"),
    
    path("d/n/<str:d_name>", del_book_name, name="del_book_name"),
    path("d/a/<str:d_author>", del_book_author, name="del_book_author"),
    
    path("d/n/<str:d_name>/<int:d_num>/", del_book_name_m, name="del_book_name_m"),
    path("d/a/<str:d_author>/<int:d_num>/", del_book_author_m, name="del_book_author_m"),

    path("author/<str:author_name>", author_input, name="author_name"),
    path("author_filter", author_filter, name="author_filter"),

    path("up/<int:u_id>/<str:u_name>/<str:u_author>/<slug:u_date>/<str:u_price>", update_book_data, name="update_book_data"),

    path("home", home, name="home"),
    path("save", save_book_data, name="save_book_data"),
    #path("author", author_input, name="author_input"),
]
