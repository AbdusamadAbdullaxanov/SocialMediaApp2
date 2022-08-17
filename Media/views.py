from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts
from django.http import *
from django.contrib.auth.models import User
from .forms import (
    PostsForm,
    SearchBarForm
)


def index(request):
    return render(request, "check.html", {})


def return_to_home(request):
    return render(request, "homepage.html", {})


def user_information(request, pk):
    username = Posts.objects.get(id=pk)
    user = User.objects.filter(username=username).values()
    return render(
        request, "user_info.html", {"user": user}
    )


class PostsView(ListView):
    template_name = "posts.html"
    model = Posts


def search_posts(request):
    search_bar = SearchBarForm(request.POST)
    data_model = None
    if request.method == "POST":
        if search_bar.is_valid():
            request_form = search_bar.cleaned_data["search_field"]
            data_model = Posts.objects.filter(text__contains=str(request_form)).values()
    return render(
        request,
        "BasicPage.html",
        {
            "search_bar": search_bar,
            "data_model": data_model
        }
    )


def update_posts(request, pk):
    form = PostsForm(request.POST)
    if form.is_valid():
        (
            updated_user, updated_text, username
        ) = (
            form.cleaned_data["user"], form.cleaned_data["text"], request.user.username
        )
        Posts.objects.get(id=pk).delete()
        updated_model = Posts(user=updated_user, text=updated_text)
        updated_model.save()
        return HttpResponseRedirect("https://socialmedi0007.herokuapp.com/posts")
    return render(
        request, "update_post.html", {"form": form}
    )


def delete_posts(request, pk):
    print(request)
    delete_post = Posts.objects.get(id=pk)
    delete_post.delete()
    return HttpResponseRedirect("https://socialmedi0007.herokuapp.com/posts")


def create_post(request):
    print(request.user.is_authenticated)
    create_posts = PostsForm(request.POST)
    if request.method == "POST" and create_posts.is_valid():
        (
            username, text
        ) = (
            create_posts.cleaned_data["user"],
            create_posts.cleaned_data["text"]
        )
        user_name = User.objects.filter(username=username).values()
        if user_name:
            post_model = Posts(user=username, text=text)
            post_model.save()
        else:
            # __________________________________________________________________________________________________________
            print(create_posts.Meta.widgets.get("user").attrs.get("placeholder"))
            # __________________________________________________________________________________________________________
            return render(request, "error_auth.html", {})
        return HttpResponseRedirect("https://socialmedi0007.herokuapp.com")
    return render(
        request, "create_posts.html", {"create_posts": create_posts}
    )
