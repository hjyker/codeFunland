# -*- coding: utf-8 -*-


import logging

from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import (
    authenticate, login, logout
)
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
# from django.core.files import File

from users.forms import (
    UserLoginForm, UserRegisterForm, UserProfileForm,
    ImageFileForm, changepasswordForm
)
from users.models import UserProfile
from courses.models import LearnRecord
from users.utils import handle_upload_files


logger = logging.getLogger("views_error")

COOKIE_EXPIRY = 86400  # second, 2 days
SESSION_IS = 0  # if remember_me == False, it's session


def user_login(request):
    form = UserLoginForm()

    if request.user.is_authenticated():
        return redirect(
            reverse("courses:courses_index", args=[])
        )

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(COOKIE_EXPIRY)
                else:
                    request.session.set_expiry(SESSION_IS)

                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Sign in Successful!'
                )

                user_record = LearnRecord.objects.filter(user=user)

                if not user_record.exists():
                    return redirect(
                        reverse('courses:courses_index', args=[])
                    )
                else:
                    return redirect(
                        reverse("labs:show_labs",
                            args=[user_record.first().course.id]
                        )
                    )
            else:
                messages.add_message(
                    request,
                    messages.WARING,
                    'Sorry, please active your account!'
                )
                return redirect(
                    reverse('users:user_login', args=[])
                )
        else:
            messages.add_message(request, messages.ERROR, 'Sign in failure!')
            return redirect(
                reverse('users:user_login', args=[])
            )
            # return render(
                # request,
                # 'users/login.html',
                # {'form': form}
            # )

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
            reverse('start:start_index', args=[])
    )


def user_register(request):
    if request.user.is_authenticated():
        return redirect(
            reverse("courses:courses_index", args=[])
        )

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
                reverse('users:user_login', args=[])
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
            try:
                file = handle_upload_files(request.FILES.get('avatar_link', ""), request)
                logger.error(file)
                current_user.userprofile.avatar_link = 'avatar/' + file.name
                current_user.userprofile.save()
            except IOError, ex:
                logger.error(ex)
                messages.add_message(request,
                    messages.ERROR,
                    "Failure of update avatar."
                )
            except ValueError, ex:
                logger.error(ex)
                error_msg = "Failure of updated avater: %s" % ex
                messages.add_message(request,
                    messages.ERROR,
                    error_msg
                )
            except Exception, ex:
                logger.error(ex)
                messages.add_message(request, messages.ERROR, ex)
            finally:
                return render(request,
                    'users/profile.html',
                )


    form = UserProfileForm()
    image_form = ImageFileForm()
    return render(request,
        'users/update_profile.html',
        {
            'form': form,
            'image_form': image_form,
        }
    )


def change_pwd(request):
    if not request.user.is_authenticated():
        return redirect(reverse("users:user_login", args=[]))
    form = changepasswordForm()
    if request.method=="POST":
        form = changepasswordForm(request.POST.copy())
        if form.is_valid():
            username = request.user.username
            oldpassword = form.cleaned_data["oldpassword"]
            newpassword = form.cleaned_data["newpassword"]
            newpassword1 = form.cleaned_data["newpassword1"]
            user = authenticate(username=username,password=oldpassword)
            if user: #原口令正确
                if newpassword == newpassword1:#两次新口令一致
                    user.set_password(newpassword)
                    user.save()
                    return redirect(reverse("users:user_profile", args=[request.user.id]))
                else:#两次新口令不一致
                    messages.add_message(
                        request,
                        messages.ERROR,
                        '两次密码不一致'
                    )
                    return render(
                        request,
                        "users/changepassword.html",
                        {'form': form}
                    )
            else:  #原口令不正确
                if newpassword == newpassword1:#两次新口令一致
                    messages.add_message(
                        request,
                        messages.ERROR,
                        '旧密码错误'
                    )
                    return render(
                        request,
                        "users/changepassword.html",
                        {'form': form}
                    )
                else:#两次新口令不一致
                    messages.add_message(
                        request,
                        messages.ERROR,
                        '两次新密码不一致'
                    )
                    return render(
                        request,
                        "users/changepassword.html",
                        {'form': form}
                    )
    return render(
        request,
        "users/changepassword.html",
        {'form': form}
    )
