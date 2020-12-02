from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.http import HttpResponse
from posts.models import Category


# Create
def add_category(request):
    if request.method == 'POST':
        category = Category(
            category_name=request.POST['category_name'], status=request.POST['status'])
        category.save()
        return redirect('/category/manage_category')
    else:
        return render(request, 'category/add_category.html')


# Read
def manage_category(request):
    categories = Category.objects.all()
    return render(request, 'category/manage_category.html', {'categories': categories})


# update
def edit_category(request, id):
    if request.method == 'POST':
        categories = Category.objects.get(id=id)
        categories.category_name = request.POST['category_name']
        categories.status = request.POST['status']
        categories.save(update_fields=['category_name', 'status'])
        return redirect('/category/manage_category')
    else:
        categories = Category.objects.get(id=id)
        return render(request, 'category/edit.html', {'categories': categories})


# Delete
def delete_category(request, id):
    categories = Category.objects.get(id=id)
    if categories:
        categories.delete()
        return redirect('/category/manage_category')
    else:
        messages = 'error'
    return render(request, 'category/manage_category.html')
