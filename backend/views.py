from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from posts.models import Category, Post
from contact.models import Contact


def login(request):
    return render(request, 'backend/login.html')


def dashboard(request):
    users = User.objects.all().count()
    category = Category.objects.all().count()
    posts = Post.objects.all().count()
    contacts = Contact.objects.all().count()
    # context = {
    #     'users': users,
    #     'post': posts,
    #     'category': category,
    #     'contacts': contacts
    # }
    return render(request, 'backend/dashboard.html', {'users': users, 'post': post, 'category': category, 'contacts': contacts})
