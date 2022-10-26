import email
import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
# Import settings
django.setup()

import random
from appTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry

        # Create Fake Data for entry
        fake_name = fakegen.name()
        fake_last_name = fakegen.name()
        fake_email = fakegen.email()

        # Create new Webpage Entry
        user = User.objects.get_or_create(first_name=fake_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')