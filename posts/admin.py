from django.contrib import admin
from django.utils.safestring import mark_safe

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['last_modification', 'image_tag']
    list_display = ['title', 'owner_fullname', 'image_tag', 'intro', 'status', 'publication_date', 'formatted_last_modification']
    list_filter = ['status', 'owner', 'categories']
    search_fields = ['title', 'owner__username']

    def owner_fullname(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    owner_fullname.admin_order_field = "owner__first_name"

    def image_tag(self, obj):
        return mark_safe(
            '<img src="{0}" alt="{1}" title="{1}" width="100" height="100">'.format(obj.image.url, obj.image.name)
        )

    image_tag.short_description = 'Image'

    def formatted_last_modification(self, obj):
        return obj.last_modification.strftime('%d/%m/%Y %H:%M')

    formatted_last_modification.short_description = 'Last modification date'
    formatted_last_modification.admin_order_field = 'last_modification'

    fieldsets = [
        [None, {
            'fields': ['image_tag', 'title', 'intro']
        }],
        ['Post info', {
            'fields': ['owner', 'image', 'status', 'body', 'categories']
        }],
        ['Important dates', {
            'fields': ['publication_date', 'last_modification'],
            'classes': ['collapse']
        }]
    ]
