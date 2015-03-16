# -*- coding: utf-8 -*-


import hashlib

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate, login, logout
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files import File

from users.forms import (
    UserLoginForm, UserRegisterForm, UserProfileForm
)
from users.models import UserProfile


def user_login(request):
    form = UserLoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(86400)
                else:
                    request.session.set_expiry(0)

                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Sign in Successful!'
                )
                return redirect(
                    reverse('start.views.index', args=[])
                )
            else:
                messages.add_message(
                    request,
                    messages.WARING,
                    'Sorry, please active your account!'
                )
                return redirect(
                    reverse('users.views.user_login', args=[])
                )
        else:
            messages.add_message(request, messages.ERROR, 'Sign in failure!')
            return redirect(
                reverse('users.views.user_login', args=[])
            )

    return render(
        request,
        'users/login.html',
        {'form': form}
    )


@login_required
def user_logout(request):
    logout(request)
    messages.add_message(
        request,
        messages.INFO,
        'You have been logout.'
    )
    return redirect(
        reverse('start.views.index', args=[])
    )


def user_register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(data=request.POST)

        if register_form.is_valid():
            new_user = register_form.save()
            new_user.set_password(new_user.password)
            new_user.save()

            new_profile = UserProfile(user=new_user)
            new_profile.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                'Register successful!You need to sign in, Now!'
            )
            return redirect(
                reverse('users.views.user_login', args=[])
            )
        else:
            return render(
                request,
                "users/register.html",
                {"register_form": register_form}
            )
    else:
        register_form = UserRegisterForm()

    return render(
        request,
        'users/register.html',
        {
            'register_form': register_form,
        }
    )


@login_required
def user_profile(request, user_id):
    return render(
        request,
        'users/profile.html'
    )


@login_required
def update_avatar(request, user_id):
    current_user = request.user
    if int(current_user.id) != int(user_id):
        return HttpResponse('turn to 404!')

    if request.method == "POST":

        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
            file = handle_upload_files(request.FILES['avatar_link'])
            current_user.userprofile.avatar_link = 'avatar/' + file.name
            current_user.userprofile.save()
            # except:
                # messages.add_message(
                    # request,
                    # messages.ERROR,
                    # 'update avatar faiure!'
                # )
                # return redirect(
                    # reverse('users.views.update_avatar', args=[user_id])
                # )
            return redirect(
               reverse('users.views.user_profile', args=[user_id])
           )

    form = UserProfileForm()
    return render(
        request,
        'users/update_profile.html',
        {'form': form}
    )

def handle_upload_files(file):
    file.name = file.name.encode('utf-8')
    file.name = "%s.jpg" % hashlib.md5(file.name).hexdigest()
    file_path = "/home/zhangyd/codeFunland/media/avatar/" + file.name
    with open(file_path, "wb+") as info:
        for chunk in file.chunks():
            info.write(chunk)
    return file


# def test1(request):
    # return HttpResponse('test1')

# def test2(request, var, test_var):
    # return HttpResponse('test2 %s %s' % (var, test_var))
