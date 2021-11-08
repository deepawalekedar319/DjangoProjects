from testapp.models import Post
from django import template
register = template.Library()

@register.simple_tag
def total_posts():
	return Post.objects.count()


@register.inclusion_tag('testapp/latest123.html')
def show_latest_posts():
	latest=Post.objects.order_by('-publish')[:20]
	return {'latest':latest}

@register.inclusion_tag('testapp/latest123.html')
def show_all_posts():
	latest=Post.objects.order_by('-publish')
	return {'latest':latest}

from django.db.models import Count
@register.assignment_tag
def get_most_commented_posts(count=25):
	return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]