from django import template
from blog.models import Category, BlogPage, BlogListing

register = template.Library()


@register.inclusion_tag("blog/tags/categories.html", takes_context=True)
def get_categories(context, parent):
    bloglisting = BlogListing.objects.filter(live=True).first()
    base_url = bloglisting.url
    categories = Category.objects.all()
    for category in categories:
        category.url = f"{base_url}categories/{category.slug}"
    return {"categories": categories}


@register.simple_tag(takes_context=False)
def categories_exist():
    categories = Category.objects.count()
    return categories > 0


@register.inclusion_tag("blog/tags/get_tags.html", takes_context=True)
def get_tags(context):
    posts = BlogPage.objects.all()
    tags = []
    for post in posts:
        tags += post.get_tags
    return {"tags": sorted(tags)}

@register.simple_tag(takes_context=False)
def blog_tags_exist():
    posts = BlogPage.objects.all()
    tags = []
    for post in posts:
        tags += post.get_tags
    return len(sorted(tags)) > 0