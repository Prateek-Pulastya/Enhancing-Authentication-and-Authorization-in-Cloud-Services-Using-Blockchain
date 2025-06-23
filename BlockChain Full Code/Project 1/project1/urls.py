"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from project1_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    ##########login start
    url(r'^$',show_index),
    url(r'^show_index', show_index, name="show_index"),
    url(r'^check_login', check_login, name="check_login"),
    url(r'^logout',logout,name="logout"),
    url(r'^register',register,name="register"),
    ##########login end

    ################Admin start
    url(r'^show_home_admin',show_home_admin,name="show_home_admin"),
    url(r'^show_request_admin',show_request_admin,name="show_request_admin"),
    url(r'^approve',approve,name="approve"),
    url(r'^reject',reject,name="reject"),
    url(r'^display_view_users',display_view_users,name="display_view_users"),
    url(r'^show_home_user',show_home_user,name="show_home_user"),
    url(r'^show_upload_file_user',show_upload_file_user,name="show_upload_file_user"),
    url(r'^upload_file',upload_file,name="upload_file"),
    url(r'^view_my_files_user',view_my_files_user,name="view_my_files_user"),
    url(r'^check_download',check_download,name="check_download"),
    url(r'^do_verify',do_verify,name="do_verify"),
    url(r'^download',download,name="download"),
]
