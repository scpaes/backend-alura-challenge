from django.contrib import admin
from api.models.video import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'descricao',
        'url'
    )
    list_display_links = (
        'id',
        'titulo'
    )
    search_fields = (
        'titulo',
    )

admin.site.register(Video, VideoAdmin)