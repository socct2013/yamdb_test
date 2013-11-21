from django.contrib import admin
from movies.models import Movie, Actor


class ActorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name Data',       {'fields': ['first_name', 'middle_name', 'last_name']}),
        ('Misc Info',       {'fields': ['birth_date', 'biography']}),
        ('Stars In',       {'fields': ['movies']}),
    ]

admin.site.register(Movie)
admin.site.register(Actor, ActorAdmin)