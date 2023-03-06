from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)  # Create a SignUpForm object with the POST data

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})  # Render the signup template, send the form as context
