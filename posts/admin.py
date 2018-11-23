from django.contrib import admin
from django.utils.safestring import mark_safe

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['pub_date', 'last_modification', 'image_tag']
    list_display = ['title', 'owner_fullname', 'image_tag', 'status', 'formatted_publication_date', 'formatted_last_modification']
    list_filter = ['status', 'owner']
    search_fields = ['title', 'owner__username']

    def owner_fullname(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    owner_fullname.admin_order_field = "owner__first_name"

    def image_tag(self, obj):
        return mark_safe(
            '<img src="{0}" alt="{1}" title="{1}" width="100" height="100">'.format(obj.image.url, obj.image.name)
        )

    image_tag.short_description = 'Image'

    def formatted_publication_date(self, obj):
        return obj.pub_date.strftime('%d/%m/%Y %H:%M')

    formatted_publication_date.short_description = 'Pub date'
    formatted_publication_date.admin_order_field = 'pub_date'

    def formatted_last_modification(self, obj):
        return obj.last_modification.strftime('%d/%m/%Y %H:%M')

    formatted_last_modification.short_description = 'Las modification date'
    formatted_last_modification.admin_order_field = 'last_modification'

    fieldsets = [
        [None, {
            'fields': ['image_tag', 'title', 'intro']
        }],
        ['Post info', {
            'fields': ['owner', 'image', 'status', 'body']
        }],
        ['Important dates', {
            'fields': ['publication_date', 'pub_date', 'last_modification'],
            'classes': ['collapse']
        }]
    ]
