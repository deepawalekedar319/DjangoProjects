from django.contrib import admin
from testapp.models import Post,Comments

class PostAdmin(admin.ModelAdmin):
	list_display=['title','slug','author','body','publish','created','updated','status']
	prepopulated_fields={'slug':('title',)}
	list_filter=('status','author','created','publish')
	search_fields=('title','body')
	raw_id_fields=('author',)
	date_hierarchy='publish'
	ordering=['status',]

class CommentAdmin(admin.ModelAdmin):
	list_display=('name','email','post','body','created','updated','active')
	list_filter=('active','created','updated')
	search_fields=('name','email','body')

admin.site.register(Comments,CommentAdmin)
admin.site.register(Post,PostAdmin)
