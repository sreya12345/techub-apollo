import csv
from company.models import *

with open('company/data/esg.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = ESG.objects.get_or_create(
                name=row[2], 
                ticker=row[3], 
                activity=row[4], 
                comparison=row[5], 
                industry=row[6], 
                country=row[7], 
                rating=row[8]
            )

with open('company/data/sustainalytics.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Sustainable.objects.get_or_create(
                name=row[2], 
                ticker=row[3], 
                esg_rating=row[4], 
                risk=row[5]
            )

with open('company/data/clean_data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = SPGlobal.objects.get_or_create(
                name=row[2],
                ticker=row[1],
                industry=row[4],
                esg_score=row[3],
                environmental_score=row[5],
                social_score=row[6],
                governance_score=row[7],
            )
