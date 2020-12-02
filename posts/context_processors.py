from .models import Category


def context_category(request):
    category = Category.objects.all()[:6]
    return {
        'category': category
    }
