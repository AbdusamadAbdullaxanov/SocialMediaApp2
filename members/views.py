from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import auth
from django.core.mail import send_mail
from .forms import (
    RegistrationForm,
    LoginUserForm,
    EmailForm,
)


def register_user(request):
    register_form = RegistrationForm(request.POST)
    if request.method == "POST":
        if register_form.is_valid():
            (
                username, firstname, lastname, email, password
            ) = (
                register_form.cleaned_data["username"],
                register_form.cleaned_data["first_name"],
                register_form.cleaned_data["last_name"],
                register_form.cleaned_data["email"],
                register_form.cleaned_data["password"]
            )
            new_user = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password
            )
            new_user.save()
            b = User(email="pythondeveloper441@gmail.com")
            b.email_user(subject="Hello", message="This is message by Abdusamad")
            return HttpResponseRedirect("https://socialmedi0007.herokuapp.com")
    return render(
        request,
        "register.html",
        {
            "register_form": register_form
        }
    )


def verify_user(request):
    email_form = EmailForm(request.POST)
    if request.method == "POST":
        if email_form.is_valid():
            (
                subject, email, sender, recipes
            ) = (
                email_form.cleaned_data["subject"],
                email_form.cleaned_data["email"],
                email_form.cleaned_data["sender"],
                ["pythondeveloper441@gmail.com"]
            )

            send_mail(
                subject=subject,
                message=email,
                from_email=sender,
                recipient_list=recipes
            )
    return render(
        request, "email.html", {"email_form": email_form}
    )


def login_user(request):
    login_form = LoginUserForm(request.POST)
    if request.method == "POST":
        if login_form.is_valid():
            username, password = login_form.cleaned_data["username"], login_form.cleaned_data["password"]
            authentication = authenticate(username=username, password=password)
            auth.login(request, authentication)
            print(request.user.is_authenticated)
            return HttpResponseRedirect("https://socialmedi0007.herokuapp.com")
    return render(
        request,
        "login.html",
        {
            "login_form": login_form
        }
    )


def logout_user(request):
    logout(request)
    print(request.user.is_authenticated)
    return HttpResponseRedirect("https://socialmedi0007.herokuapp.com")
