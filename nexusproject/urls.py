"""nexusproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from publicapp import views as v1
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static

from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('contractor/',v1.Contractorlist),
    path('company/',v1.Companieslist),

    path('delete1/<int:id>/',v1.Contractorlistdelete),
    path('delete2/<int:id>/',v1.Companieslistdelete),

    path('detail1/<int:id>/',v1.Contractorlistdetail),
    path('detail2/<int:id>/',v1.Companieslistdetail),

    path('update1/<int:id>/',v1.Contractorlistupdate),
    path('update2/<int:id>/',v1.Companieslistupdate),

    path('create/',v1.Contractorlistcreate),
    path('create2/',v1.Companieslistcreate),
    path('',v1.Joblist),
    path('createjob/',v1.Jobcreate),
    path('deletejob/<int:id>/',v1.Jobdelete),
    path('detailjob/<int:id>/',v1.Jobdetail),
    path('updatejob/<int:id>/',v1.Jobupdate),
    path('login/',v1.loginview),
    path('logout/',v1.logoutview),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 










]
