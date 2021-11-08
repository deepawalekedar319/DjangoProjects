from testapp.models import Post
from django import template
register=template.Library()

@register.simple_tag
def total_posts():
	return Post.objects.count()

@register.inclusion_tag('testapp/latest123.html')
def show_latest_post():
	latest_post=Post.objects.order_by('-publish')[:5]
	return {'latest_post':latest_post}

@register.inclusion_tag('testapp/latest123.html')
def show_search():
	latest_search=Post.objects.all().order_by('-publish')
	return {'latest_search':latest_search}

from django.db.models import Count
@register.simple_tag
def get_most_commented_posts(count=5):
	return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]