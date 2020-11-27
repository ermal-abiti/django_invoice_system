"""invoice_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from invoice_system.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('',  dashboardView, name='dashboard_url'),
    path('fletpercjellja_create/', FletpercjelljaCV.as_view(), name='fletpercjellja_create_url'),
    path('fletpercjellja_listview/', FletpercjelljaLV.as_view(), name='fletpercjellja_listview_url'),
    path('fletpercjellja_detail/<slug:f_id>/', fletpercjellja_detail_view, name='fletpercjellja_detail_url'),

    path('produkt_create/', ProductCV.as_view(), name='produkt_create_url'),
    path('produkt_listview/', produkt_listview, name='produkt_listview_url'),
    path('produkt_update/<slug:pk>/', ProductUV.as_view(), name='produkt_update_url'),
    path('produkt_detail/<slug:pk>/', ProductDV.as_view(), name='produkt_detail_url'),
     path('produkt_delete/<slug:pk>/', ProductDelete.as_view(), name='produkt_delete_url'),

]
