"""djangobasic URL Configuration

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
from django.urls import path
from djangobasic import views

urlpatterns = [
    path('',views.masterPage),
    path('admin/', admin.site.urls),
    path('aboutus/',views.aboutUs),
    path('course/',views.course),
    path('course/<int:course_id>',views.courseDetailsAsInt),
    path('course/<str:course_name>',views.courseDetailsAsString),
    path('course/<slug:course_slug>',views.courseDetailsAsSlug),
    path('emplist/',views.EmpFetch),
    path('home/',views.HomePage,name="home"),
    path('about/',views.AboutPage,name="about"),
    path('service/',views.ServicePage,name="service"),
    path('team/',views.TeamPage,name="team"),
    path('contact/',views.ContactPage,name="contact")
]