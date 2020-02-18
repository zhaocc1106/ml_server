from django.contrib import admin
from .models import AutoPainter


class AutoPainterAdmin(admin.ModelAdmin):
    # Detail page.
    fieldsets = [
        ('Time', {'fields': ['pub_date']}),
        ('Class', {'fields': ['class_name']}),
        ('Begin stroke', {'fields': ['begin_stroke']}),
        ('Follow stroke', {'fields': ['follow_stroke']})
    ]
    # List page.
    list_display = ('pub_date', 'class_name', 'begin_stroke', 'follow_stroke',
                    'was_published_recently')
    # Filter
    list_filter = ['pub_date']
    # Search box
    search_fields = ['class_name', 'pub_date']


admin.site.register(AutoPainter, AutoPainterAdmin)
