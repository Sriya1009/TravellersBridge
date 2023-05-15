from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='loginmodule'
urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.handeLogin, name="handleLogin"),
    path('signup/', views.handleSignUp, name="handlesignup"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('vacation/', views.vacation, name="vacation"),
    path('car/', views.car, name="car"),
    path('flight/', views.flight, name="flight"),
    path('contact/', views.contact, name="contact"),
    path('hotel/', views.hotel, name="hotel"),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset_password/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),
]