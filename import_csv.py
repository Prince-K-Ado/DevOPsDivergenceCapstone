""" import csv
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstoneproject.settings')
django.setup()

from capstoneapp.models import Capstoneapp

csv_file_path = '/home/komimsi/Projects/Courses/DevOPsDivergenceCapstone/cinemaTicket_Ref.csv'

with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Create an instance of the model for each row in the CSV
        instance = Capstoneapp(film_id=row['film_id'], film_code=row['film_code'], cinema_code=row['cinema_code'], total_sales=row['total_sales'], 
                               tickets_sold=row['tickets_sold'], tickets_out=row['tickets_out'], show_time=row['show_time'], occu_perc=row['occu_perc'],
                               ticket_price=row['ticket_price'], ticket_use=row['ticket_use'], capacity=row['capacity'], date=row['date'], month=row['month'], 
                               quarter=row['quarter'], day=row['day'])
        
        # Add other fields based on your CSV structure
        instance.save() """
    
import sqlite3
import pandas as pd 
 
 # Step 1. load data file
df = pd.read_csv('movie_daily.csv')

# Step 2. 
df.columns = df.columns.str.strip()

# Step 3. Create/connect to a Sqlite databse
connection = sqlite3.connect('db.capstoneapp_capstoneapp')

# Step 4. Load data file to SQlite
# fail,replace; append
df.to_sql('capstoneapp_capstoneapp', connection, if_exists='replace', index=False)

# Step 5. Load the file to data
connection.close()