from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from colonization_project.models import Company, User, UserProfile

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('people.json', 'r') as person_data:
            persons = json.load(person_data)
            try:
                for person in persons:
                    with transaction.atomic():
                        user_company = Company.objects.get(
                            pk=person.get('company_id'))
                        user = User.objects.create(username=person.get(
                            'name'), email=person.get('email'), company=user_company)
                        UserProfile.objects.create(
                            user=user,
                            guid=person.get('guid'),
                            has_died=person.get('has_died'),
                            balance=person.get('balance'),
                            picture=person.get('picture'),
                            age=person.get('age'),
                            eye_color=person.get('eye_color'),
                            gender=person.get('gender'),
                            about=person.get('about'),
                            registerd=person.get('registerd'),
                            address=person.get('address'),
                            phone=person.get('phone'),
                            greeting=person.get('greeting'),
                        )

            except (KeyError, IndexError) as e:
                raise BaseCommand(e)

        return self.stdout.write(self.style.SUCCESS('Persons populated'))
