import csv
from django.core.management.base import BaseCommand
from analyser.models import JosaaData

class Command(BaseCommand):
    help = 'Import data from CSV file to SQLite database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        self.import_data(csv_file)

    def import_data(self, csv_file):
        
        with open(csv_file, 'r') as file:
            csv_data=csv.DictReader(file)
            for row in csv_data:
                JosaaData.objects.create(
                    institute=row['Institute'],
                    program=row['Academic Program Name'],
                    quota=row['Quota'],
                    seatType=row['Seat Type'],
                    gender=row['Gender'],
                    openrank=row['Opening Rank'],
                    closerank=row['Closing Rank'],
                    year=row['Year'],
                    round=row['Round']
                    )
    if __name__=='__main__':
        import_data()