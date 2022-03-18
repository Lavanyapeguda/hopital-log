from django.contrib import admin
from django.conf.urls import url,include
from application1 import views


urlpatterns = [
    url(r'^Hospital/', views.Hospital,name="Hospital"),
    url(r'^home/', views.home,name="home"),
    url(r'^Phome/', views.Phome,name="Phome"),
    url(r'^signup/',views.signup,name="signup"),
    url(r'^signin/',views.signin,name="signin"),
    url(r'^signout/',views.signout,name="signout"),
    url(r'^Psignin/',views.Psignin,name="Psignin"),
    url(r'^Psignup/',views.Psignup,name="Psignup"),
    url(r'^Psignout/',views.Psignout,name="Psignout"),
]
    
