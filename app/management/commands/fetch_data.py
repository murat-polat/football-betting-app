# management/commands/fetch_data.py
from django.core.management.base import BaseCommand
from app.fetch_data import fetch_teams_data,fetch_match_data

class Command(BaseCommand):
    help = 'Fetch data from JSON URL and save to database'

    def handle(self, *args, **kwargs):
        fetch_teams_data()
        fetch_match_data()
        
        self.stdout.write(self.style.SUCCESS('Data fetched and saved successfully'))

        
        
        
    