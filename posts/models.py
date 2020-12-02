from django.db import models
from django.template.defaultfilters import slugify
# from category.models import Category
from tinymce.models import HTMLField

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    status = models.CharField(max_length=10, null=True, blank=True)
    # date = models.DateField()

    def __str__(self):
        return self.category_name

    @property
    def get_posts(self):
        return Post.objects.filter(category=self.id)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=150)
    short_desc = models.CharField(max_length=150)
    long_desc = HTMLField()
    author = models.CharField(max_length=150)
    main_image = models.ImageField(upload_to='media/%Y/%m/%d')
    STATUS = [
        ('0', 'Active'),
        ('1', 'Inactive'),
    ]
    post_status = models.CharField(max_length=150, choices=STATUS)
    post_date = models.DateField(auto_now_add=True)
    post_slug = models.SlugField(max_length=255, editable=False)

    def __str__(self):
        return self.post_title + ' | ' + str(self.author)

    def save(self):
        if not self.id:
            self.post_slug = slugify(self.post_title)
        super(Post, self).save()


class Comments(models.Model):
    # post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    post_slug = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    comment_desc = models.TextField()

    def __str__(self):
        return self.name + ' | ' + str(self.email)
