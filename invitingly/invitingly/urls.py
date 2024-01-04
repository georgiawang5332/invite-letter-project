"""invitingly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from invitingly import *
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from information.forms import UserLoginForm, ResetPasswordForm, NewPasswordForm
from information.views import home_view, aboutus_view, contactus_view, afterlogin_view, adminclick_view, \
    admin_signup_view, admin_dashboard_view

urlpatterns = [
    # add a app
    path('', include('information.urls')),
    # path('student/', include('student.urls')),
    path('calendarMonths/', include('calendarMonths.urls')),
    path('invite/', include('invite.urls')),

    path('admin/', admin.site.urls),


    # 未加入會員的 navbars 可供新客戶觀看
    path('', home_view, name='home'),
    path('logout', LogoutView.as_view(template_name='info/logout.html'), name='logout'),
    # path('logout/', views.LogoutView.as_view(), name="logout"),

    path('aboutus', aboutus_view, name='aboutus'),
    path('contactus', contactus_view, name='contactus'),
    path('afterlogin', afterlogin_view, name='afterlogin'),

    path('adminclick', adminclick_view, name='adminclick'),
    path('adminlogin', LoginView.as_view(template_name='info/adminlogin.html', authentication_form=UserLoginForm), name='adminlogin'),
    # path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm),name="login"),

    path('adminsignup', admin_signup_view, name='adminsignup'),
    # path('signup/', signup, name="signup"),

    path('admin-dashboard', admin_dashboard_view, name='admin-dashboard'),
    # path('adminlogin', LoginView.as_view(template_name='info/login.html'), authentication_form=AdminUserLoginForm, name='adminlogin'),
    # path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=AdminUserLoginForm),name="login"),


    # 對於忘記密碼 可以有另一個分支
    path('password-reset/',
         views.PasswordResetView.as_view(template_name="info/reset_password.html", form_class=ResetPasswordForm),
         name="password_reset"),

    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name="info/reset_password_done.html"),
         name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(template_name="info/reset_password_confirm.html",
                                                form_class=NewPasswordForm), name="password_reset_confirm"),

    path('password-reset-complete/',
         views.PasswordResetCompleteView.as_view(template_name="info/reset_password_complete.html"),
         name="password_reset_complete"),

]

