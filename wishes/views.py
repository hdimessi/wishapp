from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Wish
from .forms import WishForm

@login_required(login_url='onboarding')
def homeView(request):
    ungranted_wishes = request.user.wish_set.filter(granted=None)
    granted_wishes = Wish.objects.exclude(granted=None)
    context = {
        'ungranted_wishes': ungranted_wishes,
        'granted_wishes': granted_wishes
        }
    return render(request, 'wishes.html', context)

@login_required(login_url='onboarding')
def createWishView(request):
    form = WishForm(request.POST or None)

    if form.is_valid():
        wish = form.save(commit=False)
        wish.user = request.user
        wish.save()
        return redirect("wishes:home")

    context = {
        "form": form
    }
    return render(request, 'create_wish.html', context)

@login_required(login_url='onboarding')
def editWishView(request, pk):
    wish = Wish.objects.get(id=pk)
    form = WishForm(instance=wish)

    if request.user != wish.user:
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
        form = WishForm(request.POST, instance=wish)
        if form.is_valid():
            form.save()
            return redirect("wishes:home")

    context = {
        "form": form,
        "edit": True
    }
    return render(request, 'create_wish.html', context)

@login_required(login_url='onboarding')
def deleteWish(request, pk):
    wish = Wish.objects.get(id=pk)
    if request.user != wish.user:
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
        wish.delete()
        return redirect('wishes:home')

@login_required(login_url='onboarding')
def grantWish(request, pk):
    wish = Wish.objects.get(id=pk)
    if request.user != wish.user:
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
        wish.granted = datetime.now().date()
        wish.save()
        return redirect('wishes:home')

@login_required(login_url='onboarding')
def likeWish(request, pk):
    wish = Wish.objects.get(id=pk)
    if request.user == wish.user:
        return HttpResponse('You are not allowed to like your own wish!')
    if request.method == 'POST':
        wish.likes.add(request.user)
        wish.save()
        return redirect('wishes:home')

@login_required(login_url='onboarding')
def statsView(request):
    all_wishes = Wish.objects.all()
    total_granted_wished = all_wishes.exclude(granted=None)
    print(list(total_granted_wished).count)
    my_granted_wishes = total_granted_wished.filter(user=request.user)
    my_pending_wishes = all_wishes.filter(granted=None, user=request.user)
    context = {
        'total_granted_wished': total_granted_wished,
        'my_granted_wishes': my_granted_wishes,
        'my_pending_wishes': my_pending_wishes
    }
    return render(request, 'stats.html', context)