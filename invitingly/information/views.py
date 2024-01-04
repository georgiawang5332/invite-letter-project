from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# from invite import forms as IFORM
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from information.forms import *
from information.forms import UserRegistrationForm
from invite import models as IMODEL
# from student import models as SMODEL
from . import forms


# Create your views here.
# Django URL重定向的HttpResponseDirect, redirect和reverse方法 : https://www.twblogs.net/a/5ed4e876666708e4e28ee6e8

# NAVBAR START
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'index.html')


def is_invite(user):
    return user.groups.filter(name='INVITE').exists()


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def aboutus_view(request):
    return render(request, 'info/aboutus.html')


def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name = sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name) + ' || ' + str(email), message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER,
                      fail_silently=False)
            return render(request, 'info/contactussuccess.html')
    return render(request, 'info/contactus.html', {'form': sub})


def afterlogin_view(request):
    if is_student(request.user):
        return redirect('student/student-dashboard')

    elif is_invite(request.user):
        return redirect('invite/invite-dashboard')
    else:
        return redirect('admin-dashboard')


def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def admin_signup_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'info/adminsignup.html', context)


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict = {
        # 'total_student': SMODEL.Student.objects.all().count(),
        'total_invite': IMODEL.Invite.objects.all().count(),
        # 'total_course': models.Course.objects.all().count(),
        # 'total_question': models.Question.objects.all().count(),
    }
    return render(request, 'info/admin_dashboard.html', context=dict)

# NAVBAR END



