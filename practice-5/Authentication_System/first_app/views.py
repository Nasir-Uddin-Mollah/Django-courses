from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('homepage')

    else:
        form = forms.SignupForm()
    return render(request, 'signup.html', {'form': form, 'type': 'Signup'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login information incorrect')
                return redirect('signup')

    else:
        form = AuthenticationForm()
    return render(request, 'signup.html', {'form': form, 'type': 'Login'})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('homepage')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')

    else:
        form = PasswordChangeForm(request.user)
        for field in form.fields.values():
            field.help_text = None

    return render(request, 'passchange.html', {'form': form, 'type': 'Password Change'})


@login_required
def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Set Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')

    else:
        form = SetPasswordForm(request.user)
        for field in form.fields.values():
            field.help_text = None

    return render(request, 'passchange.html', {'form': form, 'type': 'Password Set'})
