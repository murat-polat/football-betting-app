from django.contrib import admin

from .models import Team, Match, Betting

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'code', 'country')
    read_only = ('id','name', 'code', 'country')
    ordering = ('id',)
    

class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'team1', 'team2', 'score1','score2')
    readonly_fields = ('id', 'team1', 'team2', 'score1','score2')
    ordering = ('id',)

class BettingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)
admin.site.register(Match,  MatchAdmin)
admin.site.register(Betting, BettingAdmin)