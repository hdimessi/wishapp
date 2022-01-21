from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def onboarding(request):
    if request.user.is_authenticated:
        return redirect('wishes:home')

    if request.POST.get("form_type") == 'signin':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('wishes:home')
            else:
                messages.error(request, 'Invalid credentials')
        except:
            messages.error(request, 'User does not exist')

    elif request.POST.get("form_type") == 'signup':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email.lower()
            try:
                user.save()
                login(request, user)
                return redirect('wishes:home')
            except:
                messages.error(request, 'User with that email already exist')

        context = {'form': form}
        return render(request, 'onboarding.html', context)
    form = SignupForm()
    context = {'form': form}
    return render(request, 'onboarding.html', context)


def signout(request):
    logout(request)
    return redirect('wishes:home')
