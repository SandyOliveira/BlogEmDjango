from django.contrib import admin

from .models import Post, Category


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display =('nome','criado','publicado')
    list_filter = ('nome','criado','publicado')
    date_hierarchy = 'publicado'
    search_fields = ('nome',)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'publicado','status')
    list_filter = ('status', 'criado', 'publicado', 'autor') #campo de filtragem
    readonly_fields = ('view_image',) #aparecer a imagem para o admin('view_image')
    raw_id_fields = ('autor',) #serve para campos manyTomany e foreikin , inserir mais de 1 ID
    date_hierarchy = 'publicado' #navegação de pesquisa detalhado (aqui esta pela data)
    search_fields = ('title', 'conteudo') #campo pra fazer pesquisa
    prepopulated_field = {'slug': ('title',)} #slug se basear a um campo de forma automatica


#mudando o nome view_image

def visualizar_imagem(self,obj):
    return obj.view_image
    visualizar_imagem.short_description = "Imagem Cadastrada"