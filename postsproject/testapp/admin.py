from django.contrib import admin
from testapp.models import Posts

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','slug','author','body','publish','created','updated','status']
	prepopulated_fields = {'slug':('title',)}
	list_filter = ('status','author','created','publish')
	search_fields = ('title','body')
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ['status',]

admin.site.register(Posts,PostAdmin)