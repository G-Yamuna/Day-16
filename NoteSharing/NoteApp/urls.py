from django.urls import path
from NoteApp import views
from django.contrib.auth import views as ad

urlpatterns=[
    path('',views.home,name="hm"),
    path('aboutus/',views.aboutus,name="au"),
    path('contactus/',views.contactus,name="cu"),
    path('lg/',ad.LoginView.as_view(template_name='stc/login.html'),name="log"),
    path('rg/',views.regi,name="rge"),
    path('ds/',views.dashboard,name="dsh"),
    path('lgo/',ad.LogoutView.as_view(template_name='stc/logout.html'),name="logo"),
]