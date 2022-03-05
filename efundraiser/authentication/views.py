from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(response, user=new_user)

        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "authentication/register.html", {"form": form})
