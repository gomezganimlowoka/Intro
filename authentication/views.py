
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm


def login_user(request):

    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(
                request,
                f"Welcome back, {user.first_name or user.username}!"
            )

            next_url = request.POST.get("next") or request.GET.get("next")

            if next_url:
                from django.utils.http import url_has_allowed_host_and_scheme

                if url_has_allowed_host_and_scheme(
                    next_url,
                    allowed_hosts={request.get_host()},
                    require_https=request.is_secure()
                ):
                    return redirect(next_url)

            return redirect("home")

        else:
            messages.error(
                request,
                "Invalid username or password. Please try again."
            )

    return render(request, "auth/login.html", {"form": form})


def register_user(request):

    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            user = form.save()

            messages.success(
                request,
                "Your account has been created successfully. You can now log in."
            )

            return redirect("login")

    return render(request, "auth/register.html", {"form": form})


@login_required
def logout_user(request):

    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect("login")

    return redirect("home")
