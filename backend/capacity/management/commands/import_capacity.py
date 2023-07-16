import csv
from django.core.management.base import BaseCommand
from capacity.models import CapacityData

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
                CapacityData.objects.create(
                    institute=row['Institute Name'],
                    program=row['Program Name'],
                    state=row['State/All India Seats'],
                    seatType=row['Seat Pool'],
                    open=row['OPEN'],
                    openpwd=row['OPEN-PwD'],
                    ews=row['GEN-EWS'],
                    ewspwd=row['GEN-EWS-PwD'],
                    sc=row['SC'],
                    scpwd=row['SC-PwD'],
                    st=row['ST'],
                    stpwd=row['ST-PwD'],
                    obc=row['OBC-NCL'],
                    obcpwd=row['OBC-NCL-PwD'],
                    total=row['Total (includes Female Supernumerary)'],
                    capacity=row['Seat Capacity'],
                    female_supnum=row['Female Supernumerary']
                    )
    if __name__=='__main__':
        import_data()