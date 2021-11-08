from task.models import Post
from django import template
register = template.Library()

@register.simple_tag
def total_posts():
	return Post.objects.count()

@register.inclusion_tag('task/latest123.html')
def show_latest_posts():
	latest_post = Post.objects.order_by('-publish')[:10]
	return {'latest_posts':latest_post}

@register.inclusion_tag('task/latest123.html')
def show_all_posts():
	latest_post=Post.objects.order_by('-publish')
	return {'latest_posts':latest_post}

from django.db.models import Count
@register.simple_tag
def get_most_commented_posts(count=5):
	return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]