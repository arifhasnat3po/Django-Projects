import os
import django
from faker import Faker
from first_app.models import Topic, Webpage, AccessToken
from django.utils import timezone

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')  # Adjust the path accordingly
django.setup()
# Create an instance of the Faker class
fake = Faker()

# Function to create fake data for Topic model
def create_topic():
    topic_name = fake.word()
    topic = Topic.objects.create(top_name=topic_name)
    return topic

# Function to create fake data for Webpage model
def create_webpage(topic):
    name = fake.company()
    url = fake.url()
    webpage = Webpage.objects.create(topic=topic, name=name, url=url)
    return webpage

# Function to create fake data for AccessToken model
def create_access_token(webpage):
    date = fake.date_between(start_date='-30d', end_date='today')
    access_token = AccessToken.objects.create(name=webpage, date=date)
    return access_token

# Populate the models with fake data
def populate_data(num_entries=10):
    for _ in range(num_entries):
        topic = create_topic()
        webpage = create_webpage(topic)
        create_access_token(webpage)

if __name__ == '__main__':
    # Change the argument to populate more or fewer entries
    populate_data(10)
    print("Data populated successfully.")
