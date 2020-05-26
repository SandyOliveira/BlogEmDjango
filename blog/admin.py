from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'publicado','status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    raw_id_fields = ('autor',)
    date_hierarchy = ('publicado')
    search_fields = ('title', 'conteudo')
    prepopulated_field = {'slug': ('title',)}
