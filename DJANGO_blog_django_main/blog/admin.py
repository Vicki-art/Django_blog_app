from django.contrib import admin
from .models import Post

admin.site.site_header = "Administrative panel for My_Blog"
admin.site.index_title = "Managing My_Blog"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'LongRead']
    list_editable = ['content', 'author']
    ordering = ['author']
    list_per_page = 2
    actions = ['set_author_country_to_Russia']
    search_fields = ['title', 'content']

    @admin.display(ordering='content', description='Long/Short')
    def LongRead(self, post: Post):
        if len(post.content) < 20:
            return 'Short'
        elif len(post.content) < 50:
            return 'Medium'
        else:
            return 'LongRead'
