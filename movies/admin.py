from django.contrib import admin
from movies.models import Movie, Actor


class ActorAdmin(admin.ModelAdmin):
    fieldsets = [
        #TODO: CSteele - This requires a stage name via admin, which the model doesn't. Make it congruent.
        ('Name Data',       {'fields': ['first_name', 'middle_name', 'last_name', 'stage_name']}),
        ('Misc Info',       {'fields': ['birth_date', 'biography']}),
        ('Stars In',       {'fields': ['movies']}),
    ]

admin.site.register(Movie)
admin.site.register(Actor, ActorAdmin)