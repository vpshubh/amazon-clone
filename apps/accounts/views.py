from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in after registration
            messages.success(request, "Registration successful.")
            return redirect('product_list')  # You'll create this soon
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
from django.urls import path
from . import views