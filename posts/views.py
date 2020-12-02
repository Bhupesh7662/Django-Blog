from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comments
from .models import Category


def Index(request):
    categories = Category.objects.all()
    post_data = Post.objects.all()[:4]
    return render(request, 'post/Index.html', {'categories': categories, 'post_data': post_data})


def subcategory(request):
    post_data = Post.objects.all()
    return render(request, 'post/subcategory.html', {'post_data': post_data})


# Showing post via Title wise
def news(request, slug):
    if request.method == 'POST':
        comments_data = Comments(
            name=request.POST['name'], email=request.POST['email'], comment_desc=request.POST['comment_desc'])
        comments_data.save()

    categories = Category.objects.all()[:5]
    post_data = Post.objects.filter(post_slug=slug)
    comments = Comments.objects.filter()
    return render(request, 'post/news.html', {'post_data': post_data, 'categories': categories, 'comments': comments})


# Create Post
def add_post(request):
    if request.method == 'POST':
        post = Post(category_id=request.POST['category_id'], post_title=request.POST['post_title'], short_desc=request.POST['short_desc'],
                    long_desc=request.POST['long_desc'], author=request.POST['author'], main_image=request.FILES['main_image'], post_status=request.POST['post_status'], post_date=request.POST['post_date'])
        post.save()
        return redirect('/manage_post')

    else:
        categories = Category.objects.all()
        return render(request, 'post/add_post.html', {'categories': categories})


# Read Post
def manage_post(request):
    post_data = Post.objects.all()
    return render(request, 'post/manage_post.html', {'post_data': post_data})


# Update Post
def edit_post(request, id):
    if request.method == 'POST':
        post_details = Post.objects.get(id=id)
        post_details.post_title = request.POST['post_title']
        post_details.short_desc = request.POST['short_desc']
        post_details.long_desc = request.POST['long_desc']
        post_details.author = request.POST['author']
        post_details.post_status = request.POST['post_status']
        post_details.save()

        return redirect('/manage_post')

    else:
        categories = Category.objects.all()
        post_data = Post.objects.get(id=id)
    return render(request, 'post/edit_post.html', {'post_data': post_data, 'categories': categories})


# Delete Post
def delete_post(request, id):
    post_details = Post.objects.get(id=id)
    post_details.delete()
    return redirect('/manage_post')


# Display Comments
def display_comments(request):
    comments = Comments.objects.all()
    return render(request, 'post/display_comments.html', {'comments': comments})


# Delete Comments
def delete_comment(request, id):
    comment_details = Comments.objects.get(id=id)
    comment_details.delete()
    return redirect('/display_comments')
