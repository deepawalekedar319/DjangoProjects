from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
	lis_display = ['title','slug','author','bofy','publish','created','updated','status']
	prepopulated_fields = {'slug':('title',)}
	list_filter = ('status','author','created','publish')
	search_fields = ('title','body')
	raw_id_fields = ('author',)
	date_hirarchy = 'publish'
	ordering = ['status',]

admin.site.register(Post,PostAdmin)