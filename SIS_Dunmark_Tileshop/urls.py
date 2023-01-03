"""SIS_Dunmark_Tileshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('VisitorsPage.urls')),
    path('Login/', include('LoginAuthentication.urls')),
    path('Dashboard/', include('Dashboard.urls'), name="dashboard"),
    path('UserManagement/', include('UserManagement.urls')),
    path('POS/', include('PointOfSale.urls')),
    path('SalesTransaction/', include('SalesTransaction.urls')),
    path('ProductManagement/', include('ProductManagement.urls')),
    path('ReturnProduct/', include('ReturnProduct.urls')),
    path('Settings/', include('Settings.urls')),
    path('AuditTrail/', include('AuditTrail.urls')),
    path('Reports/', include('Reports.urls')),
    path('AboutSystem/', include('AboutSystem.urls')),
]
