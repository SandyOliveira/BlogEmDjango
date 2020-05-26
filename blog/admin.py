from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'publicado','status')
    list_filter = ('status', 'criado', 'publicado', 'autor') #campo de filtragem
    raw_id_fields = ('autor',) #serve para campos manyTomany e foreikin , inserir mais de 1 ID
    date_hierarchy = ('publicado') #navegação de pesquisa detalhado (aqui esta pela data)
    search_fields = ('title', 'conteudo') #campo pra fazer pesquisa
    prepopulated_field = {'slug': ('title',)} #slug se basear a um campo de forma automatica
